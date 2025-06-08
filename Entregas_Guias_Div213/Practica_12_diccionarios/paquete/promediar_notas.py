def promediar_notas(estudiante:dict) -> int:
    total = 0
    for i in range(len(estudiante["notas"])):
        total += estudiante["notas"][i]
    
    promedio = total / len(estudiante["notas"])

    return promedio