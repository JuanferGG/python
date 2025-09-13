###
#? 03 - Quantifiers
#? Los cuantificadores se utilizan para especificar cuántas ocurrencias de un 
#? carácter o grupo de caracteres se deben encontrar en una cadena.
###

from os import system
import re

if system("clear") != 0: system("cls")

# *: Puede aparecer 0 o más veces
text = "aaaba"
pattern = "a*"

matches = re.findall(pattern, text)
print(f"Cantidad de matches encontrados: {matches}")


#? Ejercicio 1:
#? ¿Cuantas palabras tienen de 0 a más "a" y después una b?
text = "dddd aaa ccc ab a bb aa casa"
pattern = "a+b"

matches = re.findall(pattern, text)
print(f"\nMatches encontrados: {matches}")


#! ?: Cero o una vez
text = "aaabacb"
pattern = "a?b"

matches = re.findall(pattern, text)
print(f"\nMatches encontrados: {matches}")


#! {n}: Exactamente n veces
text = "aaaaaa         aa   aaaa"
pattern = "a{3}"

matches = re.findall(pattern, text)
print(f"\nMatches encontrados: {matches}")


#! {n, m}: De n a m veces
text = "u uu uuu u uuuu"
pattern = r"\w{2,3}"

matches = re.findall(pattern, text)
print(f"\nMatches encontrados: {matches}")



#? Ejercicio:
#? Encuentra las palabras de 4 a 6 letras en el siguiente texto
words = "ala casa árbol león cinco murcielago"
pattern = r"\b\w{4,6}\b"

matches = re.findall(pattern, words)
print(f"\nEjercicio #1: {matches}")

#? Ejercicio
#? Encuentra las palabras de más de 6 letras
words = "ala fantastico casa árbol león cinco murcielago"
pattern = r"\b\w{6,}\b"

matches = re.findall(pattern, words)
print(f"\nEjercicio #2: {matches}")


