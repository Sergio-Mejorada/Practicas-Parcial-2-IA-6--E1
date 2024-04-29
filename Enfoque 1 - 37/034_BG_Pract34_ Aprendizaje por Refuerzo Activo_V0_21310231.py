#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 34
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

# Definimos el factor de exploración ε para el método ε-Greedy
epsilon = 0.2

# Iteramos sobre cada episodio
for episodio in range(num_episodios):
    estado = env.reset()  # Reseteamos el entorno para cada episodio
    done = False  # Bandera para indicar si el episodio ha terminado
    
    # Iteramos hasta que el episodio termine
    while not done:
        # Aplicamos el método ε-Greedy para elegir una acción
        if np.random.uniform(0, 1) < epsilon:
            # Exploración: elegimos una acción aleatoria
            accion = env.action_space.sample()
        else:
            # Explotación: elegimos la acción con el mayor valor Q para el estado actual
            accion = np.argmax(Q[estado])
        
        # Ejecutamos la acción en el entorno
        siguiente_estado, recompensa, done, _ = env.step(accion)
        
        # Actualizamos el valor Q para la acción realizada
        mejor_accion_siguiente_estado = np.argmax(Q[siguiente_estado])
        Q[estado, accion] += 0.1 * (recompensa + Q[siguiente_estado, mejor_accion_siguiente_estado] - Q[estado, accion])
        
        estado = siguiente_estado  # Actualizamos el estado actual para la siguiente iteración

# Imprimimos la tabla de valores Q al final del aprendizaje
print("Tabla de valores Q al final del aprendizaje:")
print(Q)
