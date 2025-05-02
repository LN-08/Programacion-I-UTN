"""
9-Listar los datos de los usuarios de México ordenados por nombre 

10-Listar los datos del/los usuario/s más joven/es ordenados por edad de manera ascendente (Si la edad se repite, ordenar por nombre de manera ascendente) 

11-Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000 ordenado por nombre y edad de manera descendente 
"""


from listas_personas import *
from ejer1 import *

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



    # 2 - Listar los datos de los usuarios de México 
    datos_usuarios_mexico = []

    for i in range(len(country)):
        if country[i] == 'Mexico':
            datos_usuarios_mexico += [[nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i]]]

    

    # 3 - Listar los nombre, mail y teléfono de los usuarios de Brasil 
    datos_usuarios_brasil = []

    for i in range(len(country)):
        if country[i] == 'Brazil':
            datos_usuarios_brasil += [[nombres[i], mails[i], telefonos[i]]]

    

    # 4 - Listar los datos del/los usuario/s más joven/es 
    datos_usuarios_mas_jovenes = []
    menor_por_ahora = edades[0]

    for i in range(len(edades)):
        if edades[i] <= menor_por_ahora:
            datos_usuarios_mas_jovenes += [[nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i]]]



    # 5 - Obtener un promedio de edad de los usuarios   
    suma_de_edades = 0

    for i in range(len(edades)):
        suma_de_edades += edades[i]

    promedio_de_edades = suma_de_edades / len(edades)



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



    # 7 - Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000
    datos_de_mx_y_br_solicitados = []

    for i in range(len(postalZip)):
        if postalZip[i] > 8000 and (country[i] == 'Brazil' or country[i] == 'Mexico'):
            datos_de_mx_y_br_solicitados += [[nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i]]]



    # 8 - Listar nombre, mail y teléfono de los usuarios italianos mayores a 40 años. 
    datos_de_italianos_requeridos = []

    for i in range(len(country)):
        if country[i] == 'Italy' and edades[i] > 40:
            datos_de_italianos_requeridos += [[nombres[i], telefonos[i], mails[i]]]
    
    

    # ---------------------------- PRACTICA ORDENAMIENTO

    # 9 - Listar los datos de los usuarios de México ordenados por nombre 
    # estrategia, ordenar todos los elementos, y luego si no es de mexico, no lo agrega a una nueva lista

    # creo listas nuevas para ordenar las originales, sin pisarlas
    usuarios = nombres

    nombresOrdenadosPorNombres = nombres
    telefonosOrdenadosPorNombres = telefonos
    mailsOrdenadosPorNombres = mails
    addressOrdenadosPorNombres = address
    postalOrdenadosPorNombres = postalZip
    regionOrdenadosPorNombres = region
    countryOrdenadosPorNombres = country
    edadesOrdenadosPorNombres = edades

    for i in range(len(usuarios)-1):
         for j in range(i+1, len(usuarios)):
    
            if nombresOrdenadosPorNombres[i] > nombresOrdenadosPorNombres[j]:
    
                # ORDENAMIENTO EN NOMBRES
                nombre_que_va_despues = nombresOrdenadosPorNombres[i] 
                nombresOrdenadosPorNombres[i] = nombresOrdenadosPorNombres[j]
                nombresOrdenadosPorNombres[j] = nombre_que_va_despues

                # ORDENAMIENTO EN TELEFONOS
                telefono_que_va_despues = telefonosOrdenadosPorNombres[i]
                telefonosOrdenadosPorNombres[i] = telefonosOrdenadosPorNombres[j]
                telefonosOrdenadosPorNombres[j] = telefono_que_va_despues

                # ORDENAMIENTO EN MAILS
                mail_que_va_despues = mailsOrdenadosPorNombres[i]
                mailsOrdenadosPorNombres[i] = mailsOrdenadosPorNombres[j]
                mailsOrdenadosPorNombres[j] = mail_que_va_despues

                # ORDENAMIENTO EN ADDRESS
                address_que_va_despues = addressOrdenadosPorNombres[i]
                addressOrdenadosPorNombres[i] = addressOrdenadosPorNombres[j]
                addressOrdenadosPorNombres[j] = address_que_va_despues

                # ORDENAMIENTO EN POSTAL ZIP
                postal_que_va_despues = postalOrdenadosPorNombres[i]
                postalOrdenadosPorNombres[i] = postalOrdenadosPorNombres[j]
                postalOrdenadosPorNombres[j] = postal_que_va_despues

                # ORDENAMIENTO EN REGION
                region_que_va_despues = regionOrdenadosPorNombres[i]
                regionOrdenadosPorNombres[i] = regionOrdenadosPorNombres[j]
                regionOrdenadosPorNombres[j] = region_que_va_despues

                # ORDENAMIENTO EN COUNTRY
                pais_que_va_despues = countryOrdenadosPorNombres[i]
                countryOrdenadosPorNombres[i] = countryOrdenadosPorNombres[j]
                countryOrdenadosPorNombres[j] = pais_que_va_despues

                # ORDENAMIENTO EN EDADES
                edad_que_va_despues = edadesOrdenadosPorNombres[i]
                edadesOrdenadosPorNombres[i] = edadesOrdenadosPorNombres[j]
                edadesOrdenadosPorNombres[j] = edad_que_va_despues

    mexicanos_filtrados_en_orden_por_nombre = []

    for i in range(len(countryOrdenadosPorNombres)):
        if countryOrdenadosPorNombres[i] == 'Mexico':
            mexicanos_filtrados_en_orden_por_nombre += [[nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i]]]



    # 10 - Listar los datos del/los usuario/s más joven/es ordenados por edad de manera ascendente (Si la edad se repite, ordenar por nombre de manera ascendente) 

    # estrategia, ordenar todos los elementos, y luego si no tiene la edad minima, no se agrega a una nueva lista. Los elementos ya se encuentran ordenados POR NOMBRES, por el punto 9, entonces solo debo filtrar aquellos que tengan la misma edad del primer indice

    

    nombresOrdenadosPorEdades = nombres
    telefonosOrdenadosPorEdades = telefonos
    mailsOrdenadosPorEdades = mails
    addressOrdenadosPorEdades = address
    postalOrdenadosPorEdades = postalZip
    regionOrdenadosPorEdades = region
    countryOrdenadosPorEdades = country
    edadesOrdenadosPorEdades = edades

    for i in range(len(usuarios)-1):
         for j in range(i+1, len(usuarios)):
    
            if edadesOrdenadosPorEdades[i] > edadesOrdenadosPorEdades[j]:
    
                # ORDENAMIENTO EN NOMBRES
                nombre_que_va_despues = nombresOrdenadosPorEdades[i] 
                nombresOrdenadosPorEdades[i] = nombresOrdenadosPorEdades[j]
                nombresOrdenadosPorEdades[j] = nombre_que_va_despues

                # ORDENAMIENTO EN TELEFONOS
                telefono_que_va_despues = telefonosOrdenadosPorEdades[i]
                telefonosOrdenadosPorEdades[i] = telefonosOrdenadosPorEdades[j]
                telefonosOrdenadosPorEdades[j] = telefono_que_va_despues

                # ORDENAMIENTO EN MAILS
                mail_que_va_despues = mailsOrdenadosPorEdades[i]
                mailsOrdenadosPorEdades[i] = mailsOrdenadosPorEdades[j]
                mailsOrdenadosPorEdades[j] = mail_que_va_despues

                # ORDENAMIENTO EN ADDRESS
                address_que_va_despues = addressOrdenadosPorEdades[i]
                addressOrdenadosPorEdades[i] = addressOrdenadosPorEdades[j]
                addressOrdenadosPorEdades[j] = address_que_va_despues

                # ORDENAMIENTO EN POSTAL ZIP
                postal_que_va_despues = postalOrdenadosPorEdades[i]
                postalOrdenadosPorEdades[i] = postalOrdenadosPorEdades[j]
                postalOrdenadosPorEdades[j] = postal_que_va_despues

                # ORDENAMIENTO EN REGION
                region_que_va_despues = regionOrdenadosPorEdades[i]
                regionOrdenadosPorEdades[i] = regionOrdenadosPorEdades[j]
                regionOrdenadosPorEdades[j] = region_que_va_despues

                # ORDENAMIENTO EN COUNTRY
                pais_que_va_despues = countryOrdenadosPorEdades[i]
                countryOrdenadosPorEdades[i] = countryOrdenadosPorEdades[j]
                countryOrdenadosPorEdades[j] = pais_que_va_despues

                # ORDENAMIENTO EN EDADES
                edad_que_va_despues = edadesOrdenadosPorEdades[i]
                edadesOrdenadosPorEdades[i] = edadesOrdenadosPorEdades[j]
                edadesOrdenadosPorEdades[j] = edad_que_va_despues
    
    usuarios_con_la_edad_menor = []

    for i in range(len(usuarios)):
        if edadesOrdenadosPorEdades[i] == edadesOrdenadosPorEdades[0]:
            usuarios_con_la_edad_menor += [[nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i]]]



    # 11 - Listar los datos de los usuarios de México y Brasil cuyo código postal sea mayor a 8000 ordenado por nombre y edad de manera descendente 

    nombresOrdenadosPorCodPostal = nombres
    telefonosOrdenadosPorCodPostal = telefonos
    mailsOrdenadosPorCodPostal = mails
    addressOrdenadosPorCodPostal = address
    postalOrdenadosPorCodPostal = postalZip
    regionOrdenadosPorCodPostal = region
    countryOrdenadosPorCodPostal = country
    edadesOrdenadosPorCodPostal = edades

    for i in range(len(usuarios)-1):
         for j in range(i+1, len(usuarios)):
    
            if (nombresOrdenadosPorCodPostal[i] < nombresOrdenadosPorCodPostal[j]) or (nombresOrdenadosPorCodPostal[i] == nombresOrdenadosPorCodPostal[j] and edadesOrdenadosPorCodPostal[i] < edadesOrdenadosPorCodPostal[j]):
            # si el nombre de i es mas chico que el de J
            # O
            # el nombre de i y j son iguales, pero la edad de i es menor a la de j


                # ORDENAMIENTO EN NOMBRES
                nombre_que_va_despues = nombresOrdenadosPorCodPostal[i] 
                nombresOrdenadosPorCodPostal[i] = nombresOrdenadosPorCodPostal[j]
                nombresOrdenadosPorCodPostal[j] = nombre_que_va_despues

                # ORDENAMIENTO EN TELEFONOS
                telefono_que_va_despues = telefonosOrdenadosPorCodPostal[i]
                telefonosOrdenadosPorCodPostal[i] = telefonosOrdenadosPorCodPostal[j]
                telefonosOrdenadosPorCodPostal[j] = telefono_que_va_despues

                # ORDENAMIENTO EN MAILS
                mail_que_va_despues = mailsOrdenadosPorCodPostal[i]
                mailsOrdenadosPorCodPostal[i] = mailsOrdenadosPorCodPostal[j]
                mailsOrdenadosPorCodPostal[j] = mail_que_va_despues

                # ORDENAMIENTO EN ADDRESS
                address_que_va_despues = addressOrdenadosPorCodPostal[i]
                addressOrdenadosPorCodPostal[i] = addressOrdenadosPorCodPostal[j]
                addressOrdenadosPorCodPostal[j] = address_que_va_despues

                # ORDENAMIENTO EN POSTAL ZIP
                postal_que_va_despues = postalOrdenadosPorCodPostal[i]
                postalOrdenadosPorCodPostal[i] = postalOrdenadosPorCodPostal[j]
                postalOrdenadosPorCodPostal[j] = postal_que_va_despues

                # ORDENAMIENTO EN REGION
                region_que_va_despues = regionOrdenadosPorCodPostal[i]
                regionOrdenadosPorCodPostal[i] = regionOrdenadosPorCodPostal[j]
                regionOrdenadosPorCodPostal[j] = region_que_va_despues

                # ORDENAMIENTO EN COUNTRY
                pais_que_va_despues = countryOrdenadosPorCodPostal[i]
                countryOrdenadosPorCodPostal[i] = countryOrdenadosPorCodPostal[j]
                countryOrdenadosPorCodPostal[j] = pais_que_va_despues

                # ORDENAMIENTO EN EDADES
                edad_que_va_despues = edadesOrdenadosPorCodPostal[i]
                edadesOrdenadosPorCodPostal[i] = edadesOrdenadosPorCodPostal[j]
                edadesOrdenadosPorCodPostal[j] = edad_que_va_despues


    mexicanos_y_brasileros_ordenados_por_codPostal = []

    for i in range(len(usuarios)):
        if (countryOrdenadosPorCodPostal[i] == 'Brazil' or countryOrdenadosPorCodPostal[i] == 'Mexico') and postalOrdenadosPorCodPostal[i] > 8000:
            mexicanos_y_brasileros_ordenados_por_codPostal += [[nombres[i], telefonos[i], mails[i], address[i], postalZip[i], region[i], country[i], edades[i]]]


    match opc:
        case 1:
            return [nombres, telefonos, mails, address, postalZip, region, country, edades]
        
        case 2:
            return datos_usuarios_mexico

        case 3:
            return datos_usuarios_brasil
        
        case 4:
            return datos_usuarios_mas_jovenes

        case 5:
            return promedio_de_edades # Lo dejo como un flotante para ver su proximidad con el siguiente nro.
        
        case 6:
            return datos_del_brasilero_de_mayor_edad

        case 7:
            return datos_de_mx_y_br_solicitados
        
        case 8:
            return datos_de_italianos_requeridos
        
        case 9:
            return mexicanos_filtrados_en_orden_por_nombre
        
        case 10:
            return usuarios_con_la_edad_menor
        
        case 11:
            return mexicanos_y_brasileros_ordenados_por_codPostal

print(menu_de_opciones())
