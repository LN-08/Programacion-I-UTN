# Realizar una función recursiva que calcule la suma de los primeros números naturales:

def sumar_naturales(numero:int)->int:
    # caso 1: el numero es 0, se devuelve 0
    if numero == 0:
        return 0
    else:
        return numero + sumar_naturales(numero - 1)
    

print(sumar_naturales(3))

"""
si ingreso 3, la funcion realiza:

 3 + sumar_naturales(2)
     2 + sumar_naturales(1)
         1 + sumar_naturales(0)
             0

3 + 2 + 1 + 0 = 6
"""
