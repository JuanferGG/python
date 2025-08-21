"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, 
como el temible T-Rex, depositan un número par de huevos. 
Imagina que tienes una lista de números enteros en la que cada 
número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros 
y devuelva la suma total de los huevos que pertenecen a los 
dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""

lista_ejemplo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def suma_num_pares(lista):
    count_sum = 0
    for num in lista:
        if num % 2 == 0:
            count_sum = count_sum + num
        
    
    return  print(f"La suma de los huevos es: {count_sum}")


def sum_num_pares_2(lista):
    return print(f"La suma de los huevos es: {sum(num for num in lista if num % 2 == 0)}")



suma_num_pares(lista_ejemplo)
sum_num_pares_2(lista_ejemplo)