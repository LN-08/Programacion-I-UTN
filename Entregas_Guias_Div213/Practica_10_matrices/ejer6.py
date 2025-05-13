from ejer5 import estanteria
from paquete_manejo_basico_matrices.mostrar_la_matriz import mostrar_matriz

def menu_de_opciones():
    opc = 0
    seguir_en_menu = 's'

    while opc != 6 and (seguir_en_menu == 's' or seguir_en_menu == 'S'):
        print("----------------- MENU -----------------")
        print("1 - Reponer mercaderia")
        print("2 - Vender mercaderia")
        print("3 - Listar inventario")
        print("4 - Salir")

        print("-----------------------------------------")
        opc = int(input("Opcion: "))

        while opc < 1 or opc > 4:
            print("Numero incorrecto, vuelva a ingresar.")
            opc = int(input("Opcion: "))
    


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


                
                estanteria[fila_a_reponer - 1][columna_a_reponer - 1][1] = estanteria[fila_a_reponer - 1][columna_a_reponer - 1][1] + cantidad_a_reponer
                print(f"Unidades en total: {estanteria[fila_a_reponer - 1][columna_a_reponer - 1][1]}")



        elif opc == 2:
                fila_a_vender = int(input("Fila a vender (entre 1 y 4): "))
                columna_a_vender = int(input("Columna a vender (entre 1 y 4): "))

                while fila_a_vender < 1 or fila_a_vender > 4 or columna_a_vender < 1 or columna_a_vender > 4:
                        print("fila o columna invalidas. Vuelva a ingresar.")
                        fila_a_vender = int(input("Fila a vender (entre 1 y 4): "))
                        columna_a_vender = int(input("Columna a vender (entre 1 y 4): "))
                


                cantidad_a_vender = int(input("Cantidad de unidades a vender: "))

                while cantidad_a_vender > estanteria[fila_a_vender - 1][columna_a_vender - 1][1]:
                        print("No puede vender mas unidades de las que tiene")
                        cantidad_a_vender = int(input("Cuantas unidades desea vender: "))
                

                estanteria[fila_a_vender - 1][columna_a_vender - 1][1] = estanteria[fila_a_vender - 1][columna_a_vender - 1][1] - cantidad_a_vender
                print(f"{cantidad_a_vender} unidades vendidas con exito!")
                print(f"Unidades en total: {estanteria[fila_a_vender - 1][columna_a_vender - 1][1]}")
        


        elif opc == 3:
               mostrar_matriz(estanteria)



        else:
               print("Hasta luego!")
               break
            


menu_de_opciones()
