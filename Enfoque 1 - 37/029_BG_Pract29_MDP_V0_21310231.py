#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 29
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import numpy as np

# Definimos la matriz de transición como ejemplo
matriz_transicion = np.array([[0.7, 0.3],
                              [0.4, 0.6]])

# Definimos el estado inicial como ejemplo
estado_actual = np.array([0.5, 0.5])

# Definimos el número de iteraciones que queremos realizar
num_iteraciones = 5

# Iteramos para realizar el proceso de iteración de Markov
for _ in range(num_iteraciones):
    # Multiplicamos el estado actual por la matriz de transición
    nuevo_estado = np.dot(estado_actual, matriz_transicion)
    # Actualizamos el estado actual con el nuevo estado calculado
    estado_actual = nuevo_estado

# Imprimimos el estado final después de las iteraciones
print("Estado final después de", num_iteraciones, "iteraciones:")
print(estado_actual)
