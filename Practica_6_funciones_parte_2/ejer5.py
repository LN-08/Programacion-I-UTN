# Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.

def maximo_entre_tres(n1:int, n2:int, n3:int) -> int:
    if n1 > n2 and n1 > n3:
        print(n1)
    elif n2 > n1 and n2 > n3:
        print(n2)
    else: 
        print(n3)

maximo_entre_tres(9,12,18)