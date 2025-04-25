# Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
# En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
# Si es invierno: solo se viaja a Bariloche.
# Si es verano: se viaja a Mar del plata y Cataratas.
# Si es otoño: se viaja a todos los lugares.
# Si es primavera: se viaja a todos los lugares menos Bariloche.

estacion = input("Estacion (Otoño, Invierno, Primavera, Verano): ")

destino =  str(input("Destino (bariloche, mdq, cataratas): "))

estacionMinus = estacion.lower()

match estacionMinus: 

    case "otoño":
        if destino.lower() == "bariloche" or destino.lower() == "mdq" or destino.lower() == "cataratas":
            print("Se viaja")
        else:
            print("No se viaja a ese destino")

    case "invierno":
        if destino.lower() == "bariloche":
            print("Se viaja")
        else:
            print("No se viaja a ese destino")

    case "primavera":
        if destino.lower() == "mdq" or destino.lower() == "cataratas":
            print("Se viaja")
        else:
            print("No se viaja a ese destino")

    case "verano":
        if destino.lower() == "mdq" or destino.lower() == "cataratas":
            print("Se viaja")
        else:
            print("No se viaja")

    case _:
        print(f"{estacion} no corresponde a ninguna estacion")
