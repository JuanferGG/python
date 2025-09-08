##
# 01 - Expresiones regulares
# 

""" Las expresiones regulares son una secuencia de caracteres que forman un patrón de búsqueda.
    Se utilizan para la búsqueda de cadenas de texto, validación de datos, etc. """


""" ¿Por qué aprender Regex?

- Búsqueda avanzada: Encontrar patrones específicos en textos grandes de forma rápida y precisa. (un editor de Markdown sólo usando Regex)

- Validación de datos: Asegurarte que los datos que ingresa un usuario como el email, teléfono, etc. son correctos.

- Manipulación del texto: Extraer, reemplazar y modificar partes de la cadena de texto fácilmente
"""

from os import system
if system("clear") != 0: system("cls")

#! 1. Importar el módulo de expresiones regulares "re"
import re
#? 2. Crear un patrón, que es una cadena de texto que describe lo que queremos encontrar
pattern = "Hola"
#? 3. El texto donde queremos buscar
text = "Hola mundo"
#? 4. Usar la función de búsqueda de "re"
result = re.search(pattern, text)

if result:
    print(f"El resultado es: {result}")
else:
    print("No he encontrado patron en el texto")


#! .group() devuelve la cadena que coincide con el pattern
print(result.group())

#! .start() devolver la posición inicial de la coincidencia
print(result.start())

#! .end() devolver la posición final de la coincidencia
print(result.end())



#? EJERCICIO 01
#? Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
#? e indica en que posición empieza y termina la coincidencia.
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"
pattern = "IA"
found_word = re.search(pattern, text)

if found_word:
    print(f"la palabra encontrada empieza en la posicion {found_word.start()} y termina en la posicion {found_word.end()}")
else:
    print("Palabra no encontrada")


###! Encontrar todas las coincidencias de un patrón
#! .findall() devuelve una lista con todas las coincidencias

text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Python"

matches = re.findall(pattern, text)
print(f"La cantidad de veces que se repite Python son: {len(matches)}")

#! -------------------------

#! iter() devuelve un iterador que contiene todos los resultados de la búsqueda

text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Python"

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(), match.start(), match.end())


#? EJERCICIO 02
#? Encuentra todas las ocurrencias de la palabra "midu" 
#? en el siguiente texto e indica en que posición empieza 
#? y termina cada coincidencia y cuantas veces se encontró.
text = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"

pattern = "midu"

matches = list(re.finditer(pattern, text))

for match in matches:
    print(f"inicio: {match.start()} y termina en {match.end()}")

print(f"Veces contado la palabra 'midu': {len(matches)} veces.")


###! Modificadores

#! Los modificadores son opciones que se pueden agregar a un patrón para cambiar su comportamiento
#! re.IGNORECASE: Ignora las mayúsculas y minúsculas

text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no es tan mala. ¡Viva la Ia!"
pattern = "IA"

found = re.findall(pattern, text, re.IGNORECASE) #? aqui ignora las mayusculas y minusculas

if found: print(found)
# else: print("Found no encontrado!")

#? EJERCICIO 03
#? Encuentra todas las ocurrencias de la palabra "python" 
#? en el siguiente texto, sin distinguir entre mayúsculas y minúsculas.
text = "Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON"
pattern = "python"

found = re.findall(pattern, text, re.IGNORECASE)

print(f"En el texto hay {len(found)} veces la palabra 'python'")


###! Reemplazar el texto
#! .sub() reemplaza todas las coincidencias de un patrón en un texto

text = "Hola, mundo! Hola de nuevo. Hola otra vez."
pattern = "hola"
replacement = "adiós"

new_text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

print(f"Text nuevo: {new_text}")