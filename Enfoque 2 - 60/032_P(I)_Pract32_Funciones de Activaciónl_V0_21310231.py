#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 69
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import numpy as np

# Función de activación Sigmoid
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Función de activación ReLU (Rectified Linear Unit)
def relu(x):
    return np.maximum(0, x)

# Función de activación Tangente hiperbólica (Tanh)
def tanh(x):
    return np.tanh(x)

# Ejemplo de uso de las funciones de activación
x = np.array([-2, -1, 0, 1, 2])

# Calcular las salidas utilizando las funciones de activación
sigmoid_output = sigmoid(x)
relu_output = relu(x)
tanh_output = tanh(x)

# Imprimir los resultados
print("Entrada:", x)
print("Salida Sigmoid:", sigmoid_output)
print("Salida ReLU:", relu_output)
print("Salida Tanh:", tanh_output)
