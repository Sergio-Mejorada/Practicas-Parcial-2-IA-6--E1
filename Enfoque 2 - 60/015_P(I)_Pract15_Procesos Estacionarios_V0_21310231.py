#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 52
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


import numpy as np
import matplotlib.pyplot as plt

# Definir el número de muestras y el rango de tiempo
num_muestras = 1000
tiempo = np.arange(num_muestras)

# Generar ruido blanco como un proceso estacionario débil
ruido_blanco = np.random.normal(loc=0, scale=1, size=num_muestras)

# Graficar el proceso estacionario (ruido blanco)
plt.figure(figsize=(10, 5))
plt.plot(tiempo, ruido_blanco)
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.title('Proceso Estacionario Débil (Ruido Blanco)')
plt.grid(True)
plt.show()

