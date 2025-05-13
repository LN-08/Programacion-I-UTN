"""
Armar el siguiente menú de opciones
1-Alta de productos (producto nuevo) 
2-Baja de productos (producto existente) 
3-Modificar productos (cantidad, ubicación) 
4-Listar productos 
5-Lista de productos ordenado por nombre 
6-Salir 

"""

from paquete_manejo_basico_matrices.inicializar_la_matriz import inicializar_matriz
from paquete_manejo_basico_matrices.cargar_por_indice import cargar_matriz_automaticamente
from paquete_manejo_basico_matrices.mostrar_la_matriz import mostrar_matriz
from paquete_manejo_basico_matrices.cargar_secuencialmente import cargar_matriz_secuencialmente

filas = int(input("Cantidad de filas: "))
columnas = int (input("Cantidad de columnas: "))

matriz_de_productos_inicializada = inicializar_matriz(filas, columnas, ["nada", 0]) 


# REEMPLAZAR POR GONDOLAS DEL EJER
matriz_cargada = cargar_matriz_secuencialmente(matriz_de_productos_inicializada)



def menu_de_opciones():
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

        

        # 1 - Dar de alta un producto
        if opc == 1:
            matriz_de_productos_actualizada = cargar_matriz_automaticamente(matriz_cargada)
            mostrar_matriz(matriz_de_productos_actualizada)



        # 2 - Baja de producto (Debe existir)
        elif opc == 2:
            fila_de_producto_a_borrar = int(input("Fila del producto a dar de baja: "))
            columna_de_producto_a_borrar = int(input("Columna del producto a dar de baja: "))

            while fila_de_producto_a_borrar < 1 or columna_de_producto_a_borrar < 1 or fila_de_producto_a_borrar > len(matriz_cargada) or columna_de_producto_a_borrar > len(matriz_cargada[0]):
                print("-----------------------------------------")
                print("No existe ese indice")
                fila_de_producto_a_borrar = int(input("Fila del producto a dar de baja: "))
                columna_de_producto_a_borrar = int(input("Columna del producto a dar de baja: "))

            while matriz_cargada[fila_de_producto_a_borrar - 1][columna_de_producto_a_borrar - 1] == ['nada', 0]:
                print("No existe un producto en ese indice")
                fila_de_producto_a_borrar = int(input("Fila del producto a dar de baja: "))
                columna_de_producto_a_borrar = int(input("Columna del producto a dar de baja: "))  


            matriz_cargada[fila_de_producto_a_borrar-1][columna_de_producto_a_borrar-1] = ['nada', 0]
            mostrar_matriz(matriz_cargada)



        # 3 - Modificar productos (cantidad, ubicación)
        elif opc == 3:
            fila_producto_a_modificar = int(input("Fila del producto a modificar: "))
            columna_producto_a_modificiar = int(input("Columna del producto a modificar: "))

            while fila_producto_a_modificar < 1 or columna_producto_a_modificiar < 1 or fila_producto_a_modificar > len(matriz_cargada) or columna_producto_a_modificiar > len(matriz_cargada[0]):
                print("-----------------------------------------")
                print("No existe ese indice")
                fila_producto_a_modificar = int(input("Fila del producto a modificar: "))
                columna_producto_a_modificiar= int(input("Columna del producto a modificar: "))



            if matriz_cargada[fila_producto_a_modificar-1][columna_producto_a_modificiar-1] != ['nada', 0]:

                cambiar_datos_del_producto = input("Desea cambiar los datos del producto? s/n: ")

                if cambiar_datos_del_producto == 's' or cambiar_datos_del_producto == 'S':
                    nombre_modificado = input("Nuevo nombre: ")
                    cantidad_modificada = int(input("Nueva cantidad: "))

                    while cantidad_modificada < 1:
                        print("La cantidad no puede ser 0 o menos")
                        cantidad_modificada = int(input("Nueva cantidad: "))

                    matriz_cargada[fila_producto_a_modificar - 1][columna_producto_a_modificiar - 1] = [nombre_modificado, cantidad_modificada]



                print("Desea mover el producto a otro indice? (pisara el valor existente en caso de que exista uno)")
                cambiar_ubicacion = input("s/n: ")

                if cambiar_ubicacion == 's' or cambiar_ubicacion == 'S':
                    indice_nuevo_fila = int(input("Nuevo indice de fila: "))
                    indice_nuevo_columna = int(input("Nuevo indice de columna: "))


                    # cargo el producto en la nueva ubicacion
                    producto_a_mover = matriz_cargada[fila_producto_a_modificar - 1][columna_producto_a_modificiar - 1]

                    matriz_cargada[indice_nuevo_fila - 1][indice_nuevo_columna - 1] = producto_a_mover

                    # borro el producto de la ubicacion vieja
                    matriz_cargada[fila_producto_a_modificar - 1][columna_producto_a_modificiar - 1] = ['nada', 0]

                    print("-----------------------------------------")
                    print("Elemento modificado con exito!")


            else:
                 print("No existe un producto en esos indices, no puede modificarse")
            
            mostrar_matriz(matriz_cargada)
            

    
        # 4 - Mostrar matriz
        elif opc == 4:
                mostrar_matriz(matriz_cargada)



        # 5 - Lista de productos ordenado por nombre
        elif opc == 5:
            matriz_sin_elementos_vacios = []

            for i in range(len(matriz_cargada)):
                 for j in range(len(matriz_cargada[i])):
                      if matriz_cargada[i][j] != ['nada', 0]:
                           matriz_sin_elementos_vacios.append(matriz_cargada[i][j])
    


            for i in range(len(matriz_sin_elementos_vacios)-1): 

                for j in range(i+1, len(matriz_sin_elementos_vacios)):

                    if matriz_sin_elementos_vacios[i][0] > matriz_sin_elementos_vacios[j][0]: 
                        # si el primer nombre i deberia ir despues del nombre j 
                        # ejemplo: Sofia deberia ir despues de Maria


                        # ordenamiento en nombres
                        nombre_que_va_despues = matriz_sin_elementos_vacios[i][0]
                        # guardo en una varibale el nombre que deberia ir mas al final entre los que comparo, 
                        # ya que en el siguiente paso voy a pisar el dato. 
                        # EJ: Guardo sofia en la variable

                        matriz_sin_elementos_vacios[i][0] = matriz_sin_elementos_vacios[j][0] 
                        # pongo en la posicion que era del nombre mas grande, el nombre que deberia ir antes
                        # EJ: pongo Maria en la posicion donde estaba Sofia, tapando el dato previo de sofia

                        matriz_sin_elementos_vacios[j][0] = nombre_que_va_despues
                        # en la posicion J, donde estaba el nombre que deberia ir antes, guardo el nombre que
                        # debe ir aca, el cual guarde en la variable nombre_que_va_despues
                        # EJ: pongo el nombre Sofia, guardado previamente en la variable, en la posicion posterior


                        # Misma logica de arriba, pero con las cantidades
                        cantidad_que_va_despues = matriz_sin_elementos_vacios[i][1]
                        matriz_sin_elementos_vacios[i][1] = matriz_sin_elementos_vacios[j][1]
                        matriz_sin_elementos_vacios[j][1] = cantidad_que_va_despues
            
            mostrar_matriz(matriz_sin_elementos_vacios)



        else:
            return "Hasta luego!"


        print("-----------------------------------------")
        seguir_en_menu = input("Desea seguir en menu? s/n: ")

        if seguir_en_menu == 'n' or seguir_en_menu == 'N':
            print("Hasta luego!")
        

menu_de_opciones()
    