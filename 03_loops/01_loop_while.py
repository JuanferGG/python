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

#! utilizando la palabra break, para romper el bucle

print("\n-- Bucle while con break --")
contador = 0

while True:
    print("El contador es:", contador)
    contador += 1
    if contador == 5:
        break #* Sale del bucle


#? continue, lo que hace es saltar esa iteración en concreto
#? y continuar con el bucle

print("\n-- Bucle con continue --")
contador = 0
while contador < 10:
    contador += 1

    if contador % 2 == 0:
        continue

    print("Contador:", contador)


#? else, esta condición cuando se ejecuta?
print("\n-- Bucle while con else --")
contador = 0
while contador < 5:
    print("contador:", contador)
    contador += 1
else:
    print("EL bucle ha terminado")


#? pedirle al usuario un número que tiene
#? que ser positivo si no, no le dejamos en paz

numero = -1
while numero < 0:
    numero = int(input("Escribe un número positivo:"))
    if numero < 0:
        print("El numero debe ser positivo. Intentalo de nuevo")
    
    print(f"El numero introducido es {numero}")


numero = -1

while numero < 0:
    try:
        numero = int(input("Escribe un numero positivo:"))
        if numero < 0:
            print("EL numero debe ser positivo. Intenta otra vez")
    except:
        print("El valor tomado de be ser un numero sino peta XD!")

    print(f"El numero ingresado fue: {numero}")