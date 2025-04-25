# Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.

def es_par(numero: int):
    if numero % 2 == 0:
        print("Es par")
    else:
        print("Es impar")

es_par(3)