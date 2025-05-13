from ejer5 import estanteria
from funciones_ejer_siete.ejecucion_dependiente import *

def menu_de_opciones(matriz):
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


            brekear = ejecutar_opcion_correspondiente(opc, matriz)

            if brekear:
                 break
        
            
menu_de_opciones(estanteria)