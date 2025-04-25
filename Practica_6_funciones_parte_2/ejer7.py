# Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.

def es_primo(numero:int) -> bool:
    if numero <= 1:
        return False
    else:
        for i in range (2, numero):
            if i != numero and numero % i == 0:
                return True

if es_primo(7):
    print("es primo")
else:
    print("no es primo")