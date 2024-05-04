#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 118
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

pip install scikit-fuzzy


import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Generar el universo de discurso para la variable de entrada
x = np.arange(0, 11, 1)

# Generar los conjuntos difusos
bajo = fuzz.trimf(x, [0, 0, 5])
medio = fuzz.trimf(x, [0, 5, 10])
alto = fuzz.trimf(x, [5, 10, 10])

# Visualizar los conjuntos difusos
plt.figure()
plt.plot(x, bajo, 'b', label='Bajo')
plt.plot(x, medio, 'g', label='Medio')
plt.plot(x, alto, 'r', label='Alto')
plt.title('Conjuntos Difusos')
plt.legend()
plt.show()
