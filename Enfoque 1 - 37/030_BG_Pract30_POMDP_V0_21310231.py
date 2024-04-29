#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 30
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


import numpy as np

# Definimos la matriz de transición como ejemplo
matriz_transicion = np.array([[0.7, 0.3],
                              [0.4, 0.6]])

# Definimos la matriz de observación como ejemplo
matriz_observacion = np.array([[0.9, 0.1],
                               [0.2, 0.8]])

# Definimos el estado inicial como ejemplo
estado_actual = np.array([0.5, 0.5])

# Definimos la secuencia de observaciones como ejemplo
secuencia_observaciones = [0, 1, 0, 1]

# Definimos el número de iteraciones que queremos realizar
num_iteraciones = len(secuencia_observaciones)

# Iteramos para realizar el proceso de iteración de Markov parcialmente observable
for obs in secuencia_observaciones:
    # Calculamos la probabilidad de la observación dada el estado actual
    prob_observacion_dado_estado = matriz_observacion[obs]
    # Actualizamos el estado actual con la probabilidad de la observación
    estado_actual = estado_actual * prob_observacion_dado_estado
    # Normalizamos el estado actual
    estado_actual /= np.sum(estado_actual)
    # Multiplicamos el estado actual por la matriz de transición
    estado_actual = np.dot(estado_actual, matriz_transicion)

# Imprimimos el estado final después de las iteraciones
print("Estado final después de las observaciones:")
print(estado_actual)
