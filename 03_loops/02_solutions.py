###
#? EJERCICIOS (for)
###

from os import system
if system("clear") != 0: system("cls")

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")
numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pares = [num for num in numeros if num % 2 == 0]
print("Pares del 2-20:", pares)

# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")
numeros = [10, 20, 30, 40, 50]
media = 0
for num in numeros:
    media = media + num
media = media / len(numeros)
print(f"la media de los {numeros} es: {media}")

# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")
numeros = [15, 5, 25, 10, 20]
num_max = 0

for num in numeros:
    if num > num_max:
        num_max = num
print("Numero max:", num_max)

# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")
palabras = ["casa", "arbol", "sol", "elefante", "luna"]
new_lista = []

for palabra in palabras:
    long_palabra = len(palabra)
    if long_palabra > 5:
        new_lista.append(palabra)
print("Lista nueva con palabras mayor a 5 letras:", new_lista)

nueva_lista = [palabra for palabra in palabras if len(palabra) > 5]
print(nueva_lista)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")
palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
print("Lista:", palabras)
letra = str(input("Introduce una letra: ")).lower()
new_list = [ palabra for palabra in palabras if list(palabra)[0] == letra ]

print("Nueva lista de palabras", new_list)