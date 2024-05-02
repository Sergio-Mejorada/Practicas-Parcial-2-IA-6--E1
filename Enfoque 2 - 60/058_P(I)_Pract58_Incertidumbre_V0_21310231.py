#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 93
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import numpy as np
import matplotlib.pyplot as plt

# Generar datos simulados con incertidumbre
np.random.seed(0)  # Fijar la semilla para reproducibilidad
datos_verdaderos = np.linspace(0, 10, 100)  # Datos verdaderos (0 a 10 con 100 puntos)
ruido = np.random.normal(0, 1, 100)  # Generar ruido gaussiano con media 0 y desviación estándar 1
datos_medidos = datos_verdaderos + ruido  # Datos medidos con ruido

# Visualizar los datos verdaderos y los datos medidos
plt.plot(datos_verdaderos, label='Datos Verdaderos')
plt.plot(datos_medidos, label='Datos Medidos con Ruido')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.legend()
plt.title('Simulación de Incertidumbre')
plt.grid(True)
plt.show()
