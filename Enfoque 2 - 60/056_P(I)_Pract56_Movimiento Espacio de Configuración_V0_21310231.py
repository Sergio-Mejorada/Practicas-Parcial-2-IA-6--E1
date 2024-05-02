#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 91
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


import numpy as np
import matplotlib.pyplot as plt

# Definir el tamaño del entorno
tamano_entorno = (10, 10)  # Ancho y alto del entorno en unidades

# Crear un mapa del entorno (0: espacio libre, 1: obstáculo)
mapa = np.zeros(tamano_entorno)
mapa[2:8, 3:7] = 1  # Definir un obstáculo en el mapa

# Definir las posiciones inicial y final del robot
posicion_inicial = (1, 1)
posicion_final = (9, 9)

# Mostrar el entorno y las posiciones inicial y final
plt.imshow(mapa, cmap='gray', origin='lower')
plt.plot(posicion_inicial[0], posicion_inicial[1], 'go', label='Posición inicial')
plt.plot(posicion_final[0], posicion_final[1], 'ro', label='Posición final')
plt.legend()
plt.title('Espacio de Configuración')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
