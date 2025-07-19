###
#? 03 - casting de types
#? Transformar un tipo de un valor a otro
###

print("Conversion de tipos:")

print(2 + int("100"))
print("100" + str("5"))
print('------- | -------')
print(type(float("3.1416")))
print(int(3.1416))
print('------- | -------')
print(bool(7))
print(bool(0)) #! -----> cero es el unico que da False
print(bool(-5))
print("Strings ----> bool")
print(bool(""))
print(bool(" "))
print(bool("False"))
print('------- | -------')

print("---> Tener en cuenta esto!")
print(int(2.5))
print(round(3.5)) #! el round acerca al par mas cercano en este caso a 4 pero si fuera 2.5 a 2