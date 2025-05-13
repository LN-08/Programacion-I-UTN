# Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil distinto a "Soltero",
# mostrar el siguiente mensaje: "Es muy pequeño para NO ser soltero."

edad = int(input("Edad: "))
estado_civil = input("Estado civil (soltero/casado/divorciado): ")

estadoMinus = estado_civil.lower()

if edad < 18 and estadoMinus != "soltero":
    print("Es muy pequeño para NO ser soltero.")