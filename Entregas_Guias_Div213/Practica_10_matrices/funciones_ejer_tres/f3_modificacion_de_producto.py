def modificar_producto_de_matriz(matriz):
    fila = int(input("Fila del producto a modificar: "))
    columna = int(input("Columna del producto a modificar: "))

    while fila < 1 or columna < 1 or fila > len(matriz) or columna > len(matriz[0]):
        print("No existe ese índice")
        fila = int(input("Fila del producto a modificar: "))
        columna = int(input("Columna del producto a modificar: "))

    if matriz[fila - 1][columna - 1] != ['nada', 0]:
        cambiar_datos = input("¿Desea cambiar los datos del producto? (s/n): ")

        if cambiar_datos.lower() == 's':
            nuevo_nombre = input("Nuevo nombre: ")
            nueva_cantidad = int(input("Nueva cantidad: "))

            while nueva_cantidad < 1:
                print("La cantidad no puede ser 0 o menor.")
                nueva_cantidad = int(input("Nueva cantidad: "))

            matriz[fila - 1][columna - 1] = [nuevo_nombre, nueva_cantidad]

        cambiar_ubicacion = input("¿Desea mover el producto a otro índice? (s/n): ")

        if cambiar_ubicacion.lower() == 's':
            nueva_fila = int(input("Nuevo índice de fila: "))
            nueva_col = int(input("Nuevo índice de columna: "))

            producto = matriz[fila - 1][columna - 1]
            matriz[nueva_fila - 1][nueva_col - 1] = producto
            matriz[fila - 1][columna - 1] = ['nada', 0]

            print("Producto movido con éxito.")
    else:
        print("No existe un producto en ese índice.")

    return matriz
