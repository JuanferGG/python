###
#? 02 - types()
#? Python tiene varios tipos de datos
#? int, float, complex, str, bool, NoneType, list, tuple, dict, range, set...
###

"""
    esto es un comentario
    en multiLinea sino se asigna es un comentario normal
"""

print("Int:")
print(5)
print("tipo" ,type(10))
# print(0)
# print(-7)

print('------- | -------')

print("Float:")
print(3.2)
print("tipo:" ,type(4.5))
print("tipo:" ,type(1e3))
# print(type(0.5))

print('------- | -------')

print("Complex:")
print("tipo", type(1 + 3j))
print(1 + 1j)

print('------- | -------')

print("Str:")
print(type("hola"))
print(type(""))
print(type("123"))
print(type("""
    multiLinea 
"""))

print('------- | -------')

print("Bool:")
print(1 < 2)
print(1 > 2)
print(type(True))
print(type(False))

print('------- | -------')

print("NoneType:")
print(type(None))