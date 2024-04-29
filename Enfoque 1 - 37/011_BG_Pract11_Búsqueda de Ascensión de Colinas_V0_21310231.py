#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 10
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import random

def hill_climbing(funcion_objetivo, paso=0.01, iteraciones_maximas=1000): #Búsqueda de Ascenso de Colinas (Hill Climbing)
    punto_actual = random.uniform(-10, 10)  # Punto inicial aleatorio
    valor_actual = funcion_objetivo(punto_actual)
    
    for _ in range(iteraciones_maximas):
        nuevo_punto = punto_actual + random.uniform(-paso, paso)  # Movimiento aleatorio
        nuevo_valor = funcion_objetivo(nuevo_punto)
        
        if nuevo_valor > valor_actual:  # Maximizar la función
            punto_actual = nuevo_punto
            valor_actual = nuevo_valor
    
    return punto_actual, valor_actual

# Función objetivo de ejemplo (función cuadrática)
def funcion_objetivo(x):
    return -x**2

# Ejecutar la búsqueda de ascenso de colinas
maximo_local, valor_maximo = hill_climbing(funcion_objetivo)
print("Máximo local encontrado:", maximo_local)
print("Valor máximo encontrado:", valor_maximo)

