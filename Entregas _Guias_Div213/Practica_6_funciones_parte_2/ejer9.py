# Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.


def imprimir_tabla_de_multiplicar(numero:int, inicio:int, fin:int) -> str:
    """
    # requiere: **fin no puede ser mas chico que **inicio** 
    # parametros: numero -> indica un numero, 
    #             inicio -> indica el inicio (parametro opcional)
    #             fin -> indica el final (parametro opcional)
    # retorna: la tabla de multiplicar del **inicio** al **fin** en caso de que se haya especificado.
                Si no se especifico, los primeros 10
    """

    # caso de que ingrese 0 en inicio y fin (parametros opcionales)
    if inicio == 0 and fin == 0:
        for i in range(10):
            print(f"{numero} * {i} = {numero * i}")
    else:
        for i in range(inicio, fin + 1):
            print(f"{numero} * {i} = {numero * i}")


print(imprimir_tabla_de_multiplicar(2,3,9))