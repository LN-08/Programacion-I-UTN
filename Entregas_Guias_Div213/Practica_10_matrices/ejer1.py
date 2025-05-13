"""
Armar la lista de Productos con nombre, cantidad y ubicación (fila, columna)
"""

from paquete_manejo_basico_matrices.inicializar_la_matriz import inicializar_matriz
from paquete_manejo_basico_matrices.cargar_por_indice import cargar_matriz_automaticamente
from paquete_manejo_basico_matrices.mostrar_la_matriz import mostrar_matriz

matriz_inicializada = inicializar_matriz(3,5,["nada", 0])

matriz_cargada = cargar_matriz_automaticamente(matriz_inicializada)


# Mostrar matriz
mostrar_matriz(matriz_cargada)