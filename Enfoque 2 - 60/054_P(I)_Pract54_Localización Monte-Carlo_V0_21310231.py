#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 89
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


import random

# Definir la posición inicial y el número de partículas
posicion_real = 5  # Supongamos que el robot está inicialmente en la posición 5
num_particulas = 100

# Crear una lista de partículas con posiciones aleatorias
particulas = [random.randint(1, 10) for _ in range(num_particulas)]

def movimiento(robot_pos, sigma=1):
    # Simular el movimiento del robot añadiendo ruido gaussiano
    return robot_pos + random.gauss(0, sigma)

def medicion(posicion_real, sigma=1):
    # Simular la medición del sensor con ruido gaussiano
    return posicion_real + random.gauss(0, sigma)

def actualizar_particulas(medicion_observada):
    # Actualizar las partículas basadas en la medición observada
    pesos = [1.0 / (abs(p - medicion_observada) + 1) for p in particulas]
    pesos_normalizados = [p / sum(pesos) for p in pesos]
    particulas_actualizadas = random.choices(particulas, weights=pesos_normalizados, k=num_particulas)
    return particulas_actualiza
