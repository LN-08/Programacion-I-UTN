primerFiltro = 0 # Cantidad de empleados de género masculino que votaron por IOT o IA, cuya edad esté entre 25 y 50 años inclusive.

segundoFiltro = 0 # Cantidad de empleados que no votaron por IA, siempre y cuando su género no sea Femenino o su edad se encuentre entre los 33 y 40

tercerFiltro = 0 # Mayor edad de los empleados de género masculino.
esPrimerEncuestado = True



for i in range(10):
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    genero = str(input("Genero (m/f/o): "))
    tecnologia = int(input("Tecnologia (1 - IA , 2 - RV/RA , 3 - IOT): "))



    ### FILTROS DE VERIFICACION

    while edad < 18:
        print("Edad incorrecta.")
        edad = int(input("Edad: "))
    
    while genero != "m" and genero != "f" and genero != "o":
        print("Genero incorrecto. Ingrese 'm', 'f', u 'o")
        genero = str(input("Genero (m/f/o): "))

    while tecnologia < 1 or tecnologia > 3:
        print("Numero incorrecto.")
        tecnologia = int(input("Tecnologia (1 - IA , 2 - RV/RA , 3 - IOT): "))
    


    ### ALGORITMO SOLICITADO

    if genero == "m" and (tecnologia == 1 or tecnologia == 3) and (edad >= 25 and edad <= 50):
        primerFiltro = primerFiltro + 1
    

    # FILTRA HOMBRES, QUE NO VOTARON IA, Y NO TENGAN ENTRE 33 Y 40 AÑOS
    if tecnologia != 1 and genero != "f" and edad < 33 or edad > 40:
        segundoFiltro = segundoFiltro + 1



    if esPrimerEncuestado == True and genero == "m":
        tercerFiltro = edad
        nombreDelMayor = nombre
        esPrimerEncuestado = False

    elif esPrimerEncuestado == False and genero == "m":
        if (edad > tercerFiltro):
            tercerFiltro = edad
            nombreDelMayor = nombre
            tecnologiaDelMayor = tecnologia

print(f"Cantidad de empleados de género masculino que no votaron por IA o IOT, que tengan entre 25 y 50 años inclusive: {primerFiltro}")

print(f"Porcentaje de empleados que no votaron por IA, que correspondan al genero masculino y su edad no se encuentre entre los 33 y 40: % {int(segundoFiltro * 100 / 10)})")

print(f"{nombre} es el empleado masculino de mayor edad, y voto por la tecnologia nro {tecnologiaDelMayor}")