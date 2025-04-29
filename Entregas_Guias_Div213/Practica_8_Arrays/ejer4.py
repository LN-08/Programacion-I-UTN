"""
Ejercicio 4: Desarrollar una función que reciba por parámetro, una lista de números
y un número especificado. La misma debe buscar el número especificado en la lista
y retornar “True” si existe.
"""

def buscar_numero_en_lista(listaDeNumeros, numero)->bool:
    return numero in listaDeNumeros