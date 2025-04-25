#Realizar un programa que: asigne a la variable numero1 un valor  solicitado al usuario, valide el mismo entre 10 y 100, realice un descuento del 5% a  dicho valor a través de una función llamada realizarDescuento(). Mostrar el resultado por pantalla.  Atención: pueden reutilizarse funciones ya creadas.

def realizarDescuento(nro:int)->int:
    return nro - nro*5/100


numero1 = int(input("Numero: "))

if numero1 >= 10 and numero1 <= 100:
    print(f"Valor original: {numero1}")
    print(realizarDescuento(numero1))
else:
    print("El numero debe estar entre 10 y 100.")
