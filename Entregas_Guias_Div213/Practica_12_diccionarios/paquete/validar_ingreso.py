def validar_ingreso_de_datos(mensaje_error:str, mensaje_reingreso:str, n_min:int, n_max:int, opcion:str):
    """  
    # valida que el numero ingresado sea valido

    # args:
        mensaje_error -> un string que muestra si no es valido el numero ingresado
        n_min -> nro minimo que se puede ingresar
        n_max -> nro maximo que se puede ingresar
        opcion -> nro que se ingreso inicialmente, y el cual vamos a validar

    # returns:
            el nuevo valor asignado a opcion
    """
    while opcion != '1' and opcion != '2' and opcion != '3' and opcion != '4' and opcion != '5' and opcion != '6' and opcion != '7' and opcion != '8' :
        print("✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖")
        print(f"{mensaje_error}")
        print("✖✖✖✖ ✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖✖")
        opcion = input(f"● {mensaje_reingreso} ({n_min}-{n_max}): ")
        
    return opcion