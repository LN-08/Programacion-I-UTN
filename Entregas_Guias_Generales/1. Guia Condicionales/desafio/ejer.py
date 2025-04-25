""" 
Facturación del Servicio de Agua Potable

El acceso al agua potable es un servicio esencial para hogares, comercios e industrias. Para garantizar un uso eficiente del recurso y establecer una estructura justa de costos, se han definido diferentes tarifas y ajustes según el consumo y el tipo de cliente.

Este sistema de facturación contempla una tarifa base que incluye un cargo fijo y un costo variable por metro cúbico consumido. Además, se aplican bonificaciones y recargos dependiendo del consumo y la categoría del usuario. En algunos casos especiales, también pueden otorgarse descuentos adicionales.

A continuación, se detallan las reglas del sistema de facturación y los cálculos necesarios para determinar el monto final a pagar.

Tarifa base:
* Todas las facturas incluyen un cargo fijo de $7000 además del costo por consumo.
* El costo por metro cúbico (m³) de agua es de $200/m³.



Bonificaciones y Recargos según tipo de cliente:

____Cliente Residencial:
* Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del consumo.
* Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo.

____Cliente Comercial:
* Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del consumo.
* Si el consumo supera los 300 m³, la bonificación aumenta al 12%.
* Si el consumo es menor a 50 m³, se aplica un recargo del 5%.

____Cliente Industrial:
* Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del 
consumo.
* Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%.
* Si el consumo es menor a 200 m³, se aplica un recargo del 10%.

____Casos especiales:
* Si el cliente es Residencial y el total de la factura sin impuestos ni bonificaciones  es menor a $35000, se aplica un descuento adicional del 5%.



En todos los casos, se aplica el IVA del 21% sobre el total.




Requerimientos del programa:

1. Solicitar al usuario:
* Cantidad de metros consumidos
* Tipo de cliente, que puede ser: Residencial, Comercial o Industrial.

2. Calcular:
* Subtotal de consumo.
* Bonificaciones, si corresponde
* Recargos, si corresponde
* Subtotal, con recargos y bonificaciones.
* IVA aplicado (21%), si corresponde.
* Total final a pagar.

3.Mostrar en pantalla el desglose de los cálculos.

"""

cantMetros = int(input("Cantidad de m³ consumidos: "))

tipoCliente = str(input("Tipo de cliente (residencial, comercial, industrial): "))


tipoClienteMinus = tipoCliente.lower()


costoMetroCubico = 200 # 200 cuesta cada metro cubico consumido
costoConsumo = cantMetros * costoMetroCubico # cuanto se gasta contando solo consumo
cargoFijo = 7000 # valor agregado de cobro
costoConsumoMasCargoFijo = costoConsumo + cargoFijo # el costo de lo consumido mas el valor agregado de 7000



