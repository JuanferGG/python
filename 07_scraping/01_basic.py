
#! pip3 install requests -> instalas la dependencia para hacer peticiones

from os import system
import requests
import re

if system("clear") != 0: system("cls")

url = 'https://www.apple.com/es/shop/buy-mac/macbook-air/'

response = requests.get(url)

if response.status_code == 200:
    print("- Peticion exitosa -")

    html = response.text
    #* print(html)

    #? regular expression para encontrar el precio
    price_pattern = r'<span class="rc-prices-fullprice">(.*?)</span>'
    match = re.search(price_pattern, html)

    if match:
        print(f"El del producto es: {match.group(1)}")

    #? get the title if the patter is found
    title_patter = r"<title>(.*?)</title>"
    match = re.search(title_patter, html)

    if match:
        print(f"El titulo de la web es: {match.group(1)}")