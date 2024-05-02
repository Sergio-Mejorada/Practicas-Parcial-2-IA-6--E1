#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 103
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


import random

# Función para generar un estado inicial aleatorio
def generar_estado_inicial(n):
    return [random.randint(1, n) for _ in range(n)]

# Función para evaluar la calidad de un estado (número de conflictos)
def evaluar_estado(estado):
    n = len(estado)
    conflictos = 0
    for i in range(n):
        for j in range(i + 1, n):
            if estado[i] == estado[j] or abs(estado[i] - estado[j]) == abs(i - j):
                conflictos += 1
    return conflictos

# Función para generar un vecino aleatorio
def generar_vecino(estado):
    vecino = estado.copy()
    i = random.randint(0, len(estado) - 1)
    j = random.randint(1, len(estado))
    vecino[i] = j
    return vecino

# Algoritmo de subida de colina (hill climbing)
def subida_colina(n, max_iter):
    estado_actual = generar_estado_inicial(n)
    mejor_estado = estado_actual.copy()
    mejor_evaluacion = evaluar_estado(mejor_estado)
    
    iteracion = 0
    while iteracion < max_iter:
        vecino = generar_vecino(estado_actual)
        evaluacion_vecino = evaluar_estado(vecino)
        if evaluacion_vecino < mejor_evaluacion:
            mejor_estado = vecino.copy()
            mejor_evaluacion = evaluacion_vecino
        estado_actual = vecino.copy()
        iteracion += 1
    
    return mejor_estado, mejor_evaluacion

# Ejemplo de uso del algoritmo de subida de colina para el problema de las N reinas
n_reinas = 8  # Tamaño del tablero de reinas
max_iteraciones = 1000  # Número máximo de iteraciones

mejor_estado, mejor_evaluacion = subida_colina(n_reinas, max_iteraciones)
print("Mejor estado encontrado:", mejor_estado)
print("Número de conflictos en el mejor estado:", mejor_evaluacion)
