def mostrar_numero(nro:int):
    if nro < 1 or nro > 10:
        print("el numero debe estar entre 1 y 10")
    else:
        print(nro)

mostrar_numero(6)

# 
#

def retornar_numero():
    nro = int(input("Numero: "))

    if nro < 1 or nro > 10:
        print("el numero debe estar entre 1 y 10")
    else:
        return nro

print(retornar_numero())