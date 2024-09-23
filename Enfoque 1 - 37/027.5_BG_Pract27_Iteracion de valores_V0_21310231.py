#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 67
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

def calcular_pagos(prestamo, tasa_interes_anual, pago_mensual):
    # Convertir tasa anual a tasa mensual
    tasa_mensual = tasa_interes_anual / 12 / 100
    
    meses = 0
    saldo = prestamo
    
    # Iterar hasta que el saldo sea 0 o menor
    while saldo > 0:
        # Aplicar el interés mensual al saldo
        interes_mensual = saldo * tasa_mensual
        saldo += interes_mensual
        
        # Hacer el pago mensual
        saldo -= pago_mensual
        meses += 1
        
        # Si el saldo es negativo, se ha pagado completamente
        if saldo < 0:
            saldo = 0
    
    return meses

# Solicitar datos al usuario
print("Calculadora de pagos de préstamos")
prestamo = float(input("Ingresa el monto del préstamo: "))
tasa_interes_anual = float(input("Ingresa la tasa de interés anual (en %): "))
pago_mensual = float(input("Ingresa el pago mensual que harás: "))

# Calcular el número de meses
meses = calcular_pagos(prestamo, tasa_interes_anual, pago_mensual)

# Mostrar el resultado
print(f"Te tomará {meses} meses pagar el préstamo.")
