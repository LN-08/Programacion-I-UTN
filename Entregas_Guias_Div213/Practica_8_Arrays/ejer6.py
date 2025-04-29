"""
Ejercicio 6: Analizar los datos del archivo listas_personas.py.  Utilizando el archivo 
listas_personas.py. Importar los nombres a una lista. Realizar una función que 
muestre los mismos
"""
from listas_personas import nombres

lista_de_nombres = []

for i in range(len(nombres)):
    lista_de_nombres.append(nombres[i])

print(lista_de_nombres)

# otra opcion era:
# lista_de_nombres = nombres
# print(lista_de_nombres)