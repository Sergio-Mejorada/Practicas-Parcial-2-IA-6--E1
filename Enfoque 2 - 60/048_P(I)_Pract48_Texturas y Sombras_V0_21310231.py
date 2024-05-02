#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 84
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter

# Crear una imagen de ejemplo (en este caso, un círculo blanco sobre fondo negro)
dimensiones = 100
imagen = np.zeros((dimensiones, dimensiones))
centro = (dimensiones // 2, dimensiones // 2)
radio = dimensiones // 4
y, x = np.ogrid[-centro[0]:dimensiones - centro[0], -centro[1]:dimensiones - centro[1]]
mascara_circulo = x**2 + y**2 <= radio**2
imagen[mascara_circulo] = 1

# Aplicar un filtro de suavizado (textura)
imagen_textura = gaussian_filter(imagen, sigma=3)

# Crear una imagen de sombra con un degradado de color
imagen_sombra = np.zeros((dimensiones, dimensiones, 3))
gradiente = np.linspace(0, 1, dimensiones)
imagen_sombra[:, :, 0] = gradiente[:, np.newaxis]
imagen_sombra[:, :, 1] = gradiente[:, np.newaxis]
imagen_sombra[:, :, 2] = gradiente[:, np.newaxis]

# Combinar la imagen original con la textura y la sombra
imagen_final = imagen + imagen_textura * 0.5 - imagen_sombra * 0.2
imagen_final = np.clip(imagen_final, 0, 1)  # Asegurar que los valores estén en el rango [0, 1]

# Mostrar las imágenes
plt.figure(figsize=(10, 4))

plt.subplot(1, 4, 1)
plt.imshow(imagen, cmap='gray')
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(1, 4, 2)
plt.imshow(imagen_textura, cmap='gray')
plt.title('Textura')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.imshow(imagen_sombra)
plt.title('Sombra')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.imshow(imagen_final, cmap='gray')
plt.title('Imagen Final')
plt.axis('off')

plt.tight_layout()
plt.show()
