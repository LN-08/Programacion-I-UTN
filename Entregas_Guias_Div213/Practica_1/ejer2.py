#Pedir una edad. Informar si la persona es mayor de edad (más de 18 años), adolescente (entre 13 y 17 años) o niño (menor a 13 años).

edad = int(input("Edad: "))

if edad >= 18:
    print("Es mayor")

elif edad >= 13:
    print("Es adolescente")

elif edad >= 0:
    print("Es menor")

else: 
    print("edad invalida")