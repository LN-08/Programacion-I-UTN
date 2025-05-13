#9 Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.

nro = int(input("Nro: "))

for i in range(1, nro + 1):
    if nro % i == 0:
        print(i)