"""
8. Realizar un programa que permita mostrar una pirámide de números. Por
ejemplo: si se ingresa el numero 5, la salida del programa será la
siguiente: 
1
12
123
1234
12345
"""

nro = int(input("Nro: "))

for i in range(1, nro + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()