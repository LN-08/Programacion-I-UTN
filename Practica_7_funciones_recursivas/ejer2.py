# Realizar una función recursiva que calcule la potencia de un número:

def calcular_potencia(base:int, exponente:int):
    if exponente == 0:
        return 1
    else:
        return base * calcular_potencia(base, exponente - 1)

print(calcular_potencia(2,3))

"""
si ingreso 2 de base y 3 de exponente, la función realiza:

 2 * calcular_potencia(2,2) 
    2 * ( 2 * calcular_potencia(2,1) )
        2 * ( 2 * calcular_potencia(2,0) )
            2 * ( 2 * (2 * 1) )

2 * ( 2 * (2 * 1) ) = 8
"""
