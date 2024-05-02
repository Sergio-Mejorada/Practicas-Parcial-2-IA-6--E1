#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 92
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


import numpy as np

# Definir la longitud de los eslabones del robot
l1 = 5  # Longitud del primer eslabón en unidades
l2 = 4  # Longitud del segundo eslabón en unidades

def cinematica_inversa(x, y):
    # Calcular la cinemática inversa para el robot de 2-DOF
    # x, y son las coordenadas del extremo efector deseado
    
    # Calcular el ángulo del primer eslabón (theta1)
    cos_theta1 = (x**2 + y**2 - l1**2 - l2**2) / (2 * l1 * l2)
    sin_theta1 = np.sqrt(1 - cos_theta1**2)
    theta1 = np.arctan2(sin_theta1, cos_theta1)
    
    # Calcular el ángulo del segundo eslabón (theta2)
    cos_theta2 = (x**2 + y**2 - l1**2 - l2**2) / (2 * l1 * l2)
    sin_theta2 = np.sqrt(1 - cos_theta2**2)
    theta2 = np.arctan2(sin_theta2, cos_theta2)
    
    return np.degrees(theta1), np.degrees(theta2)  # Devolver ángulos en grados

# Coordenadas del extremo efector deseado
x_deseado = 7
y_deseado = 6

# Calcular la cinemática inversa para las coordenadas deseadas
theta1_resultado, theta2_resultado = cinematica_inversa(x_deseado, y_deseado)

# Mostrar los resultados de la cinemática inversa
print(f"Ángulo del primer eslabón (theta1): {theta1_resultado} grados")
print(f"Ángulo del segundo eslabón (theta2): {theta2_resultado} grados")
