"""
Crear una función que reciba como parámetro una cadena y determine la
cantidad de vocales que hay de cada una (individualmente). La función
retornará una matriz indicando en la columna 1 cada vocal, y en la columna 2
la cantidad.
Por ej:
cadena = “murcielaguito”
“a” 1
“e” 1
“i” 2
“o” 1
“u” 2
"""

def contar_vocales(cadena:str)->int:
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    

    for letra in range(len(cadena)):
        match cadena[letra]:
            case 'a': a += 1
            case 'e': e += 1
            case 'i': i += 1
            case 'o': o += 1
            case 'u': u += 1

    matriz = [
                ['a', a],
                ['e', e],
                ['i', i],
                ['o', o],
                ['u', u]
    ]
    
    return matriz

# mostrar_matriz(matriz)
print(contar_vocales('dinosaurio'))                
