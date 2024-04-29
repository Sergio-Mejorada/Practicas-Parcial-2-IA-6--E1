#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 33
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import numpy as np
import gym

# Creamos el entorno de ejemplo (usaremos el entorno CartPole de gym)
env = gym.make('CartPole-v1')

# Definimos el número de episodios y el tamaño del espacio de acción
num_episodios = 100
num_acciones = env.action_space.n

# Inicializamos la tabla de valores Q con ceros
Q = np.zeros((env.observation_space.shape[0], num_acciones))

# Definimos la tasa de aprendizaje y el factor de descuento
alpha = 0.1
gamma = 0.99

# Iteramos sobre cada episodio
for episodio in range(num_episodios):
    estado = env.reset()  # Reseteamos el entorno para cada episodio
    done = False  # Bandera para indicar si el episodio ha terminado
    
    # Iteramos hasta que el episodio termine
    while not done:
        # Elegimos una acción aleatoria
        accion = env.action_space.sample()
        
        # Ejecutamos la acción en el entorno
        siguiente_estado, recompensa, done, _ = env.step(accion)
        
        # Actualizamos el valor Q para la acción realizada utilizando la fórmula de actualización Q-learning
        Q[estado, accion] = (1 - alpha) * Q[estado, accion] + alpha * (recompensa + gamma * np.max(Q[siguiente_estado]))
        
        estado = siguiente_estado  # Actualizamos el estado actual para la siguiente iteración

# Imprimimos la tabla de valores Q al final del aprendizaje
print("Tabla de valores Q al final del aprendizaje:")
print(Q)
