###
#? 05 - Entrada de usuario (input()) - Versión simplificada
#? La función input() permite obtener datos del usuario a través de la consola.
###

# print("Hola, como te llamas?")
nombre = input("Hola Como te llamas?\n")

print("Tu nombre es:", nombre.capitalize())
print(type(nombre))

print('------- | -------')

age = int(input("Cuantos años tienes: "))
print(f"Dentro de 5 años tendras {age + 5} años")

print('------- | -------')

print("Multiples valores a la vez")
country, city = input("En que pais y ciudad vives?\n").split()

print(f"Vives en {country.capitalize()}, {city.capitalize()}")
