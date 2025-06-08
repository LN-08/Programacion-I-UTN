"""
Ejercicio 3: Desarrollar una función “char_at” que recibe una cadena y un número.   
Se debe retornar el caracter en la posición indicada por el número si ésta es válida.   
**IMPORTANTE: **Las posiciones de los caracteres en un string van del 0 hasta el 
<número de caracteres> - 1. 
"""

def char_at(cadena:str, numero:int)->any:
    if len(cadena) < numero:
        devolver = "Nro Invalido"

    for i in range(len(cadena)):
        if i == numero:
            devolver = cadena[i]

    return devolver

print(char_at("hola", 0))