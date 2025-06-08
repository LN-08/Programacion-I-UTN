from paquete.buscar_edad_mas_joven import buscar_edad_mas_joven

def mostrar_que_cursan_los_mas_jovenes(lista_de_personas:list):
    edad_mas_joven = buscar_edad_mas_joven(lista_de_personas)
    personas_jovenes = []

    for i in range(len(lista_de_personas)):
        if lista_de_personas[i]["edad"] == edad_mas_joven:
            personas_jovenes.append(lista_de_personas[i])
    


    for i in range(len(personas_jovenes)):
        print(f"Legajo: ",personas_jovenes[i]["legajo"])
        print(f"Nombre: ",personas_jovenes[i]["nombre"])
        print(f"Apellido: ",personas_jovenes[i]["apellido"])
        print(f"Programa: ",personas_jovenes[i]["programa"])
        print("")