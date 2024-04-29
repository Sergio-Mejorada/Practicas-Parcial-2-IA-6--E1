#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 35
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import numpy as np
import gym

# Crear el entorno CartPole de OpenAI Gym
env = gym.make('CartPole-v1')

# Definir los parámetros del algoritmo Q-Learning
num_episodios = 1000  # Número de episodios de entrenamiento
num_pasos_max = 200  # Número máximo de pasos por episodio
tasa_aprendizaje = 0.2  # Tasa de aprendizaje (alpha)
factor_descuento = 0.9  # Factor de descuento (gamma)
epsilon = 0.2  # Factor de exploración epsilon-greedy

# Inicializar la tabla Q con ceros (dimensiones: espacio de observaciones x espacio de acciones)
num_observaciones = env.observation_space.shape[0]
num_acciones = env.action_space.n
Q = np.zeros((num_observaciones, num_acciones))

# Función para elegir una acción basada en la estrategia epsilon-greedy
def elegir_accion(estado):
    if np.random.uniform(0, 1) < epsilon:
        return env.action_space.sample()  # Acción aleatoria para exploración
    else:
        return np.argmax(Q[estado])  # Acción según el valor Q máximo para explotación

# Entrenamiento mediante Q-Learning
for episodio in range(num_episodios):
    estado_actual = env.reset()  # Reiniciar el entorno y obtener el estado inicial
    
    for paso in range(num_pasos_max):
        accion = elegir_accion(estado_actual)  # Elegir una acción para el estado actual
        
        # Ejecutar la acción y obtener el siguiente estado, la recompensa, y si el episodio ha terminado
        siguiente_estado, recompensa, done, _ = env.step(accion)
        
        # Actualizar el valor Q para la acción tomada
        mejor_valor_siguiente_estado = np.max(Q[siguiente_estado])
        Q[estado_actual][accion] += tasa_aprendizaje * (recompensa + factor_descuento * mejor_valor_siguiente_estado - Q[estado_actual][accion])
        
        estado_actual = siguiente_estado  # Actualizar el estado actual
        
        if done:
            break  # Salir del bucle si el episodio ha terminado
    
    # Imprimir información sobre el episodio actual
    if episodio % 100 == 0:
        print(f"Episodio {episodio}: Duración = {paso+1}")

# Imprimir la tabla Q al final del entrenamiento
print("\nTabla Q final:")
print(Q)
