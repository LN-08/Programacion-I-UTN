continuar = True
encontro_el_tesoro = False

mapa = [
 [0, 0, 0, 0, 0],
 [0, 0, 0, 1, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0] ]



def verificar_tesoro(mapa:list, x:int, y:int) -> int:
    if mapa[x][y] == 1:
        distancia = 0
    else:
        distancia = (x - 1) + (y - 3)

        if distancia < 0:
            distancia = distancia * -1

    return distancia


while continuar and not encontro_el_tesoro:

    coordenada_x = int(input("X: "))
    coordenada_y = int(input("Y: "))


    while coordenada_x < 0 or coordenada_x > 4 or coordenada_y < 0 or coordenada_y > 4:
        print("Coordenadas incorrectas")
        coordenada_x = int(input("X: "))
        coordenada_y = int(input("Y: "))

    distancia = verificar_tesoro(mapa, coordenada_x, coordenada_y)

    if distancia == 0:
        print("¡Encontraste el tesoro!")
        encontro_el_tesoro = True
    else:
        print(f"Fallaste. El tesoro está a {distancia} casilleros de distancia.")

        continuar = int(input("Continuar? 1-Si | 2-No: "))

        if continuar == 1:
            continuar = True
        else:
            continuar = False
