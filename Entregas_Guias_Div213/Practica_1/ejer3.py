# Ingresar 5 números enteros, distintos de cero.
# Informar:
# a. Cantidad de pares e impares.
# b. El menor número ingresado.
# c. De los pares el mayor número ingresado.
# d. Suma de los positivos.
# e. Producto de los negativos.

# a
cantidadDePares = 0
# a
cantidadDeImpares = 0

# b
flagMenor = True
menorIngresado = 0

# c
mayorDePares = 0
flagMayor = True # Denota que es el primer elemento de los 5 numeros a ingresar


# d
sumaDePositivos = 0

# e
prodDeNegativos = 1
primDelArray = True

for i in range(5):

    numeroActual = int(print("Numero (no puede ser 0): " ))

    if numeroActual == 0:
        print("Nro invalido.")

    else:

        if numeroActual % 2 == 0:
            cantidadDePares = cantidadDePares + 1

            if flagMayor == True:
                mayorDePares = numeroActual
                flagMayor = False
            else:
                if numeroActual > mayorDePares:
                    mayorDePares = numeroActual

        else:
            cantidadDeImpares = cantidadDeImpares + 1
        


        if flagMenor == True:
            menorIngresado = i
            flagMenor = False
        else: 
            if menorIngresado > numeroActual:
                menorIngresado = numeroActual



        if numeroActual > 0:
            sumaDePositivos = sumaDePositivos + numeroActual
        
        else:
            if primDelArray == True:
                prodDeNegativos = prodDeNegativos * numeroActual
                primDelArray = False
            else:
                prodDeNegativos = prodDeNegativos * numeroActual


print(f"Cant. Pares: {cantidadDePares}. Cant. Impares: {cantidadDeImpares}")
print(f"Menor nro: {menorIngresado}")
print(f"Mayor de los pares: {mayorDePares}")
print(f"Suma de positivos: {sumaDePositivos}")
print(f"Producto de negativos: {prodDeNegativos}")