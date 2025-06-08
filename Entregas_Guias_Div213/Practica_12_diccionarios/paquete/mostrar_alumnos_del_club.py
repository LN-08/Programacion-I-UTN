def mostrar_alumnos_del_grupo(lista_de_personas:list, club:str):
    for estudiante in range(len(lista_de_personas)):
        if "grupos" in lista_de_personas[estudiante]:
            for grupo in lista_de_personas[estudiante]["grupos"]:
                if grupo["nombre"] == "Club de Informatica":
                    print(lista_de_personas[estudiante]["nombre"])
