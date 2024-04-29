#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 57
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

from filterpy.kalman import KalmanFilter
import numpy as np
import matplotlib.pyplot as plt

# Crear un filtro de Kalman
kf = KalmanFilter(dim_x=2, dim_z=1)

# Definir las matrices de transición y de observación
kf.F = np.array([[1., 1.],  # Matriz de transición de estado
                 [0., 1.]])
kf.H = np.array([[1., 0.]])  # Matriz de observación

# Definir la covarianza del proceso y del ruido de medición
kf.P *= 1000.0  # Covarianza de la estimación inicial
kf.R = 5.0      # Covarianza del ruido de medición
kf.Q = np.array([[0.1, 0.],  # Covarianza del ruido del proceso
                 [0., 0.01]])

# Simular datos sintéticos
np.random.seed(0)
num_muestras = 50
tiempo = np.arange(num_muestras)
posicion_real = 0.1 * tiempo**2 + 5 * tiempo  # Trayectoria cuadrática
mediciones = posicion_real + np.random.normal(0, 10, num_muestras)  # Agregar ruido a las mediciones

# Inicializar el filtro de Kalman con la posición inicial y velocidad inicial
kf.x = np.array([[0.], [0.]])  # [posición, velocidad]

# Lista para almacenar las estimaciones de posición
estimaciones_posicion = []

# Aplicar el filtro de Kalman a cada muestra
for medicion in mediciones:
    kf.predict()  # Predicción del siguiente estado
    kf.update(medicion)  # Actualización con la nueva medición
    estimaciones_posicion.append(kf.x[0, 0])  # Estimación de la posición

# Graficar resultados
plt.figure(figsize=(10, 6))
plt.plot(tiempo, posicion_real, label='Posición Real')
plt.plot(tiempo, mediciones, label='Mediciones (con ruido)')
plt.plot(tiempo, estimaciones_posicion, label='Estimaciones de Posición')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.title('Filtro de Kalman - Estimación de Posición')
plt.legend()
plt.grid(True)
plt.show()

