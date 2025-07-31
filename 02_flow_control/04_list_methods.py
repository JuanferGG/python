
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

#! Eliminar por lo bestia
del lista1[-1]
print(lista1)

lista1.clear() #* Elimina todos los elementos de la lista
print(lista1)

#! ELiminar un rango de elementos
lista2 = ['🐼', '🐨', '🐶', '😿', '🐹']
del lista2[1:3]
print(lista2)

#! mas metodos utiles
print('Ordenar listas modificando la original')
numbers = [3, 10, 2, 8, 99, 101]
numbers.sort()
print('Modificando lista:', numbers)

print('Ordenar listas creando una nueva')
numbers = [3, 10, 2, 8, 99, 101]
sorted_numbers = sorted(numbers)
print('Lista nueva:', sorted_numbers)

print("Ordenar una lista de cadenas de texto (mezclas mayúscula y minúscula)")
frutas = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
sorted_frutas = sorted(frutas)
print('Frutas minusculas ordenadas:', sorted_frutas)

frutas = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
frutas.sort(key=str.lower)
print(frutas)

#! Más cositas útiles
animals = ['🐶', '🐼', '🐨', '🐶']
print('Tamaño de lista', len(animals)) #? Tamaño de la lista
print('Cantidad de veces repetido', animals.count('🐶')) #? Cuantas veces aparece un elemento
print('🐼' in animals) #? Comprueba si hay un '🐼' en la lista -> True

