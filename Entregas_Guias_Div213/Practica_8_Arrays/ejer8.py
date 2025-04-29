"""
8. Crear una función para cada opción de menú del ejercicio 7.
"""

# 1-Importar listas 
from listas_personas import *



def listar_todos_los_datos()->list:
    return [nombres, telefonos, mails, address, postalZip, region, country, edades]



def listar_datos_de_mexicanos()->list:
    # 2 - Listar los datos de los usuarios de México 
    datos_usuarios_mexico = []

    for i in range(len(country)):
        if country[i] == 'Mexico':
            datos_usuarios_mexico.append([nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i]])
    
    return datos_usuarios_mexico



def listar_usuarios_de_brasil()->list:
    # 3 - Listar los nombre, mail y teléfono de los usuarios de Brasil 
    datos_usuarios_brasil = []

    for i in range(len(country)):
        if country[i] == 'Brazil':
            datos_usuarios_brasil.append([nombres[i], mails[i], telefonos[i]])

    return datos_usuarios_brasil



def listar_usuarios_mas_jovenes()->list:
    # 4 - Listar los datos del/los usuario/s más joven/es 
    datos_usuarios_mas_jovenes = []
    menor_por_ahora = edades[0]

    for i in range(len(edades)):
        if edades[i] <= menor_por_ahora:
            datos_usuarios_mas_jovenes.append([nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i]])
    
    return datos_usuarios_mas_jovenes



def calcular_promedio_de_edad_de_usuarios()->list:
    # 5 - Obtener un promedio de edad de los usuarios   
    suma_de_edades = 0

    for i in range(len(edades)):
        suma_de_edades += edades[i]

    promedio_de_edades = suma_de_edades / len(edades)

    return promedio_de_edades



def listar_usuario_br_de_mayor_edad()->list:
    # 6 - De los usuarios de Brasil, listar los datos del usuario de mayor edad 
    datos_del_brasilero_de_mayor_edad = []

    indice_del_primer_brasilero = 0 # Voy al primer user, no tiene que ser BRA necesariamente

    while country[indice_del_primer_brasilero] != 'Brazil':
        indice_del_primer_brasilero += 1
    
    edad_mayor_de_un_br_por_ahora = edades[indice_del_primer_brasilero]

    for i in range(len(edades)):
        if country[i] == 'Brazil' and edades[i] >= edad_mayor_de_un_br_por_ahora:
            indice_del_brasilero_mayor = i
            edad_mayor_de_un_br_por_ahora = edades[i] # guardo la posicion, la cual sirve con cualquier lista
            

    datos_del_brasilero_de_mayor_edad = [[nombres[indice_del_brasilero_mayor], telefonos[indice_del_brasilero_mayor], mails[indice_del_brasilero_mayor], address[indice_del_brasilero_mayor], postalZip[indice_del_brasilero_mayor], region[indice_del_brasilero_mayor], country[indice_del_brasilero_mayor], edades[indice_del_brasilero_mayor]]]

    return datos_del_brasilero_de_mayor_edad



def listar_users_de_mx_y_br_con_cod_postal_requerido()->list:
    # 7 - Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000
    datos_de_mx_y_br_solicitados = []

    for i in range(len(postalZip)):
        if postalZip[i] > 8000 and (country[i] == 'Brazil' or country[i] == 'Mexico'):
            datos_de_mx_y_br_solicitados.append([nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i]])
    
    return datos_de_mx_y_br_solicitados



def listar_italianos_mayores_de_40_años()->list:
    # 8 - Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años. 
    datos_de_italianos_requeridos = []

    for i in range(len(country)):
        if country[i] == 'Italy' and edades[i] > 40:
            datos_de_italianos_requeridos.append([nombres[i], telefonos[i], mails[i]])
    
    return datos_de_italianos_requeridos



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

    opc = int(input("Opcion: "))

    while opc < 1 or opc > 8:
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


print(menu_de_opciones())