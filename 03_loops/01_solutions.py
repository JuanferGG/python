###
#? EJERCICIOS (while)
###

from os import system
if system("clear") != 0: system("cls")

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")
numbers = 10
while numbers > 0:
    print("conteo:", numbers)
    numbers -= 1

# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")
numbers = 1
suma = 0

while numbers <= 20:
    if numbers % 2 == 0:
        suma = suma + numbers
    
    numbers += 1

print(f"La suma total es: {suma}")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")
number = -1

while number < 0:
    try:
        number = int(input("Escribe un número positivo: "))
        if number < 0:
            print("----> El número debe ser positivo!")
        else:
            factorial = 1
            pasos = [] 
            temp = number
            
            while temp > 0:
                pasos.append(str(temp))
                factorial *= temp
                temp -= 1
            
            print(f"{' x '.join(pasos)} = {factorial}")
    except ValueError:
        print("Debe ser un número! <----")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")
password = ""
long_pass = []

while len(long_pass) < 8:
    try:
        password = str(input("Ingresa una contraseña:"))
        long_pass = list(password)
        if len(long_pass) < 8:
            print("La contraseña deber ser mayor a 8 caracteres:")
        else :
            print("Contraseña guardada corrextamente")

    except ValueError:
        print("---> Debe ser un string")


# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")
num_tabla = -1

while num_tabla < 0:
    try:
        num_tabla = int(input("Ingresa un numero de tabla: "))
        if num_tabla < 0:
            print("Debe ser positivo el número <---")
        else:
            contador = 1
            while contador <= 10:
                print(f"{num_tabla} x {contador} = {num_tabla*contador}")
                contador += 1

    except ValueError:
        print("---> Debe ser un numero")


# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
print("\nEjercicio 6:")
exit = False

while exit != True:
    try:
        n = int(input("Introduce un número entero positivo N: "))
        if n < 2:
            print("No hay números primos menores o iguales a", n)
        else:
            list_num_primos = []
            numero = 2
            while numero <= n:
                es_primo = True
                divisor = 2
                while divisor * divisor <= numero:
                    if numero % divisor == 0:
                        es_primo = False
                        break
                    divisor += 1
                if es_primo:
                    # print(numero)
                    list_num_primos.append(numero)
                numero += 1
            print("Numeros primos:", list_num_primos)
            exit = True
    except ValueError:
        print("---> Debe ser un número entero")
