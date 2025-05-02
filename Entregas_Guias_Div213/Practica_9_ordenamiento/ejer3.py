"""
Ejercicio 3: Dadas las siguientes listas: 


Estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"] 

Apellidos = [“Sosa”,”Gutierrez”,”Alsina”,”Martinez”,”Sosa”,”Ramirez”,”Perez”,”Lopez”,”Arregui”,”Mitre”,"Andrade”,”Loza”,”Antares”,”Roca”,”Perez”] 

Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8] 


Desarrollar una función que realice el ordenamiento de las listas por apellido de manera ascendente, si el apellido es el mismo, debe ordenar por nombre de manera ascendente, si el nombre también es el mismo, debe ordenar por nota de manera descendente. 
"""


def ordenar_lista_por_apellidos_nombres_o_nota(listaApellidos:list, listaNombres:list, listaNotas:list)->list:
    for i in range(len(listaApellidos)-1):

        for j in range(i+1, len(listaApellidos)):


            # CASO DONDE LOS APELLIDOS SE PUEDEN ORDENAR
            if listaApellidos[i] > listaApellidos[j]: 
                # si el primer apellido i deberia ir despues del apellido j 


                # ordenamiento en nombres
                apellido_que_va_despues = listaApellidos[i] 
                # guardo en una varibale el apellido que deberia ir mas al final entre los que comparo, 
                # ya que en el siguiente paso voy a pisar el dato

                listaApellidos[i] = listaApellidos[j] 
                # pongo en la posicion que era del apellido mas grande, el apellido que deberia ir antes

                listaApellidos[j] = apellido_que_va_despues
                # en la posicion J, donde estaba el apellido que deberia ir antes, guardo el apellido que
                # debe ir aca, el cual guarde en la variable apellido_que_va_despues


                # Misma logica de arriba, pero con los nombres
                nombre_que_va_despues = listaNombres[i]
                listaNombres[i] = listaNombres[j]
                listaNombres[j] = nombre_que_va_despues


                # Misma logica de arriba, pero con las notas
                nota_que_va_despues = listaNotas[i]
                listaNotas[i] = listaNotas[j]
                listaNotas[j] = nota_que_va_despues
            


            # CASO DONDE EL APELLIDO ES EL MISMO, PERO LOS NOMBRES SE PUEDEN ORDENAR
            elif listaApellidos[i] == listaApellidos[j] and listaNombres[i] > listaNombres[j]:
                # si ambos apellidos son iguales pero los nombres son distintos (es decir, se pueden ordenar)


                # no hace falta ordenar los apellidos pq son iguales


                # se ordenan en base a orden de los nombres
                nombre_que_va_despues = listaNombres[i]
                listaNombres[i] = listaNombres[j]
                listaNombres[j] = nombre_que_va_despues


                # Misma logica de arriba, pero con las notas
                nota_que_va_despues = listaNotas[i]
                listaNotas[i] = listaNotas[j]
                listaNotas[j] = nota_que_va_despues
            


            # CASO DONDE EL APELLIDO Y NOMBRE SON EL MISMO, ASI QUE SE ORDENA POR NOTA DE FORMA ASCENDENTE
            elif listaApellidos[i] == listaApellidos[j] and listaNombres[i] == listaNombres[j] and listaNotas[i] < listaNotas[j]:
                # no hace falta ordenar los apellidos porque son iguales

                # no hace falta ordenar los nombres porque son iguales

                # Se ordenan las notas de forma descendente
                nota_que_va_despues = listaNotas[i]
                listaNotas[i] = listaNotas[j]
                listaNotas[j] = nota_que_va_despues

   
    return [listaApellidos, listaNombres, listaNotas]

Estudiantes = ["Ana","Luis","Juan","Sol","Roberto","Sonia","María","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "María"] 

Apellidos = ["Sosa","Gutierrez","Alsina","Martinez","Sosa","Ramirez","Perez","Lopez","Arregui","Mitre","Andrade","Loza","Antares","Roca","Perez"] 

Nota = [8,4,9,10,8,6,4,8,7,5,6,7,10,4,8] 


print(ordenar_lista_por_apellidos_nombres_o_nota(Apellidos, Estudiantes, Nota))