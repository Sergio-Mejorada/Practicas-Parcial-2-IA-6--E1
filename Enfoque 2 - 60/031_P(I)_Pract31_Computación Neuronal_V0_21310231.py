#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 68
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


import numpy as np

# Definir los pesos y el sesgo de la neurona
weights = np.array([0.5, 0.3])  # Pesos sinápticos
bias = -0.2  # Sesgo

# Función de activación sigmoidal
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Entradas de la neurona
inputs = np.array([1, 0.5])

# Calcular la suma ponderada de las entradas y el sesgo
weighted_sum = np.dot(weights, inputs) + bias

# Aplicar la función de activación sigmoidal
output = sigmoid(weighted_sum)

print("Salida de la neurona:", output)
