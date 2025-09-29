from os import system
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests

if system("clear") != 0: system("cls")

def scrape_url(url:str):
    headers = {
        'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/131.0.0 Safari/537.36'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("-- La peticion fue exitosa --")

        soup = BeautifulSoup(response.text, "html.parser")

        #? Extraer todos los titulos
        titulos = [titulo.string for titulo in soup.find_all("h1")]
        print(f"\nLos titulos: {titulos}")

        #? Extraer todos los enlaces
        enlaces = [urljoin(url, enlace.get('href')) for enlace in soup.find_all('a')]
        # print(f"\nTodos los enlaces: {enlaces}")


        #? Extraer todo el contenido de la pagina texto
        all_text = soup.get_text()
        # print(f"\nTodo el texto de la pagina: {all_text}")

        #? Extraer todo el texto del main
        main_text = soup.find("main").get_text()
        # print(f"\nTexto del main: {main_text}")

        #? Extraer de la id mw-content-text
        # content_text = soup.find('div', {'id': 'mw-content-text'}).get_text()
        # print(f"\nContenido del textopor id: {content_text}")

        #? extrar el open graph si existe
        og_image = soup.find('meta', property='og:image')
        if og_image:
            print(og_image['content'])
        else:
            print("no se ha encontrado la imagen")



scrape_url("https://midu.dev")