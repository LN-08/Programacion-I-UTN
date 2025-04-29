"""
Ejercicio 2: Desarrollar una función que inicialice una lista de 10 números en 0, pida posición y número a guardar al usuario, lo guarde en una lista en la posición solicitada aleatoriamente y la retorne. El programa principal debe invocar a la función y mostrar por pantalla el retorno.
"""

def lista_con_inidice_modificado()->list:
    lista = [0] * 10

    posicion = int(input("Posicion (0-9): "))
    numero = int(input("Numero: "))

    if posicion < 0 and posicion > 9:
        print("Posicion incorrecta.")
    else:
        lista[posicion] = numero
    
    return lista

print(lista_con_inidice_modificado())

