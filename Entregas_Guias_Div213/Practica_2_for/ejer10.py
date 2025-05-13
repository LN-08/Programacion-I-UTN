#10.Ingresar un número. Determinar si el número es primo o no.
numero = int(input("Numero: "))

nroNoPrimo = False

if numero == 1:
    nroNoPrimo == True
else:
    for i in range (2, numero):
        if i != numero and numero % i == 0:
            nroNoPrimo = True

if nroNoPrimo == True:
    print("No es un nro primo.")
else:
    print("Es un nro primo.")