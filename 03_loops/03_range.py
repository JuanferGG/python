###
#? 03 - range()
#? Permite crear una secuencia de números. Puede ser útil para for, pero no solo para eso
###


from os import system
if system("clear") != 0: system("cls")

print("\n-- Range(): --")

#! Generado una secuencia de números del 0 al 9
for num in range(10):
    print(f"Num: {num}")

#! range(inicio, fin)
print("\n-- Range desde hasta --")
for num in range(5, 10):
    print(f"Num: {num}")


#! range(inicio, fin, paso)
print("\n-- Range(inicio, fin, paso)")
for num in range(0, 20, 5):
    print(f"Num: {num}")

print("\nDesde negativos")
for num in range(-5, 0):
    print(f"Num: {num}")


print("\nHacia atras")
for num in range(10, 0, -1):
    print(f"Num: {num}")


# for num in range(0, 444):
#     print(f"Num: {num}")

nums = range(10)
list_of_nums = list(nums)
print(f"\nLista de numeros: {list_of_nums}")

#! Sirve para ejecutar algo 5 veces
for _ in range(5):
    print("Hacer algo 5 veces!")


