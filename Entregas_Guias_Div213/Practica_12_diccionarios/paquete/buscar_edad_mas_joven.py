def buscar_edad_mas_joven(lista_de_personas:list)->int:
    edad_mas_joven = lista_de_personas[0]["edad"]
    for i in range(len(lista_de_personas)):
        if lista_de_personas[i]["edad"] < edad_mas_joven:
            edad_mas_joven = lista_de_personas[i]["edad"]
        
    return edad_mas_joven
