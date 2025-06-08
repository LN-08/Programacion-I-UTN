def mostrar_promedio_edad(lista_de_personas:list):
    suma_de_edades = 0
    for i in range(len(lista_de_personas)):
        suma_de_edades += lista_de_personas[i]["edad"]
    
    promedio = suma_de_edades / len(lista_de_personas)

    print(f"Promedio de edad: ", promedio)