match tipoClienteMinus:

    case "residencial":
        if cantMetros < 30:
            descuento = costoConsumo * 10 / 100 
            costoSinIva = costoConsumoMasCargoFijo - descuento
            costoConIva = costoSinIva + (costoSinIva * 21 / 100)  
            input(f"Subtotal (SIN IVA): ${costoSinIva} | DESCUENTO RESIDENCIAL POR CONSUMO: 10% (${descuento}) | Presione enter para continuar")
            input(f"Costo final: ${costoConIva} | Presione enter para salir") 
        
        elif cantMetros <= 80:
            costoConIva = costoConsumoMasCargoFijo + (costoConsumoMasCargoFijo * 21 / 100)
            input(f"Subtotal (SIN IVA): ${costoConsumoMasCargoFijo} | Presione enter para continuar")
            input(f"Costo final: ${costoConIva} | Presione enter para salir")
        
        else:
            recargo = costoConsumo * 15 / 100
            costoSinIva = costoConsumoMasCargoFijo  + recargo
            costoConIva = costoSinIva + (costoSinIva * 21 / 100)  
            input(f"Subtotal (SIN IVA): ${costoSinIva} | RECARGO RESIDENCIAL POR CONSUMO: 15% (${recargo}) | Presione enter para continuar")
            input(f"Costo final: ${costoConIva} | Presione enter para salir") 



    case "comercial":
        if cantMetros > 150:
            bonificacion = costoConsumo * 8 / 100
            costoSinIva = costoConsumoMasCargoFijo - bonificacion 
            costoConIva = costoSinIva + (costoSinIva * 21 / 100)
            input(f"Subtotal (SIN IVA): ${costoSinIva} | BONIFICACION COMERCIAL POR CONSUMO: 8% (${bonificacion}) | Presione enter para continuar")
            input(f"Costo final: ${costoConIva} | Presione enter para salir")
        
        elif cantMetros > 300:
            bonificacion = costoConsumo * 12/ 100
            costoSinIva = costoConsumoMasCargoFijo - bonificacion 
            costoConIva = costoSinIva + (costoSinIva * 21 / 100)
            input(f"Subtotal (SIN IVA): ${costoSinIva} | BONIFICACION COMERCIAL POR CONSUMO: 12% (${bonificacion}) | Presione enter para continuar")
            input(f"Costo final: ${costoConIva} | Presione enter para salir")

        elif cantMetros >= 50:
             costoConIva = costoConsumoMasCargoFijo + (costoConsumoMasCargoFijo * 21 / 100)
             input(f"Subtotal (SIN IVA): ${costoConsumoMasCargoFijo} | Presione enter para continuar")
             input(f"Costo final: ${costoConIva} | Presione enter para salir")
        
        else:
            recargo = costoConsumo * 5 / 100
            costoSinIva = costoConsumoMasCargoFijo + recargo
            costoConIva = costoSinIva + (costoSinIva * 21 / 100)
            input(f"Subtotal (SIN IVA): ${costoSinIva} | RECARGO COMERCIAL POR CONSUMO: 5% (${recargo}) | Presione enter para continuar")
            input(f"Costo final: ${costoConIva} | Presione enter para salir")



    case "industrial":
        if cantMetros > 500:
            bonificacion = costoConsumo * 20 / 100
            costoSinIva = costoConsumoMasCargoFijo - bonificacion 
            costoConIva = costoSinIva + (costoSinIva * 21 / 100)
            input(f"Subtotal (SIN IVA): ${costoSinIva} | BONIFICACION INDUSTRIAL POR CONSUMO: 20% (${bonificacion}) | Presione enter para continuar")
            input(f"Costo final: ${costoConIva} | Presione enter para salir")

        elif cantMetros > 1000:
            bonificacion = costoConsumo * 30 / 100
            costoSinIva = costoConsumoMasCargoFijo - bonificacion 
            costoConIva = costoSinIva + (costoSinIva * 21 / 100)
            input(f"Subtotal (SIN IVA): ${costoSinIva} | BONIFICACION INDUSTRIAL POR CONSUMO: 30% (${bonificacion}) | Presione enter para continuar")
            input(f"Costo final: ${costoConIva} | | Presione enter para salir")

        elif cantMetros >= 200:
            costoConIva = costoConsumoMasCargoFijo + (costoConsumoMasCargoFijo * 21 / 100)
            input(f"Subtotal (SIN IVA): ${costoConsumoMasCargoFijo} | Presione enter para continuar")
            input(f"Costo final: ${costoConIva} | Presione enter para salir")
        
        else:
            recargo = costoConsumo * 10 / 100
            costoSinIva = costoConsumoMasCargoFijo + recargo
            costoConIva = costoSinIva + (costoSinIva * 21 / 100)
            input(f"Subtotal (SIN IVA): ${costoSinIva} | RECARGO INDUSTRIAL POR CONSUMO: 10% (${recargo}) | Presione enter para continuar")
            input(f"Costo final: ${costoConIva} | Presione enter para salir")



    case _:
        input("TIPO DE CLIENTE INVALIDO")
