# Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su sueldo para esa persona.

nombre = str(input("Nombre: "))
sueldo = int(input("Sueldo: "))

print(f"El sueldo de {nombre} incrementado en un 10% es de {int(sueldo + sueldo * 10 / 100)}")