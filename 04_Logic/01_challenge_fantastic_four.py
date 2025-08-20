"""
¿Está en Equilibrio la Alianza entre Reed Richards y Johnny Storm?

En el universo de los 4 Fantásticos, la unión y el equilibrio entre
los poderes es fundamental para enfrentar cualquier desafío.
En este problema, nos centraremos en dos de sus miembros:

Reed Richards (Mr. Fantastic), representado por la letra R.
Johnny Storm (La Antorcha Humana), representado por la letra J.

Objetivo:

Crea una función en Python que reciba una cadena de texto. 
Esta función debe contar cuántas veces aparece la letra R (para Reed Richards)
y cuántas veces aparece la letra J (para Johnny Storm) en la cadena.

- Si la cantidad de R y la cantidad de J son iguales, 
se considera que la alianza entre la mente y 
el fuego está en equilibrio y la función debe retornar True.

- Si las cantidades no son iguales, la función debe retornar False.
- En el caso de que no aparezca ninguna de las dos letras en la cadena,
se entiende que el equilibrio se mantiene (0 = 0), por lo que la función debe retornar True.
"""

Reed_Richards = "r"
Johnny_Storm = "j"

cadena_ejemplo = "JjjjRrr"
# print(sorted(cadena_ejemplo.lower())) #?--> devuelve la cadena de texto en array y minusculas.

def equilibrio(text : str):
    count_r = 0
    count_j = 0
    array_text = sorted(text.lower())
    print(array_text)

    for letter in array_text:
        if letter == Reed_Richards:
            count_r += 1
        elif letter == Johnny_Storm:
            count_j += 1
        
    print(f"count R: {count_r} y count J: {count_j}")
    
    if count_j == count_r:
        return True
    else:
        return False

equilibrio(cadena_ejemplo)