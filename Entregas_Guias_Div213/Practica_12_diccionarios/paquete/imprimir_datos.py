def imprimir_datos(lista:list, lista_de_diccionarios: list):
    for i in range(len(lista_de_diccionarios)):
        for dato in range(len(lista)):
            print(lista[dato], ": ", lista_de_diccionarios[i][lista[dato]])
        
        print(" ")