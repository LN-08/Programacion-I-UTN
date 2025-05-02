"""
Ejercicio 9: Desarrollar las funciones del ejer 8 en una biblioteca.
"""
from ejer8 import *

def menu_de_opciones():

    opc = 0

    while opc != 1:
        print("Presione 1 para importar las listas como primer paso")
        opc = int(input("Opcion: "))

    print("Listas importadas correctamente")

    print("1 - Mostrar listas completas")
    print("2 - Listar los datos de los usuarios de México")
    print("3 - Listar los nombre, mail y teléfono de los usuarios de Brasil")
    print("4 - Listar los datos del/los usuario/s más joven/es ")
    print("5 - Obtener un promedio de edad de los usuarios")
    print("6 - De los usuarios de Brasil, listar los datos del usuario de mayor edad ")
    print("7 - Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000 ")
    print("8 - Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años.")
    print("9 - Listar los datos de los usuarios de México ordenados por nombre.")
    print("10 - Listar los datos del/los usuario/s más joven/es ordenados por edad de manera ascendente (Si la edad se repite, se ordenan por nombre de manera ascendente)")
    print("11 - Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000 ordenado por nombre y edad de manera descendente)")

    opc = int(input("Opcion: "))

    while opc < 1 or opc > 11:
        print("Numero incorrecto, vuelva a ingresar.")
        opc = int(input("Opcion: "))


    match opc:
        case 1:
            return listar_todos_los_datos()
        
        case 2:
            return listar_datos_de_mexicanos()

        case 3:
            return listar_usuarios_de_brasil()
        
        case 4:
            return listar_usuarios_mas_jovenes()

        case 5:
            return calcular_promedio_de_edad_de_usuarios() 
            # Lo dejo como un flotante para ver su proximidad con el siguiente nro.
        
        case 6:
            return listar_usuario_br_de_mayor_edad()

        case 7:
            return listar_users_de_mx_y_br_con_cod_postal_requerido()
        
        case 8:
            return listar_italianos_mayores_de_40_años()
        
        case 9:
            return listar_mexicanos_por_orden()
        
        case 10:
            return listar_usuarios_jovenes_ordenados()
        
        case 11:
            return mexicanos_y_brasileros_ordenados_por_nombres_y_mayores_a_8000_en_cod_postal()

print(menu_de_opciones())