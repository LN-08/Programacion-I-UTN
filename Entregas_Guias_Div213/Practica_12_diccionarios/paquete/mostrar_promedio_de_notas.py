from paquete.promediar_notas import promediar_notas

def mostrar_promedio_de_notas(lista_de_personas:list):
    for i in range(len(lista_de_personas)):
        promedio_estudiante = promediar_notas(lista_de_personas[i])
        print(f"Nombre:", lista_de_personas[i]["nombre"])
        print(f"Promedio:", promedio_estudiante)
        print(f"Legajo:", lista_de_personas[i]["legajo"])
        
        print(" ")
