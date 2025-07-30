
###
#? 04 - Listas Métodos
#? Los métodos más importantes para trabajar con listas
###


from os import system
if system("clear") != 0: system("cls")

#! Añadir elementos a una lista
lista1 = ['a', 'b', 'c', 'd']

lista1.append('e') #* esto añade un elemento al final de la lista
print(lista1)

lista1.insert(1, '@') #* Inserta un elemento en la posicion que le indiquemos como primer argumento
print(lista1)

lista1.extend(['😃', '😍']) #* Agregar elementos al final de una lista
print(lista1)

#! Eliminar elementos de una lista
lista1.remove('@') #* Eliminar la primera aparicion de la cadena de texto
print(lista1)

ultimo = lista1.pop() #* Elimina el ultimo elemento de la lista y lo devuelve
print("Elemento borrado:", ultimo)
print("Lista actualizada:", lista1)

lista1.pop(1) #! --> basicamente recibe el indice valor por defecto: -1 el ultimo
print("Lista con índice borrado:", lista1)