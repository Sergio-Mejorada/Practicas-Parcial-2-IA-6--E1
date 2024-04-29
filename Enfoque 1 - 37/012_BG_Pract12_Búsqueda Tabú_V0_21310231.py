#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 11
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import random

def busqueda_tabu(funcion_objetivo, movimientos_tabu=10, iteraciones_maximas=1000):
    punto_actual = random.uniform(-10, 10)  # Punto inicial aleatorio
    valor_actual = funcion_objetivo(punto_actual)
    mejor_solucion = punto_actual
    mejor_valor = valor_actual
    lista_tabu = []
    
    for _ in range(iteraciones_maximas):
        movimientos = [punto_actual + random.uniform(-0.1, 0.1) for _ in range(movimientos_tabu)]  # Genera movimientos aleatorios
        movimientos_valores = [(movimiento, funcion_objetivo(movimiento)) for movimiento in movimientos]
        movimientos_valores.sort(key=lambda x: x[1])  # Ordena los movimientos por el valor de la función objetivo
        
        mejor_movimiento = None
        for movimiento, valor in movimientos_valores:
            if movimiento not in lista_tabu:
                mejor_movimiento = movimiento
                break
        
        if mejor_movimiento is None:  # Si todos los movimientos están en la lista tabú, termina
            break
        
        punto_actual = mejor_movimiento
        valor_actual = funcion_objetivo(punto_actual)
        
        if valor_actual < mejor_valor:  # Minimizar la función
            mejor_solucion = punto_actual
            mejor_valor = valor_actual
        
        lista_tabu.append(mejor_movimiento)
        if len(lista_tabu) > movimientos_tabu:  # Mantiene la lista tabú con longitud máxima
            lista_tabu.pop(0)
    
    return mejor_solucion, mejor_valor

# Función objetivo de ejemplo (función cuadrática)
def funcion_objetivo(x):
    return x**2

# Ejecutar la búsqueda tabú
mejor_solucion, mejor_valor = busqueda_tabu(funcion_objetivo)
print("Mejor solución encontrada:", mejor_solucion)
print("Valor mínimo encontrado:", mejor_valor)

