from paquete_manejo_basico_matrices.inicializar_la_matriz import inicializar_matriz
from paquete_manejo_basico_matrices.cargar_secuencialmente import cargar_matriz_secuencialmente

def cargar_matriz():
    filas = int(input("Cantidad de filas: "))
    columnas = int (input("Cantidad de columnas: "))

    matriz_de_productos_inicializada = inicializar_matriz(filas, columnas, ["nada", 0]) 

    matriz_cargada = cargar_matriz_secuencialmente(matriz_de_productos_inicializada)

    return(matriz_cargada)