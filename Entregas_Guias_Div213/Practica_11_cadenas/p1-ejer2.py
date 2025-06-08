# Ejercicio 2: Desarrollar una función que reciba una cadena y dos índices.  Se debe retornar la cadena que va entre las posiciones indicadas por los índices.  Si las posiciones no son válidas se debe informar.


def retornar_cadena_entre_indices(cadena:str, i1:int, i2:int)->str:
    devolver = ""

    if i2 < i1:
        devolver = "El segundo indice no puede ser menor que el primero"
    elif i2 - i1 == 1:
        devolver = "Debe haber al menos un numero entre medio de ambos indices"
    
    for i in range( len(cadena) ):
        if i > i1 and i < i2:
            devolver = devolver + cadena[i]
    
    return devolver

print(retornar_cadena_entre_indices('hola', 0, 3))