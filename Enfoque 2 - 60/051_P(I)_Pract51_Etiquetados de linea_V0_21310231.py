#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 86
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


import cv2
import numpy as np

# Cargar una imagen
imagen = cv2.imread('imagen.jpg')

# Convertir la imagen a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar umbralización para obtener una imagen binaria
_, binaria = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Encontrar contornos en la imagen binaria
contornos, _ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Crear una copia de la imagen original para dibujar los contornos
imagen_contornos = imagen.copy()

# Dibujar los contornos encontrados en la copia de la imagen original
cv2.drawContours(imagen_contornos, contornos, -1, (0, 255, 0), 2)

# Mostrar la imagen original y la imagen con los contornos etiquetados
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen con Contornos Etiquetados', imagen_contornos)
cv2.waitKey(0)
cv2.destroyAllWindows()
