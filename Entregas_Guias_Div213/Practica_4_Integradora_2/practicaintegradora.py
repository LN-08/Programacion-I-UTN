cantidadCensados = 0

# 1
primerFiltro = 0

#2
primerIngreso = True
nombreSegundoFiltro = "No hay un jugador menor de edad con mas de 50 puntos"
categoriaSegundoFiltro = "No hay un jugador menor de edad con mas de 50 puntos"

#3
tercerFiltro = 0

#4
cantidadDeAvanzados = 0

#5
cantSaquesPlanos = 0
cantSaquesLiftados = 0
cantSaquesCortados = 0

# continuar
continuar = True

while continuar == True:
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    puntos = int(input("Puntos: "))
    ganadas = int(input("Ganadas: "))
    tipoSaque = int(input("Saque: 1.Plano 2.Liftado 3.Cortado: "))
    categoria = int(input("Categoria: 1.Elite 2.Experto 3.Avanzado: "))

    # VALIDACIONES
    while edad < 0:
        input("Edad invalida")
        edad = int(input("Edad: "))
    
    while puntos > 60 or puntos <= 0:
        input("Cantidad de puntos invalida")
        edad = int(input("Puntos: "))

    while tipoSaque < 1 or tipoSaque > 3:
        input("Tipo de saque invalido")
        tipoSaque = int(input("Saque: 1.Plano 2.Liftado 3.Cortado: "))

    while categoria < 1 or categoria > 3:
        input("Categoria invalida")
        categoria = int(input("Categoria: 1.Elite 2.Experto 3.Avanzado: "))
    

    cantidadCensados += 1

    # 1-Cantidad de jugadores de la categoría "elite" con tipo de saque “plano”, cuya edad esté entre 19 y 25 años inclusive
    if categoria == 1 and tipoSaque == 1 and (edad >= 19 and edad <= 25):
        primerFiltro = primerFiltro + 1

    # 2-Nombre y Categoría del jugador de menor edad con más de 50 puntos.
    if primerIngreso == True and edad < 18 and puntos > 50:
        edadDelMayor = edad
        nombreSegundoFiltro = nombre
        categoriaSegundoFiltro = categoria
        primerIngreso = False

    elif primerIngreso == False and edad < 18 and puntos > 50:
        if edad > edadDelMayor:
            nombreSegundoFiltro = nombre
            categoriaSegundoFiltro = categoria
    
    # 3 - Porcentaje de jugadores de categoría "experto".
    if categoria == 3:
        tercerFiltro += 1

    # 4 - Mostrar el promedio de edad de los jugadores cuya categoría es “avanzado”.
    if categoria == 3:
        sumaDeEdades += edad
        cantidadDeAvanzados += 1 
        
        # 5 - Determinar el tipo de saque más usado por los jugadores, cuya categoría sea “elite”.
        if tipoSaque == 1:
            cantSaquesPlanos += 1
        elif tipoSaque == 2:
            cantSaquesLiftados += 1
        else:
            cantSaquesCortados += 1
    

    # Continuar
    seguir = 0

    while seguir != 1 and seguir != 2:
        seguir = int(input("Continuar? (1-Si, 2-No): "))

        if seguir == 1:
            continuar = True
        elif seguir == 2:
            continuar = False
        else:
            print("Nro Incorrecto")
            seguir = 0

#5 continuacion
if cantSaquesPlanos > cantSaquesLiftados and cantSaquesPlanos > cantSaquesCortados:
    saqueGanador = "Plano"
elif cantSaquesLiftados > cantSaquesPlanos and cantSaquesLiftados > cantSaquesCortados:
    saqueGanador = "Liftado"
else:
    saqueGanador = "Cortado"

print(f"Cantidad de jugadores de la categoría 'elite' con tipo de saque “plano”, cuya edad esté entre 19 y 25 años inclusive: {primerFiltro}")

print(f"Nombre: {nombreSegundoFiltro}, categoria: {categoriaSegundoFiltro}")

print(f"Porcentaje de jugadores de categoría 'experto': {tercerFiltro / cantidadCensados * 100}")

print(f"Promedio de edad de los jugadores cuya categoría es 'avanzado': {sumaDeEdades / cantidadDeAvanzados}")

print(f"Tipo de saque más usado por los jugadores de categoría sea 'elite': {saqueGanador}")
        

