###
#? 01 - Sentencias condicionales (if, elif, else)
#? Permiten ejecutar bloques de código solo si se cumplen ciertas condiciones.
###

from os import system
if system("clear") != 0: system("cls")

print("-Sentencia simple condicional-")

age = int(input("\nDigite su edad:\n"))

if age >= 18:
    print("Eeres mayor de edad")
else:
    print("Eres menor de edad")


print("\n-Sentencia elif-")

nota = int(input("Escriba su nota final:\n"))

if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >=5:
    print("Aprovado")
else:
    print("Reprovado")


print("\n-Condiciones multiples-")

edad = 25
have_card = False

#! and
if edad >= 18 and have_card:
    print("Puedes conducir")
else:
    print("No puedes conducir")
#! or
if edad >= 18 or have_card:
    print("Puedes conducir")
else:
    print("No puedes conducir")

#! not
es_fin_semana = False

if not es_fin_semana:
    print("Es fin de semana hay que salir!")


print("\n-Anidar Condicionales-")
edad_2 = 20
have_money = True

#! Evitar muchos if y else menos legible
if edad_2 >= 18:
    if have_money:
        print("Pueder entrar a la discoteca")
    else:
        print("Quedate en casa")
else:
    print("No puedes entrar a la disco")

#* Mejor caso de uso mismo resultado

if edad_2 < 18:
    print("No puedes entrar a la disco")
elif have_money:
    print("Puedes ir a la disco")
else:
    print("Quedate en casa")


numero = 5
if numero: #? True
    print("El numero no es cero")

nombre = "Juan"
#! nota: una cadena de texto vacio se evalua como False
if nombre:
    print("El nombre no esta vacio")

#* ¡Ten cuidado con no confundir la asignación = con la comparación ==!
numero = 3 # asignación
es_el_tres = numero == 3 # comparación

if es_el_tres:
  print("El número es 3")

#* A veces podemos crear condicionales en una sola línea usando
#* las ternarias, es una forma concisa de un if-else en una línea de código

print("\nLa condición ternaria:")
# [código si cumple la condición] if [condicion] else [codigo si no cumple]

edad_3 = 17
mensaje = "Es mayor de edad" if edad_3 >= 10 else "Es menor"
print(mensaje)


