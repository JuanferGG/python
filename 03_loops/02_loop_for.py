###
#? 02 - Bucles (for)
#? Permiten ejecutar un bloque de código repetidamente mientras ITERA un iterable o una lista
###

from os import system
if system("clear") != 0: system("cls")

print("\n-- Bucle For --")

#! Iterar en una lista
frutas = ["manzana", "pera", "mandarina"]
for fruta in frutas:
    print("Fruta: ", fruta)

#! Iterar sobre cualquier cosa que sea iterable
print("\n-- For sobre un cade de texto --")
cadena = "textolargo"
for caracter in cadena:
    print("Letra:", caracter)

#? Enumerate()
frutas = ["manzana", "pera", "mandarina"]
for idx, value in enumerate(frutas):
    print(f"El indice es: {idx}, y la fruta es: {value}")

#! bucles anidados
print("\n-- Bucles anidados --")
letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras:
    for numero in numeros:
        print(f"letra:{letra}, numero: {numero}")

#? break
print("\n-- For with break --")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]

for idx, animal in enumerate(animales):
    print("Animal: ", animal)
    if animal == "loro":
        print(f"El loro esta escondido en el indice: {idx}")
        break

#? continue
print("\n-- For with continue --")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales):
    if animal == "loro":
        continue

    print(f"Animales: {animal}")

#! Comprensión de listas (list comprehension)
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
animales_mayus = [animal.upper() for animal in animales]
print(f"Animales mayus: {animales_mayus}")

#! Muestra los números pares de una lista
pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print("Pares:", pares)