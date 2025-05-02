"""
Ejercicio 2: 

Dadas las siguientes listas: 

Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza"] 

Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98] 

Desarrollar una función que realice el ordenamiento de las listas por nombre de manera ascendente, si el nombre es el mismo, debe ordenar por puntos de manera descendente. 
"""

def ordenar_lista_por_nombres_o_puntaje(listaNombres:list, listaPuntos:list)->list:
    for i in range(len(listaNombres)-1):

        for j in range(i+1, len(listaNombres)):

            if listaNombres[i] > listaNombres[j]: 
                # si el primer nombre i deberia ir despues del nombre j 


                # ordenamiento en nombres
                nombre_que_va_despues = listaNombres[i] 
                # guardo en una varibale el nombre que deberia ir mas al final entre los que comparo, 
                # ya que en el siguiente paso voy a pisar el dato

                listaNombres[i] = listaNombres[j] 
                # pongo en la posicion que era del nombre mas grande, el nombre que deberia ir antes

                listaNombres[j] = nombre_que_va_despues
                # en la posicion J, donde estaba el nombre que deberia ir antes, guardo el nombre que
                # debe ir aca, el cual guarde en la variable nombre_que_va_despues


                # Misma logica de arriba, pero con los puntos
                puntaje_que_va_despues = listaPuntos[i]
                listaPuntos[i] = listaPuntos[j]
                listaPuntos[j] = puntaje_que_va_despues
            


            elif listaNombres[i] == listaNombres[j] and listaPuntos[i] < listaPuntos[j]:
                # si ambos nombres son iguales pero el puntaje de i es mas grande que el de j

                # no hace falta ordenar los nombres porque son iguales

                # se ordenan las notas de forma descendente
                puntaje_que_va_despues = listaPuntos[i]
                listaPuntos[i] = listaPuntos[j]
                listaPuntos[j] = puntaje_que_va_despues

   
    return [listaNombres, listaPuntos]

Nombres = ["Matematica","Investigacion Operativa","Ingles","Literatura","Ciencias Sociales","Computacion","Ingles","Algebra","Contabilidad","Artistica", "Algoritmos", "Base de Datos", "Ergonomia", "Naturaleza"] 

Puntos = [100,98,56,25,87,38,64,42,28,91,66,35,49,57,98] 

print(ordenar_lista_por_nombres_o_puntaje(Nombres, Puntos))

