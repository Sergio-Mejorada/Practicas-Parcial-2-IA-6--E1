#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 58
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import numpy as np
import matplotlib.pyplot as plt
from filterpy.monte_carlo import systematic_resample

# Definir la función de transición de estado
def transition_function(x, dt):
    return x + 2 * dt

# Definir la función de observación
def observation_function(x):
    return x + np.random.normal(0, 1)

# Configuración inicial del filtro de partículas
num_particulas = 1000
dt = 0.1
posicion_real = 0  # Posición inicial
varianza_proceso = 0.1
varianza_medicion = 1

# Generar partículas iniciales
particulas = np.random.normal(posicion_real, varianza_proceso, num_particulas)

# Lista para almacenar las estimaciones de posición
estimaciones_posicion = []

# Simular el proceso de filtrado de partículas
for _ in range(50):
    # Transición de estado (modelo del proceso)
    particulas = transition_function(particulas, dt) + np.random.normal(0, np.sqrt(varianza_proceso), num_particulas)
    
    # Observación (modelo de medición)
    observacion = observation_function(posicion_real) + np.random.normal(0, np.sqrt(varianza_medicion))
    
    # Actualizar pesos de las partículas basado en la observación
    likelihood = np.exp(-0.5 * ((particulas - observacion) / np.sqrt(varianza_medicion))**2)
    weights = likelihood / np.sum(likelihood)
    
    # Resampling (reemplazo sistemático)
    indices_resample = systematic_resample(weights)
    particulas = particulas[indices_resample]
    
    # Estimar la posición utilizando el promedio de las partículas
    estimacion_posicion = np.mean(particulas)
    estimaciones_posicion.append(estimacion_posicion)

# Graficar resultados
plt.figure(figsize=(10, 6))
plt.plot(range(50), estimaciones_posicion, label='Estimaciones de Posición')
plt.axhline(y=posicion_real, color='r', linestyle='--', label='Posición Real')
plt.xlabel('Tiempo')
plt.ylabel('Posición')
plt.title('Filtrado de Partículas - Estimación de Posición')
plt.legend()
plt.grid(True)
plt.show()
