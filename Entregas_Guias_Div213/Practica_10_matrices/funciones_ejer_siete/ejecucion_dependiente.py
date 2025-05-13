from paquete_manejo_basico_matrices.mostrar_la_matriz import mostrar_matriz

def ejecutar_opcion_correspondiente(opc, matriz):
        
        terminar = False
        
        if opc == 1:
                fila_a_reponer = int(input("Fila a reponer (entre 1 y 4): "))
                columna_a_reponer = int(input("Columna a reponer (entre 1 y 4): "))

                while fila_a_reponer < 1 or fila_a_reponer > 4 or columna_a_reponer < 1 or columna_a_reponer > 4:
                        print("fila o columna invalidas. Vuelva a ingresar.")
                        fila_a_reponer = int(input("Fila a reponer (entre 1 y 4): "))
                        columna_a_reponer = int(input("Columna a reponer (entre 1 y 4): "))

                cantidad_a_reponer = int(input("Cantidad de unidades a reponer: "))

                while cantidad_a_reponer < 0:
                        print("No puede reponer menos de cero unidades")
                        cantidad_a_reponer = int(input("Cuantas unidades desea reponer: "))

                matriz[fila_a_reponer - 1][columna_a_reponer - 1][1] = matriz[fila_a_reponer - 1][columna_a_reponer - 1][1] + cantidad_a_reponer
                print("------------------------------------------------------------------------------")
                print(f"Unidades en total: {matriz[fila_a_reponer - 1][columna_a_reponer - 1][1]}")

                terminar = False

                

        elif opc == 2:
                fila_a_vender = int(input("Fila a vender (entre 1 y 4): "))
                columna_a_vender = int(input("Columna a vender (entre 1 y 4): "))

                while fila_a_vender < 1 or fila_a_vender > 4 or columna_a_vender < 1 or columna_a_vender > 4:
                        print("fila o columna invalidas. Vuelva a ingresar.")
                        fila_a_vender = int(input("Fila a vender (entre 1 y 4): "))
                        columna_a_vender = int(input("Columna a vender (entre 1 y 4): "))
                
                cantidad_a_vender = int(input("Cantidad de unidades a vender: "))

                while cantidad_a_vender > matriz[fila_a_vender - 1][columna_a_vender - 1][1]:
                        print("No puede vender mas unidades de las que tiene")
                        cantidad_a_vender = int(input("Cuantas unidades desea vender: "))
                
                matriz[fila_a_vender - 1][columna_a_vender - 1][1] = matriz[fila_a_vender - 1][columna_a_vender - 1][1] - cantidad_a_vender
                print("------------------------------------------------------------------------------")
                print(f"{cantidad_a_vender} unidades vendidas con exito!")
                print(f"Unidades en total: {matriz[fila_a_vender - 1][columna_a_vender - 1][1]}")

                terminar = False



        elif opc == 3:
            mostrar_matriz(matriz)
            terminar = False



        else:
            print("Hasta luego!")
            terminar = True
        


        return terminar
