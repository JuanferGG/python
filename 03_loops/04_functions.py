###
#? 04 - Funciones
#? Bloques de código reutilizables y parametrizables para hacer tareas especificas
###

from os import system
if system("clear") != 0: system("cls")


#! """ Definición de una función

#* def nombre_de_la_funcion(parametro1, parametro2, ...):
    #* docstring
    #* cuerpo de la función
    #* return valor_de_retorno

#? Ejemplo de una función para imprimir algo en consola
def imprimir_algo():
    print("Hola!")

imprimir_algo()


#? Ejemplo de una funcion con parametro

def saludar(nombre : str):
    print(f"\nHola {nombre}!, como estas?")

saludar("Luis")


def sumar(a : int, b : int):
    suma = a + b
    return suma


result = sumar(4, 7)
print(f"\nEl resultado es: {result}")

#! Documentar las funciones con docstring

def restar(a : int, b : int):
    """Resta dos números y devuelve el resultado"""
    return a - b

print(f"\nLa resta de 7 y 5 es: {restar(7, 5)}")


#! parámetros por defecto
def multiplicar(a : int, b : int = 2):
    """Multiplicacion de 2 numeros y retorna el resultado, por defecto b = 2"""
    return a * b

print(f"\nLa multiplicacion por defecto de 4x2 es: {multiplicar(4)}")
print(f"a:5 b:8 = {multiplicar(5, 8)}")

#! Argumentos por posición
def describir_personas(nombre: str, edad : int, sexo : str):
    print(f"\nSoy {nombre}, tengo {edad} y me identifico como {sexo}")

describir_personas("Mario", 79, "helicoptero apache")
describir_personas("midudev", 25, "gato")
# describir_personas("hombre", "madeval", 39) ----> igual pasa al momento de ejecucion

#! Argumentos por clave
#! parámetros nombrados

describir_personas(sexo ="MotoGT", edad = 7, nombre = "luis")

#! Argumentos de longitud de variable (*args):
def sumar_numeros(*arg):
    suma = 0
    for numero in arg:
        suma += numero
    return suma

print(f"\nLa suma de los numeros del 1-7 es: {sumar_numeros(1, 2, 3, 4, 5, 7)}")
print(sumar_numeros(2, 2))

#! Argumentos de clave-valor variable (**kwargs):
def mostrar_inf_de(**kwargs):
    for clave, valor in kwargs.items():
        print(f"clave: {clave}, valor: {valor} ")

mostrar_inf_de(nombre = "midudev", edad = 5, sexo = "gato albino montez")
print("\n")
mostrar_inf_de(name = "Mario", last_name = "Castañeda" , lvl = 78, country = "Costa Rica")
print("\n")
mostrar_inf_de(super_name="felixicaza", es_modo=True, gatos=40)