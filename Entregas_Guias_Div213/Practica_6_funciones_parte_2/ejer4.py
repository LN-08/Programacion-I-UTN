# Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.


# Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.

def es_par(numero:int) -> bool:
    if numero % 2 == 0:
        esPar = True
    else:
        esPar = False
    
    return esPar

if es_par:
    print("Es par")
else:
    print("Es impar")