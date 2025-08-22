###
#? 04 - Dictionaries
#? Los diccionarios son colecciones de pares clave-valor.
#? Sirven para almacenar datos relacionados.
###


from os import system
if system("clear") != 0: system("cls")

#! ejemplo tipico de diccionario
persona = {
    "nombre": "midudev",
    "edad": 25,
    "es_estudiante": True,
    "calificaciones": [7, 8, 9],
    "socials": {
        "twitter": "@Midudev",
        "instagram": "@Midudev",
        "facebook": "Midudev"
    }
}


#! para acceder a los valores
print(persona["nombre"])
print(persona["calificaciones"][2])
print(persona["socials"]["twitter"])

#! cambiar valores al acceder
persona["nombre"] = "madeval"
persona["calificaciones"][2] = 10

# print(persona)

#! eliminar completamente una propiedad
del persona["edad"]
# print(persona)

#? pop para buscar mediante una key q retorna su valor, sino existe retorna el default
es_estudiante = persona.pop("es_estudiante")
print(f"Es estudiante: {es_estudiante}")


#! sobreescribir un diccionario con otro diccionario
a = { "name": "miduev", "age": 25 }
b = { "name": "madeval", "es_estudiante": True }

a.update(b)
print(f"Diccionario A actualizado: {a}")


#! comprobar si existe una propiedad
print("name" in persona) # ---> False
print("nombre" in persona) # ---> True


#! obtener todas las claves
print("\nKeys de un diccionario")
print(persona.keys())

#! obtener todas los valores
print("\nValues de un diccionario")
print(persona.values())

#! obtener tanto clave como valor
print("\nObtener tanto clave como valor")
print(persona.items())

for key, value in persona.items():
    print(f"Key: {key}, valor: {value}")