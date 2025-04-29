""" Ejercicio 1: Desarrollar una función que pida 10 nombres de manera secuencial, los guarde en una lista y la retorne. El programa principal debe invocar a la función y mostrar por pantalla el retorno.
"""

def pedir_nombre() -> list:
    lista_nombres = []

    for i in range(10):
        nombre = input(f"Nombre {i+1}: ")
        lista_nombres.append(nombre)
        # append() agrega en la proxima posicion libre el elemento pasado por parametro (al final de la lista)
    
    return lista_nombres

print(pedir_nombre())
