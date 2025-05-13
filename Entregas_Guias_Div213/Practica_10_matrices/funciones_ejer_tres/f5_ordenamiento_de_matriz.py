def ordenar_matriz(matriz):       
    matriz_ordenada = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != ['nada', 0]:
                matriz_ordenada.append(matriz[i][j])

    for i in range(len(matriz_ordenada) - 1):
        for j in range(i + 1, len(matriz_ordenada)):
            if matriz_ordenada[i][0] > matriz_ordenada[j][0]:
                matriz_ordenada[i], matriz_ordenada[j] = matriz_ordenada[j], matriz_ordenada[i]

    return matriz_ordenada