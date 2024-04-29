#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 37
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import numpy as np

# Función para generar episodios (simulación de interacciones agente-entorno)
def generar_episodio(politica):
    estados = []
    acciones = []
    recompensas = []
    estado_actual = 0  # Estado inicial
    
    while True:
        accion = politica[estado_actual]
        nuevo_estado = estado_actual + accion  # Simulación de la transición de estado
        recompensa = 1 if nuevo_estado == 10 else 0  # Recompensa de 1 al llegar al estado objetivo
        
        estados.append(estado_actual)
        acciones.append(accion)
        recompensas.append(recompensa)
        
        estado_actual = nuevo_estado
        
        if nuevo_estado == 10:
            break  # Finalizar episodio al llegar al estado objetivo
    
    return estados, acciones, recompensas

# Algoritmo de búsqueda de política mediante Monte Carlo
def buscar_politica(num_episodios, num_estados, num_acciones):
    # Inicializar política aleatoria
    politica = np.random.randint(0, num_acciones, num_estados)
    
    # Inicializar tabla de valores de acción-estado y contador de visitas
    q_valores = np.zeros((num_estados, num_acciones))
    contador_visitas = np.zeros((num_estados, num_acciones))
    
    for _ in range(num_episodios):
        estados, acciones, recompensas = generar_episodio(politica)
        
        # Actualizar los valores Q y el contador de visitas
        retorno = 0
        for t in range(len(estados) - 1, -1, -1):  # Recorrer el episodio en reversa
            retorno = recompensas[t] + retorno
            estado = estados[t]
            accion = acciones[t]
            
            contador_visitas[estado][accion] += 1
            q_valores[estado][accion] += (retorno - q_valores[estado][accion]) / contador_visitas[estado][accion]
        
        # Actualizar la política basada en los valores Q actuales (greedy)
        politica = np.argmax(q_valores, axis=1)
    
    return politica

# Parámetros
num_episodios = 1000
num_estados = 11  # Estados 0 a 10
num_acciones = 2  # Acciones izquierda y derecha

# Ejecutar la búsqueda de política
politica_optima = buscar_politica(num_episodios, num_estados, num_acciones)
print("Política óptima encontrada:", politica_optima)
