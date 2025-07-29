###
#? 03 - Listas
#? Secuencias mutables de elementos.
#? Pueden contener elementos de diferentes tipos.
###


from os import system
if system("clear") != 0: system("cls")

#? Creación de listas
print("\nCrear listas")
lista1 = [1, 2, 3, 4, 5] #? lista de enteros
lista2 = ["manzanas", "peras", "plátanos"] #? lista de cadenas
lista3 = [1, "hola", 3.14, True] #? lista de tipos mixtos


#? Lista Vacias
lista_vacias = []
lista_de_listas = [[1, 2], [3, 4]]
matrix = [[1, 2], [3, 4], [5, 6]]

print("lista 1:", lista1)
print("lista 2:",lista2)
print("lista 3:",lista3)
print("Lista vacia:", lista_vacias)
print("Lista de listas:", lista_de_listas)
print("matrix:", matrix)

#? Acceso a elementos por indice
print("\n-Acceso a elementos por indice-")
print(lista2[0]) #*manzanas
print(lista2[1]) #*peras
print(lista2[-1]) #*platanos puedes hacer de atras hacia adelante o lo q es igual a numeros negativos -1 --> ultimo de atras hacia adelante


print(lista_de_listas[-1][0])

#? Slicing
print("\nSlicing 1-4:", lista1[1:4]) #* [2,3,4]
print("Desde el principio hasta x:", lista1[:3])  #* [1,2,3]
print("Desde el final hasta x:", lista1[2:]) #* [3, 4, 5]
print("Hacer una copia de una lista:", lista1[:]) #* [1, 2, 3, 4, 5]


#? Final el "paso" tercer parametro 
lista4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("\nEl paso es el tercer parametro Lista[desde:hasta:paso]")
print("Lista4:", lista4[::2])
print("Lista invertida con paso:", lista4[::-1])

#? Modificar listas
lista5 = [1, 2, 3, 4, 5, 6, 7]
print("\nModificando lista #5:", lista5)
lista5[1] = 20
print("Modificado:",lista5)

#? Añadir elementos a una lista
print("Añadiendo mas elementos a lista #5.")
#! Forma larga
lista5 = lista5 + [8, 9, 10]
print(lista5)
#! Forma corta y mas eficiente
print("Forma corta y mas eficiente:")
lista5 += [11, 12, 13, 14]
print(lista5)


#? Recuperar longitud de una lista
print("\nLongitud de la lista", len(lista1))