from paquete.imprimir_datos import imprimir_datos


def listar_por_apellido_o_nombre(lista_de_diccionarios:list):
    for i in range(len(lista_de_diccionarios) - 1):
        for j in range(len(lista_de_diccionarios)):
            if (lista_de_diccionarios[i]["apellido"] < lista_de_diccionarios[j]["apellido"]) or (lista_de_diccionarios[i]["apellido"] == lista_de_diccionarios[j]["apellido"] and lista_de_diccionarios[i]["nombre"] < lista_de_diccionarios[j]["nombre"]):
                aux = lista_de_diccionarios[i]
                lista_de_diccionarios[i] = lista_de_diccionarios[j]
                lista_de_diccionarios[j] = aux
    
    datos_necesarios = ["legajo", "nombre", "apellido", "edad"]

    imprimir_datos(datos_necesarios, lista_de_diccionarios)
