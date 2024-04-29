#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 32
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

from nashpy import Game

# Definimos una matriz de pagos para el juego de ejemplo (coordenadas: Jugador 1, Jugador 2)
matriz_pagos = [[(3, 3), (0, 5)],
                [(5, 0), (1, 1)]]

# Creamos un objeto Game con la matriz de pagos
juego = Game(matriz_pagos)

# Encontramos el equilibrio de Nash del juego
equilibrio = juego.lemke_howson()

# Imprimimos el equilibrio de Nash encontrado
print("Equilibrio de Nash:", equilibrio)

# Calculamos el pago esperado para cada jugador en el equilibrio de Nash
pago_jugador1, pago_jugador2 = juego[equilibrio]
print("Pago esperado para Jugador 1:", pago_jugador1)
print("Pago esperado para Jugador 2:", pago_jugador2)

# Calculamos un mecanismo para incentivar un resultado específico (2, 2 en este caso)
mecanismo = juego.lemke_howson_enumeration()
pago_jugador1_mecanismo, pago_jugador2_mecanismo = juego[mecanismo]
print("Mecanismo para el resultado (2, 2):", mecanismo)
print("Pago esperado para Jugador 1 con el mecanismo:", pago_jugador1_mecanismo)
print("Pago esperado para Jugador 2 con el mecanismo:", pago_jugador2_mecanismo)
