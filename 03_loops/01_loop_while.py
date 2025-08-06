###
#? 01 - Bucles (while)
#? Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición
###

from os import system
if system("clear") != 0: system("cls")

print("--- Bucle While --")

#! Bucle While con una simple condicion

contador = 0

while contador <= 5:
    print("El contador es:", contador)
    contador += 1

