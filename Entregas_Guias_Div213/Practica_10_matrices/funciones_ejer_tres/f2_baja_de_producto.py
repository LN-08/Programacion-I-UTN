def dar_producto_de_baja(matriz):
    fila = int(input("Fila del producto a dar de baja: "))
    columna = int(input("Columna del producto a dar de baja: "))

    while fila < 1 or columna < 1 or fila > len(matriz) or columna > len(matriz[0]):
        print("No existe ese índice")
        fila = int(input("Fila del producto a dar de baja: "))
        columna = int(input("Columna del producto a dar de baja: "))
      
    while matriz[fila - 1][columna - 1] == ['nada', 0]:
        print("No existe un producto en ese índice")
        fila = int(input("Fila del producto a dar de baja: "))
        columna = int(input("Columna del producto a dar de baja: "))

    matriz[fila - 1][columna - 1] = ['nada', 0]

    return(matriz)