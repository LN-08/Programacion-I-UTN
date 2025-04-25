"""
Realizar una función para calcular el número de Fibonacci de un número ingresado por consola. La función deberá seguir el siguiente prototipo:

Definición:
La sucesión de Fibonacci comienza con los números 0 y 1, y cada número subsecuente es la suma de los dos anteriores:
f(0) = 0
f(1) = 1


f(2) = f(1) + f(0) = 1 + 0 = 1
f(3) = f(2) + f(1) = 1 + 1 = 2
f(4) = f(3) + f(2) = 2 + 1 = 3
f(5) = f(4) + f(3) = 3 + 2 = 5
...
"""



# EJ: INGRESAN 5
def calcular_fibonacci(numero: int) -> int:
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        return calcular_fibonacci(numero - 1) + calcular_fibonacci(numero - 2)

print(calcular_fibonacci(5))

"""
F(5) = F(4) + F(3)
     = (F(3) + F(2)) + (F(2) + F(1))
     = ((F(2) + F(1)) + (F(1) + F(0))) + ((F(1) + F(0)) + F(1))
     = ((1 + 1) + (1 + 0)) + ((1 + 0) + 1)
     = 2 + 1 + 1 + 1 = 5
"""

