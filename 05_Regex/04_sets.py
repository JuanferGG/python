from os import system
import re

if system("clear") != 0: system("cls")

#! [:] Coincide con cualquier caracter dentro de los corchetes

username = "rub.$ius_69+"
pattern = r"^[\w._%+-]+$"

match = re.search(pattern, username)

if match:
    print(f"El nombre de usuario es valido: {match.group()}")
else:
    print("Nombre invalido!")


#! Buscar todas las vocales de una palabra
text = "Hola mundo"
pattern = r"[aeiuo]"

matches = re.findall(pattern, text)

print(f"\nMatches encontrados: {matches}")


#! Una Regex para encontrar las palabras man, fan y ban
#! pero ignora el resto

text = "man ran fan ñan ban"
pattern = r"[mfb]an"

matches = re.findall(pattern, text)

print(f"\nMatches encontrados para man, fan & ban: {matches} ")

#! [^]: Coincide con cualquier caracter que no esté dentro de los corchetes
text = "Hola mundo"
pattern = r"[^aeiou]"

matches = re.findall(pattern, text)

print(f"\nMatches encontrados: {matches}")

#? Ejercicio:
#? Nos han complicado el asunto, porque ahora hay palabras que encajan pero no empiezan por esas letras.
#? Solo queremos las palabras man, fan y ban
text = "omniman fanatico man bandana"

pattern = r"\b[mbf]an\b"

matches = re.findall(pattern, text)

print(f"\nEjercicio #1: {matches}")

