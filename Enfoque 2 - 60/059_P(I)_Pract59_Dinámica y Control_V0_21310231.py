#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 94
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import numpy as np
import matplotlib.pyplot as plt

# Parámetros del péndulo invertido
m = 1  # Masa del péndulo en kg
l = 1  # Longitud del péndulo en metros
g = 9.81  # Aceleración gravitacional en m/s^2
dt = 0.01  # Paso de tiempo en segundos
t_final = 10  # Tiempo final de simulación en segundos

# Condiciones iniciales
theta_0 = np.pi / 4  # Ángulo inicial en radianes
theta_dot_0 = 0  # Velocidad angular inicial en radianes por segundo

# Control proporcional-derivativo (PD)
Kp = 100  # Ganancia proporcional
Kd = 10  # Ganancia derivativa

# Listas para almacenar datos de la simulación
t_sim = np.arange(0, t_final, dt)
theta_sim = []
theta_dot_sim = []
theta_desired = np.zeros_like(t_sim)  # Ángulo deseado (vertical)

# Simulación de la dinámica y el control del péndulo
theta = theta_0
theta_dot = theta_dot_0
for t in t_sim:
    # Calcular el error de seguimiento
    error = theta_desired[int(t/dt)] - theta
    
    # Calcular el control PD
    control = Kp * error + Kd * theta_dot
    
    # Calcular las aceleraciones angular y lineal
    theta_dot_dot = (-m * g * l * np.sin(theta) + control) / (m * l**2)
    
    # Integrar las ecuaciones de la dinámica
    theta_dot += theta_dot_dot * dt
    theta += theta_dot * dt
    
    # Almacenar los resultados de la simulación
    theta_sim.append(theta)
    theta_dot_sim.append(theta_dot)

# Visualizar los resultados de la simulación
plt.figure(figsize=(10, 6))
plt.plot(t_sim, theta_sim, label='Ángulo')
plt.plot(t_sim, theta_dot_sim, label='Velocidad Angular')
plt.plot(t_sim, theta_desired, '--', label='Ángulo Deseado', color='red')
plt.xlabel('Tiempo (s)')
plt.ylabel('Valor')
plt.title('Simulación de Dinámica y Control del Péndulo Invertido')
plt.legend()
plt.grid(True)
plt.show()
