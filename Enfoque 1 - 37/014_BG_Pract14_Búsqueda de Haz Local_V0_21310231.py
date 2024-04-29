#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 13
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import random

def local_beam_search(funcion_objetivo, num_haces=5, ancho_haz=3, iteraciones_maximas=1000):
    # Búsqueda de Haz Local (Local Beam Search)
    haces = [random.uniform(-10, 10) for _ in range(num_haces)]  # Haces iniciales aleatorios
    mejores_haces = haces[:]  # Copia de los mejores haces
    mejor_valor = min(funcion_objetivo(h) for h in haces)  # Mejor valor encontrado
    
    for _ in range(iteraciones_maximas):
        nuevos_haces = []  # Nuevos haces generados en esta iteración
        
        for haz in haces:
            vecinos = [haz + random.uniform(-0.1, 0.1) for _ in range(ancho_haz)]  # Genera vecinos aleatorios
            nuevos_haces.extend(vecinos)
        
        nuevos_haces.sort(key=lambda x: funcion_objetivo(x))  # Ordena los nuevos haces por valor de la función objetivo
        
        mejores_haces = nuevos_haces[:num_haces]  # Selecciona los mejores haces
        mejor_valor = min(funcion_objetivo(h) for h in mejores_haces)  # Mejor valor encontrado
        
        haces = mejores_haces[:]  # Actualiza los haces para la siguiente iteración
    
    return mejores_haces[0], mejor_valor

# Función objetivo de ejemplo (función cuadrática)
def funcion_objetivo(x):
    return x**2

# Ejecutar Búsqueda de Haz Local
mejor_estado, mejor_valor = local_beam_search(funcion_objetivo)
print("Mejor estado encontrado:", mejor_estado)
print("Valor mínimo encontrado:", mejor_valor)

