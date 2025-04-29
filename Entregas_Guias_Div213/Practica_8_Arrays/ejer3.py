"""
Ejercicio 3: Desarrollar una función que pida 10 números dentro de un rango
especificado, validar los números solicitados dentro de ese rango, guardar en una
lista y retornarla. El programa principal debe invocar a la función y mostrar por
pantalla el retorno.
"""

def pedir_numeros()->list:

    lista_numeros = []

    rango_minimo = int(input("Rango minimo: "))
    rango_maximo = int(input("Rango maximo: "))


    while rango_minimo > rango_maximo:
        print("El rango minimo ingresado es mas grande que el maximo")
        rango_minimo = int(input("Rango minimo: "))
        rango_maximo = int(input("Rango maximo: "))

    print("--------------------------------------------------------------------------------------")
    print("Si algun numero ingresado no se encuentra dentro de este rango, se volvera a solicitar")
    print("--------------------------------------------------------------------------------------")

    for i in range(10):
        numero = rango_maximo + 1
        
        while numero < rango_minimo or numero > rango_maximo:
            numero = int(input(f"Numero {i+1}: "))
        
        if numero > rango_minimo or numero < rango_maximo:
            lista_numeros.append(numero)
        

    return(lista_numeros)

print(pedir_numeros())