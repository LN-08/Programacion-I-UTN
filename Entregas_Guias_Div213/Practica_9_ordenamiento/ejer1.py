"""
Ejercicio 1: 
Dadas las siguientes listas: 

Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"] 

Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43] 

Desarrollar una función que realice el ordenamiento de las listas por nombre de manera ascendente.
"""

def ordenar_lista_por_nombres(listaNombres:list, listaEdades:list)->list:
    for i in range(len(listaNombres)-1):

        for j in range(i+1, len(listaNombres)):

            if listaNombres[i] > listaNombres[j]: 
                # si el primer nombre i deberia ir despues del nombre j 
                # ejemplo: Sofia deberia ir despues de Maria


                # ordenamiento en nombres
                nombre_que_va_despues = listaNombres[i] 
                # guardo en una varibale el nombre que deberia ir mas al final entre los que comparo, 
                # ya que en el siguiente paso voy a pisar el dato. 
                # EJ: Guardo sofia en la variable

                listaNombres[i] = listaNombres[j] 
                # pongo en la posicion que era del nombre mas grande, el nombre que deberia ir antes
                # EJ: pongo Maria en la posicion donde estaba Sofia, tapando el dato previo de sofia

                listaNombres[j] = nombre_que_va_despues
                # en la posicion J, donde estaba el nombre que deberia ir antes, guardo el nombre que
                # debe ir aca, el cual guarde en la variable nombre_que_va_despues
                # EJ: pongo el nombre Sofia, guardado previamente en la variable, en la posicion posterior


                # Misma logica de arriba, pero con las edades
                edad_que_va_despues = listaEdades[i]
                listaEdades[i] = listaEdades[j]
                listaEdades[j] = edad_que_va_despues
   
    return [listaNombres, listaEdades]

Nombres = ["Ana","Luis","Juan","Sol","Roberto","Sonia","Ulises","Sofia","Maria","Pedro","Antonio", "Eugenia", "Soledad", "Mario", "Mariela"] 

Edades = [23,45,34,23,46,23,45,67,37,68,25,55,45,27,43] 

# print(ordenar_lista_por_nombres(Nombres, Edades))