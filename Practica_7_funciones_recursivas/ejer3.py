# Realizar una función recursiva que permita realizar la suma de los dígitos de un número:

def sumar_digitos(numero:int)->int:
    if numero == 0:
        return 0
    else:
        return numero % 10 + sumar_digitos(numero // 10)

print(sumar_digitos(1234))

"""
numero % 10 obtiene el ultimo digito de un nro
numero // 10 saca el ultimo digito del nro


si ingreso 1234

4 + sumar_digitos(123)
             3         + sumar_digitos(12)
                                2            + sumar_digitos(1)
                                                        1        + sumar_digitos(0)
                                                                            0

4 + 3 + 2 + 1 + 0 = 10
"""
