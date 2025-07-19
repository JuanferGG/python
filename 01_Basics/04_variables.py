##
#? 04 - Variables
#? Las variables sirven para guardar datos en memoria.
#? Python es un lenguaje de tipado dinámico y de tipado fuerte.
###

#* asignar una variable de manera simple
my_name = "JuanferGG"

print("Hola," ,my_name)

print('------- | -------')

age = 32
print("el age es:", age)
age = 39
print("el age es:", age)

#* Las variables en python son reasignables en ejecucion.

print('------- | -------')

#? Tipado dinámico
name = "Luis"
print(type(name))

name = 32
print(type(name))

print('------- | -------')
#* F-String
print(f"Hola {my_name}, tienes {age} años")

#! no recomendada forma de asignar varias variables
lastName, age2, city = "apellido", 7, "Bogota"
print(lastName, age2, city)

#* Conveciones de nombres de variables
mi_nombre_de_variable = "ok" #snake_case

MiNombreDeVariable = "ko" # pascal_case

MI_CONSTANTE = "constante" #! para evitar confunsion las constantes serán en upperCase

#* Tipado fuerte
print('------- | -------')
is_user_logged_in: bool = True
print(is_user_logged_in)

# is_user_logged_in = 42
# print(is_user_logged_in)