def cargar_matriz_automaticamente(matriz:list):

    seguir = "S"
    while seguir == "S" or seguir == 's':
        fila = int(input("Indice de fila: "))
        columna = int(input("Indice de columna: "))
        nombre = input("Nombre a cargar: ")
        cantidad = int(input("Cantidad a cargar: "))

        while cantidad == 0:
            print("La cantidad no puede ser 0")
            cantidad = int(input("Cantidad a cargar: "))

        if matriz[fila-1][columna-1] != ["nada", 0]:
            print("Ya existe un producto en este , seleccione otro")

        matriz[fila-1][columna-1] = [nombre, cantidad]
        
        seguir = input("Desea seguir cargando? S/N: ")

    return matriz
