#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 54
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


from filterpy.kalman import KalmanFilter
import numpy as np
import matplotlib.pyplot as plt

# Definir el filtro de Kalman
kalman_filter = KalmanFilter(dim_x=2, dim_z=1)

# Inicializar la matriz de estado y la matriz de observación
kalman_filter.x = np.array([[0.0],   # Posición inicial
                             [0.0]])  # Velocidad inicial

kalman_filter.F = np.array([[1.0, 1.0],  # Matriz de transición de estado
                             [0.0, 1.0]])

kalman_filter.H = np.array([[1.0, 0.0]])  # Matriz de observación

kalman_filter.P *= 1000.0  # Covarianza de la estimación inicial
kalman_filter.R = 5.0       # Covarianza del ruido de medición
kalman_filter.Q = np.array([[0.1, 0.0],  # Covarianza del ruido de proceso
                             [0.0, 0.01]])

# Generar datos sintéticos para la prueba
np.random.seed(123)
num_muestras = 50
tiempo = np.arange(num_muestras)
posicion_real = 0.1 * tiempo**2 + 5 * tiempo  # Trayectoria cuadrática
mediciones = posicion_real + np.random.normal(0, 10, num_muestras)  # Agregar ruido a las mediciones

# Filtrado y predicción utilizando el filtro de Kalman
predicciones = []
estimaciones = []
for medicion in mediciones:
    kalman_filter.predict()
    kalman_filter.update(medicion)
    predicciones.append(kalman_filter.x[0, 0])  # Posición predicha
    estimaciones.append(kalman_filter.x[1, 0])  # Velocidad estimada

# Graficar resultados
plt.figure(figsize=(10, 6))
plt.plot(tiempo, posicion_real, label='Posición Real')
plt.plot(tiempo, mediciones, label='Mediciones (con ruido)')
plt.plot(tiempo, predicciones, label='Predicciones')
plt.plot(tiempo, estimaciones, label='Estimaciones')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.title('Filtrado, Predicción y Estimación con Filtro de Kalman')
plt.legend()
plt.grid(True)
plt.show()
