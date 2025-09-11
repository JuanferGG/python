###
#? 02 - Meta caracteres
#? Los metacaracteres son simbolos especiales con significados especificos en las expresiones regulares
###
from os import system
import re

if system("clear") != 0: system("cls")

#! 1. El punto (.)
#! Coincidir con cualquier caracter excepto una nueva linea

text = "Hola mundo, H0la de nuevo, H$la otra vez"
pattern = "H.la" #? ---> Hola, H0la, H$la

found = re.findall(pattern, text)

if (found):
    print(f"Caracteres encontrados: {found}")
else:
    print("No se ha encontrado nada")


text = "casa caasa cosa cisa cesa causa"
pattern = "c.sa"

matches = re.findall(pattern, text)

if (matches):
    print(f"\nMatches encontrados para c.sa: {matches}")
else:
    print("ningun coincidencia encontrado")

#! -----------------

text = "Hola mundo, H0la de nuevo, H$la otra vez"
pattern = r"H.la"

found = re.findall(pattern, text)

if (found):
    print(f"\nMatches encontrados para r'H.la': {found}")
else:
    print("No he encontrado nada")

#! Cómo usar la barra invertida para anular el significado especial de un símbolo

text = "Mi casa es blanca. Y el coche es negro."
pattern = r"\."

matches = re.findall(pattern, text)

print(f"\nMatches encontrados (.): {matches}")

#! \d: coincide con cualquier dígito (0-9)

text = "El número de teléfono es 123456789"
found = re.findall(r"\d{9}", text)

print(f"\nMatch encontrados el 1-9: {found}")



#! Ejercicio: Detectar si hay un número de España en el texto gracias al prefijo +34
text = "Mi número de teléfono es +34 688999999 apúntalo vale?"
found = re.findall(r"\+34 \d{9}", text)

if (found):
    print(f"\nNumero encontrado: {found}")
else: 
    print("\nnumero no encontrado")

#! \w: Coincide con cualquier caracter alfanumerico (a-z, A-Z, 0-9, _)
text = "el_rubius_69"
pattern = r"\w"

found = re.findall(pattern, text)

print(f"\nCualquier caracter alfanumerico: {found}")


#! \s: Coincide con cualqueir espacio en blanco (espacio, tabulación, salto de línea)
text = "Hola mundo\n¿Cómo estás?\t"
pattern = r"\s"

found = re.findall(pattern, text)

print(f"\n matches: {found}")

#! ^: Coincide con el principio de una cadena
username = "423_name%22"
pattern = r"^\w" # validar nombre de usuario

valid = re.search(pattern, text)

if valid: print("El nombre de usuario es valido")
else: print("El nombre de usuario no es valido")

phone = "+54 688999999"
pattern = r"^\+\d{1,3}"

valid = re.search(pattern, phone)

if valid: print(f"El numero {phone} es valido")
else: print("El numero no es valido")