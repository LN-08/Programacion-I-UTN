"""
#1. Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.
pwCorrecta = "123"
pwIngresada = ""

while pwCorrecta != pwIngresada:
    pwIngresada = input("PW: ")

    if pwIngresada != pwCorrecta:
        print("PW Incorrecta. Intenta de nuevo.")

print("Acceso garantizado")



#2 Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.
pwCorrecta = "123"
pwIngresada = ""

intentos = 0

while pwCorrecta != pwIngresada and intentos <= 2:
    pwIngresada = input("PW: ")
    intentos += 1
    
    if pwIngresada != pwCorrecta:
        print("PW Incorrecta.")

if pwIngresada == pwCorrecta:
    print("Acceso garantizado")
else:
    print("Acceso denegado")



#3 Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.
nota = int("Nota: ")

if nota < 1 or nota > 10:
    print("Nota Incorrecta")



#4 Solicitarle al usuario el ingreso de un color. Validar que el mismo sea Rojo, Verde o Azul.
color = int("Color: ")

if color != "Rojo" or color != "rojo" or color != "Azul" or color != "azul" or color != "Verde" or color != "verde":
    print("Color invalido")



# INTEGRADOR VALIDACIONES

Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.
 
Los datos requeridos son:
Apellido
Edad, entre 18 y 90 años inclusive.
Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.

Una vez ingresados y validados los datos, mostrarlos por pantalla.
"""

apellido = input("Apellido: ")
edad = int(input("Edad: "))
estdCiv = int(input("Estado civil (1-Soltero, 2-Casado, 3-Divorciado, 4-Viudo): "))
legajo = int(input("Legajo: "))

while edad < 18 or edad > 90:
    print("La edad debe ser entre 18 y 90 años.")
    edad = int(input("Edad: "))

while estdCiv != 1 and estdCiv != 2 and estdCiv != 3 and estdCiv != 4:
    print("Estado civil incorrecto.")
    estdCiv = str(input("Estado civil (1-Soltero, 2-Casado, 3-Divorciado, 4-Viudo): "))

while legajo < 1000 or legajo > 9999:
    print("Legajo incorrecto.")
    legajo = int(input("Legajo: "))


print(f"Apellido: {apellido}")
print(f"Edad: {edad}")
print(f"Estado civil: {estdCiv}")
print(f"Legajo: {legajo}")