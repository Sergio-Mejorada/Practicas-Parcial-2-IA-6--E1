#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 53
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


import numpy as np
import matplotlib.pyplot as plt

# Definir la matriz de transición de un proceso de Markov de dos estados
P = np.array([[0.8, 0.2],  # Probabilidades de transición del estado 1 al estado 1 y al estado 2
              [0.4, 0.6]]) # Probabilidades de transición del estado 2 al estado 1 y al estado 2

# Definir el número de pasos y el estado inicial
num_pasos = 100
estado_actual = 0  # Empezamos en el estado 1

# Listas para almacenar los estados a lo largo del tiempo
estados = [estado_actual]

# Simular el proceso de Markov
for _ in range(num_pasos):
    # Elegir el próximo estado basado en las probabilidades de transición
    estado_siguiente = np.random.choice([0, 1], p=P[estado_actual])
    estados.append(estado_siguiente)
    estado_actual = estado_siguiente

# Graficar la evolución de los estados a lo largo del tiempo
plt.figure(figsize=(10, 5))
plt.plot(range(num_pasos + 1), estados, marker='o')
plt.xlabel('Tiempo')
plt.ylabel('Estado')
plt.title('Evolución de un Proceso de Markov')
plt.grid(True)
plt.xticks(np.arange(0, num_pasos + 1, step=10))
plt.yticks([0, 1], ['Estado 1', 'Estado 2'])
plt.show()
