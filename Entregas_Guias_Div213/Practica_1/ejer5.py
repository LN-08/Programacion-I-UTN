""""
Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
por cada estadía como base, se pide el ingreso de una estación del
año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
Plata/Córdoba) para vacacionar para poder calcular el precio final:
-en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un
descuento del 10% Mar del Plata tiene un descuento del 20%
-en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene
un aumento del 10% Mar del Plata tiene un aumento del 20%
-en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el
precio sin descuento.
Validar el ingreso de datos

"""

precioBase = 15000 

estacion = str(print("Estacion (otoño/invierno/primavera/verano): "))

localidad = str(print("Localidad (bariloche/cataratas/mdq/cordoba): "))

estacionLower = estacion.lower()

if estacionLower == "invierno":
    precioBariloche = precioBase + precioBase * 20 / 100
    precioMdq = precioBase - precioBase * 20 / 100
    precioCataratas = precioBase - precioBase * 10 / 100
    precioCordoba = precioBase - precioBase * 10 / 100

    print(f"Precios --> Bariloche: ${precioBariloche}, Mdq: ${precioMdq}, Cataratas: ${precioCataratas}, Cordoba: ${precioCordoba}")

elif estacionLower == "verano":
    precioBariloche = precioBase - precioBase * 20 / 100
    precioMdq = precioBase + precioBase * 20 / 100
    precioCataratas = precioBase + precioBase * 10 / 100
    precioCordoba = precioBase + precioBase * 10 / 100

elif estacionLower == "otoño" or estacionLower == "primavera":
    precioBariloche = precioBase + precioBase * 10 / 100
    precioMdq = precioBase + precioBase * 10 / 100
    precioCataratas = precioBase + precioBase * 10 / 100
    precioCordoba = precioBase

else:
    print(f"Estacion inexistente.")