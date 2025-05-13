def cargar_matriz_secuencialmente(matriz:list):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            nombre = input(f"Producto para fila {i+1}, columna {j+1}: ")
            cantidad = int(input("Cantidad: "))
            matriz[i][j] = [nombre, cantidad]

    return matriz