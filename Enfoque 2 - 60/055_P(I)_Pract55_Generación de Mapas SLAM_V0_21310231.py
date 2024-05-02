#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 90
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


import numpy as np
import matplotlib.pyplot as plt

# Definir la clase del filtro de Kalman extendido (EKF)
class EKF_SLAM:
    def __init__(self, x, P, Q, R):
        self.x = x  # Estado inicial (posición y orientación)
        self.P = P  # Matriz de covarianza inicial
        self.Q = Q  # Covarianza del proceso
        self.R = R  # Covarianza de la medición
    
    def prediction(self, u):
        # Predicción del estado utilizando el modelo de movimiento del robot
        # Aquí asumimos un modelo de movimiento simple
        self.x = self.x + u
        # Actualizar la matriz de covarianza de la predicción
        self.P = self.P + self.Q
        return self.x, self.P
    
    def update(self, z):
        # Actualización del estado basada en la medición
        # z es la medición (puntos de referencia detectados por sensores)
        # Aquí asumimos un modelo de medición simple
        H = np.eye(len(z))  # Matriz de medición
        K = self.P.dot(H.T).dot(np.linalg.inv(H.dot(self.P).dot(H.T) + self.R))  # Ganancia de Kalman
        self.x = self.x + K.dot(z - H.dot(self.x))  # Actualizar el estado
        self.P = (np.eye(len(self.x)) - K.dot(H)).dot(self.P)  # Actualizar la matriz de covarianza
        return self.x, self.P

# Parámetros del filtro de Kalman extendido
x_init = np.array([0, 0, 0])  # Estado inicial (x, y, orientación)
P_init = np.eye(len(x_init))  # Matriz de covarianza inicial
Q = np.eye(len(x_init)) * 0.1  # Covarianza del proceso
R = np.eye(2) * 0.1  # Covarianza de la medición (asumimos mediciones 2D)

# Inicializar el filtro de Kalman extendido para SLAM
ekf_slam = EKF_SLAM(x_init, P_init, Q, R)

# Simular la secuencia de movimientos y mediciones
movimientos = np.array([[1, 0, 0], [0, 1, np.pi/2], [1, 0, 0], [0, 1, np.pi/2]])  # Movimientos del robot
mediciones = np.array([[1, 1], [1, 2], [2, 2], [2, 1]])  # Mediciones de puntos de referencia

# Ejecutar el algoritmo EKF-SLAM
mapa = []
for movimiento, medicion in zip(movimientos, mediciones):
    x_pred, P_pred = ekf_slam.prediction(movimiento)
    x_upd, P_upd = ekf_slam.update(medicion)
    mapa.append(x_upd[:2])  # Agregar la posición estimada al mapa

# Mostrar el mapa final
mapa = np.array(mapa)
plt.plot(mapa[:, 0], mapa[:, 1], marker='o')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Mapa generado por EKF-SLAM')
plt.grid(True)
plt.show()
