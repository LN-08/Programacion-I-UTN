from paquete.promediar_notas import promediar_notas

def mostrar_alumno_con_mayor_promedio_de_notas(lista_de_personas:list):
    mayor_promedio = lista_de_personas[0]
    lista_mayores_promedios = []

    for i in range(len(lista_de_personas)):
        if promediar_notas(mayor_promedio) < promediar_notas(lista_de_personas[i]):
            mayor_promedio = lista_de_personas[i]


    for i in range(len(lista_de_personas)):
        if promediar_notas(lista_de_personas[i]) == promediar_notas(mayor_promedio):
            lista_mayores_promedios.append(lista_de_personas[i])
    
    for i in range(len(lista_mayores_promedios)):
        print(f"Nombre: ", lista_mayores_promedios[i]["nombre"])
        print(f"Apellido: ", lista_mayores_promedios[i]["apellido"])
        print("")