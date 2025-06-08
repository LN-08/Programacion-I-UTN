# Desarrollar una función que reciba una letra y una cadena. Debe retornar las veces que la letra está incluida en el texto.


def retornar_cantidad_existente(letra:str, cadena:str)->int:
    contador = 0

    if len(letra) > 1:
        print("No ingreso una letra, ingreso una cadena de caracteres. Por lo tanto, aparece: ")
        


    for i in range( len(cadena) ):
        if cadena[i] == letra:
            contador += 1

    return contador


print(retornar_cantidad_existente('aa', 'dinosaurio'))