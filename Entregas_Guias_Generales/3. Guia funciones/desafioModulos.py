"""
1.
Realizar una función para pedir un número por consola. La misma deberá seguir el siguiente prototipo:

En donde:
- mensaje: es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.
- mensaje_error: mensaje de error en el caso de que el dato ingresado sea invalido.
- mínimo: valor mínimo admitido (inclusive)
- máximo: valor máximo admitido (inclusive)
- reintentos: cantidad de veces que se volverá a pedir el dato en caso de error.

"""

def get_int(mensaje:str, mensaje_error:str, minimo: int, maximo: int, reintentos: int) -> int|None:

    print(mensaje)

    numero = int(input("Numero: "))

    if numero > maximo or numero < minimo:
        print(mensaje_error)

        while reintentos > 0 and (numero > maximo or numero < minimo):
            numero = int(input("Numero: "))

            if numero > maximo or numero < minimo:
                print(mensaje_error)
            
            reintentos = reintentos - 1

        
        if reintentos == 0:
            valor_a_devolver = None
        else:
            valor_a_devolver = numero

    else:
        valor_a_devolver = numero


    return(valor_a_devolver) # nro validado o None