"""
Dadas las siguientes listas:

Nombres=["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Ped
ro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]

edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

Desarrollar una función que reciba por parámetro la lista de edades, busque a las
personas de menor edad (puede ser más de una) y las retorne. El programa
principal deberá mostrar nombre y edad de los menores.

"""

nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"]

edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]

def buscar_persona_de_menor_edad(lista_de_edades)->list:

    datos_del_o_los_menores = []

    # buscar la edad mas chica de la lista dada por parametro
    menor_por_ahora = lista_de_edades[0]
    for i in range(len(lista_de_edades)):
        if lista_de_edades[i] < menor_por_ahora:
            menor_por_ahora = lista_de_edades[i]


    # buscar los nombres con la edad mas chica encontrada
    for i in range(len(lista_de_edades)):
        
        if lista_de_edades[i] == menor_por_ahora:
            datos_del_o_los_menores.append((nombres[i], lista_de_edades[i]))


    return datos_del_o_los_menores

print(buscar_persona_de_menor_edad([23,45,34,23,46,23,45,67,37,68,25,55,45,27,43]))