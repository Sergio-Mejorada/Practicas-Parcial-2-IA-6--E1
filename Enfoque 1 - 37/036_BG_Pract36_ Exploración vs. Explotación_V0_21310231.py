#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 36
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


import numpy as np

# Función para elegir una acción basada en la estrategia epsilon-greedy
def epsilon_greedy(epsilon, valores_q):
    if np.random.uniform(0, 1) < epsilon:
        # Exploración: elige una acción aleatoria
        return np.random.choice(len(valores_q))
    else:
        # Explotación: elige la acción con el mayor valor Q
        return np.argmax(valores_q)

# Parámetros
epsilon = 0.2  # Factor de exploración (ε)
valores_q = [0.1, 0.5, 0.3, 0.9, 0.2]  # Valores Q para cada acción

# Ejemplo de uso de epsilon-greedy
num_iteraciones = 10
for iteracion in range(num_iteraciones):
    accion_elegida = epsilon_greedy(epsilon, valores_q)
    print(f"Iteración {iteracion + 1}: Acción elegida = {accion_elegida}")
