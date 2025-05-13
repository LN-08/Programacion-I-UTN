from paquete_manejo_basico_matrices.mostrar_la_matriz import mostrar_matriz
from funciones_ejer_tres.f0_matriz_cargada import cargar_matriz
from funciones_ejer_tres.f1_producto_de_alta import dar_producto_de_alta
from funciones_ejer_tres.f2_baja_de_producto import dar_producto_de_baja
from funciones_ejer_tres.f3_modificacion_de_producto import modificar_producto_de_matriz
from funciones_ejer_tres.f5_ordenamiento_de_matriz import ordenar_matriz


def menu_de_opciones(matriz_cargada):
    opc = 0
    seguir_en_menu = 's'

    while opc != 6 and (seguir_en_menu == 's' or seguir_en_menu == 'S'):
        print("----------------- MENU -----------------")
        print("1 - Alta de producto")
        print("2 - Baja de producto")
        print("3 - Modificar producto")
        print("4 - Listar productos")
        print("5 - Lista de productos ordenados por nombre")
        print("6 - Salir")
        print("-----------------------------------------")
        opc = int(input("Opcion: "))

        while opc < 1 or opc > 6:
            print("Numero incorrecto, vuelva a ingresar.")
            opc = int(input("Opcion: "))

        # 1 - Dar de alta
        if opc == 1:
            matriz_cargada = dar_producto_de_alta(matriz_cargada)

        # 2 - Dar de baja
        if opc == 2:
            matriz_cargada = dar_producto_de_baja(matriz_cargada)

        # 3 - Modificar
        if opc == 3:
            matriz_cargada = modificar_producto_de_matriz(matriz_cargada)

        # 4 - Listar productos
        if opc == 4:
            mostrar_matriz(matriz_cargada)

        # 5 - Ordenar productos
        if opc == 5:
            mostrar_matriz( ordenar_matriz(matriz_cargada) )

        if opc == 6:
            print("Hasta luego!")
            break

        print("-----------------------------------------")
        seguir_en_menu = input("¿Desea seguir en el menú? (s/n): ")

    return matriz_cargada


matriz_cargada = cargar_matriz() # Introducir cantidad de filas y columnas antes de ir al menu
matriz_cargada = menu_de_opciones(matriz_cargada)
