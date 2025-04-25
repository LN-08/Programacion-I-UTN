#Ejercicio 3-7: Realizar un programa que: asigne a las variables numero1 y numero2 los valores solicitados al usuario, valide los mismos entre 10 y 100, asigne a la  variable operacion el valor solicitado al usuario: 's'-sumar, 'r'-restar (validar), realice la operación de dichos valores a través de una función. Mostrar el resultado por pantalla.

numero1 = int(input("Numero 1: "))
numero2 = int(input("Numero 2: "))
flag = True

while flag == True:
    operacion = input("s para sumar, r para restar: ")

    if operacion != "s" and operacion != "S" and operacion != "r" and operacion != "r":
        print("operacion invalida")
    else:
        flag = False

    
def resultado_suma(n1:int, n2:int) -> int:
    return n1 + n2

def resultado_resta(n1:int, n2:int) -> int:
    return n1 - n2


if (numero1 >= 10 and numero1 <= 100) and (numero2 >= 10 and numero2 <= 100):
    if operacion == 's':
        print(resultado_suma(numero1, numero2))
    else:
        print(resultado_resta(numero1, numero2))