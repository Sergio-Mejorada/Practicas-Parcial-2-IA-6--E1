#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 51
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import numpy as np
import matplotlib.pyplot as plt

# Definir la matriz de transición de la cadena de Markov
P = np.array([[0.5, 0.3, 0.2],
              [0.2, 0.6, 0.2],
              [0.1, 0.4, 0.5]])

# Definir el número de iteraciones del algoritmo de Monte Carlo
num_iteraciones = 1000

# Inicializar la cadena de Markov en un estado aleatorio
estado_actual = np.random.choice([0, 1, 2])

# Listas para almacenar las muestras generadas por el algoritmo
muestras = []
estados_visitados = []

# Ejecutar el algoritmo de Monte Carlo
for _ in range(num_iteraciones):
    estados_visitados.append(estado_actual)
    muestras.append(estado_actual)
    estado_actual = np.random.choice([0, 1, 2], p=P[estado_actual])

# Calcular la frecuencia de visitas a cada estado
frecuencias = [estados_visitados.count(i) / num_iteraciones for i in range(3)]

# Imprimir la frecuencia estimada de cada estado
print("Frecuencia estimada de visitas a cada estado:", frecuencias)

# Graficar el histograma de las muestras generadas
plt.hist(muestras, bins=[0, 1, 2, 3], align='left', rwidth=0.5, edgecolor='black')
plt.xticks([0, 1, 2])
plt.xlabel('Estado')
plt.ylabel('Frecuencia')
plt.title('Histograma de Muestras Generadas por MCMC')
plt.show()
