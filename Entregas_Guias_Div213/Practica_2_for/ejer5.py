# 5. Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0. Mostrar la suma y el promedio de todos los números.

suma = 0
promedio = 0

for i in range(1,11):
    nro = int(input("Nro: "))

    if nro == 0:
        break

    suma = suma + nro
    promedio = promedio + nro

print(f"Suma de los nros: {suma}")
print(f"Prom. de los nros: {promedio / 10}")