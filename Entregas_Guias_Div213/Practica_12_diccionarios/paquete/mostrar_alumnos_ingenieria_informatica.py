def mostrar_alumnos_ingenieria_informatica(lista_de_personas:list):
    for i in range(len(lista_de_personas)):
        if lista_de_personas[i]["programa"]["nombre"] == "Ingenieria en Informatica":
            print(f"Legajo: ", lista_de_personas[i]["legajo"])
            print(f"Nombre: ", lista_de_personas[i]["nombre"])
            print(f"Apellido: ", lista_de_personas[i]["apellido"])
            print(f"Edad: ", lista_de_personas[i]["edad"])
            print("")