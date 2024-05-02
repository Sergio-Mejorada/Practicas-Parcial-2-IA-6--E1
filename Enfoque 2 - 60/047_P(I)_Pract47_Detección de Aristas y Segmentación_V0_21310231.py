#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 83
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
imagen = cv2.imread('ejemplo.jpg')

# Convertir la imagen a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar detección de bordes utilizando el operador Canny
bordes = cv2.Canny(gris, 100, 200)

# Aplicar segmentación utilizando la función findContours
contornos, _ = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujar los contornos en la imagen original
cv2.drawContours(imagen, contornos, -1, (0, 255, 0), 2)

# Mostrar la imagen con los bordes detectados y los contornos dibujados
plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
plt.title('Detección de Bordes y Segmentación')
plt.axis('off')
plt.show()
