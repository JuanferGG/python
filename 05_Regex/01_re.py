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

