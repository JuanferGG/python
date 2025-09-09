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

