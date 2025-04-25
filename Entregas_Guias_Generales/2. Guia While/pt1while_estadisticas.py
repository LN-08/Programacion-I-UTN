""""
#1. Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.
contador = 1
while contador <= 10:
    print(f"{contador}")
    contador += 1


#2 Mostrar 10 repeticiones de números descendentes desde el 10 al 1.
contador = 10
while contador > 0:
    print(f"{contador}")
    contador -= 1


#3. Mostrar la suma de los números desde el 1 hasta el 10
contador = 0
suma = contador

while contador <= 10:
    ######## 1+2+3+4+5+6.. = 55
    suma += contador
    contador += 1

print(f"{suma}")


#4. Mostrar la suma de los números pares desde el 1 hasta el 10.
contador = 0
suma = contador

while contador <= 10:
    ######## 2+4+6.. = 30
    if contador % 2 == 0:
        suma += contador

    contador += 1

print(f"{suma}")


#5. Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.
nrosIngresados = 0
suma = 0
promedio = 0

while nrosIngresados != 5:
    numero = int(input("Numero: "))
    suma += numero
    nrosIngresados += 1

promedio = suma / nrosIngresados
print(f"Promedio: {promedio}")


#6. Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.
quiere = True
suma = 0
cantIngresados = 0

while quiere:
    numero = int(input("Numero: "))
    suma += numero
    cantIngresados += 1

    continuar = int(input("Desea ingresar otro numero? (1-Si / 2-No): "))

    while continuar != 1 and continuar != 2:
        continuar = int(input("Dato incorrecto. Presione 1 si desea continuar, 2 si no: "))
    
    if continuar == 2:
        quiere = False

print(f"Suma: {suma}")
promedio = suma / cantIngresados
print(f"Promedio: {promedio}")


#7 Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.
quiere = True
suma = 0
producto = 1

while quiere:
    numero = int(input("Numero: "))

    if numero >= 0:
        suma += numero
    else:
        prodcuto *= numero
    

    continuar = int(input("Desea ingresar otro numero? (1-Si / 2-No): "))

    while continuar != 1 and continuar != 2:
        continuar = int(input("Dato incorrecto. Presione 1 si desea continuar, 2 si no: "))
    
    if continuar == 2:
        quiere = False

print(f"Sum. Positivos: {suma}")
print(f"Prod. Negativos: {producto}")


#8. Ingresar 10 números enteros. Determinar el máximo y el mínimo.
ingresados = 0
nroMax = 0
esPrimero = True

while ingresados <= 10:
    numero = int(input("Numero: "))

    if esPrimero == True:
        nroMax = numero
        nroMin = numero
        esPrimero = False
    else:
        if numero > nroMax:
            nroMax = numero
        elif numero < nroMin:
            nroMin = numero
    
    ingresados += 1

print(f"Nro max: {nroMax}") 
print(f"Nro min: {nroMin}")


#9. Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos.}
cantIngresados = 0
suma = 0
deseaSeguir = True

while cantIngresados <= 5:
    nro = int(input("Nro: "))
    suma += nro
    cantIngresados += 1


while deseaSeguir:
    continuar = int(input("Desea ingresar otro numero? (1-Si / 2-No): "))

    while continuar != 1 and continuar != 2:
        continuar = int(input("Nro incorrecto. Presione 1 si desea continuar, 2 si no: "))
    
    
    if continuar == 2:
        deseaSeguir = False
    else:
        nro = int(input("Nro: "))
        suma += nro
        cantIngresados += 1

promedio = suma / cantIngresados

print(f"Suma: {suma}")
print(f"Promedio: {promedio}")
"""


#10. Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de los mismos.

cantIngresados = 0
suma = 0

while cantIngresados <= 5:
    nro = int(input("Nro: "))
    suma += nro
    cantIngresados += 1


while deseaSeguir and cantIngresados <= 10:
    continuar = int(input("Desea ingresar otro numero? (1-Si / 2-No): "))

    while continuar != 1 and continuar != 2:
        continuar = int(input("Nro incorrecto. Presione 1 si desea continuar, 2 si no: "))
        
        
    if continuar == 2:
        deseaSeguir = False
    else:
        nro = int(input("Nro: "))
        suma += nro
        cantIngresados += 1


promedio = suma / cantIngresados
print(f"Suma: {suma}")
print(f"Promedio: {promedio}")



# INTEGRADOR WHILE
# Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
# La suma acumulada de los números negativos.
# La suma acumulada de los números positivos.
# La cantidad de números negativos ingresados.
# El promedio de los números positivos.
# El número positivo más grande.
# El porcentaje de números negativos ingresados, respecto del total de ingresos.

quiere = True
sumaNegativos = 0
sumaPositivos = 0
cantidadNegativos = 0
esPrimerPositivo = True
# % negativos ingresadoss

nro = int(input("Nro: "))
cantidadIngresados = 1

while quiere:

    if nro < 0:
        sumaNegativos += nro
        cantidadNegativos += 1
        cantidadIngresados += 1
    elif nro >= 0:
        sumaPositivos += nro
        cantidadPositivos += 1
        cantidadIngresados += 1

        if esPrimerPositivo:
            masGrande = nro
            esPrimerPositivo = False
        else:
            if nro > masGrande:
                masGrande = nro



    continuar = int(input("Desea ingresar otro numero? (1-Si / 2-No): "))

    while continuar != 1 and continuar != 2:
        continuar = int(input("Nro incorrecto. Presione 1 si desea continuar, 2 si no: "))
    

    if continuar == 2:
        quiere = False
    else:
        nro = int(input("Nro: "))
        cantidadIngresados += 1

print(f"Suma positivos: {sumaPositivos}")
print(f"Suma negativos: {sumaNegativos}")
print(f"Cantidad de negativos: {cantidadNegativos}")
print(f"Promedio positivos: {sumaPositivos / cantidadPositivos}")
print(f"Positivo mas grande: {masGrande}")
print(f"Porcentaje de negativos: % {cantidadNegativos / cantidadIngresados * 100}")