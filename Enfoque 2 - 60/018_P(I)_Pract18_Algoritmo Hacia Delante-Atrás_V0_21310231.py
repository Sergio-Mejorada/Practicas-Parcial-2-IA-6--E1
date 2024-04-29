#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 55
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())



import numpy as np

def forward_backward(observaciones, transiciones, emisiones, estado_inicial):
    num_estados = len(estado_inicial)
    num_observaciones = len(observaciones)
    
    # Paso hacia adelante (forward)
    forward = np.zeros((num_estados, num_observaciones))
    forward[:, 0] = estado_inicial * emisiones[:, observaciones[0]]
    
    for t in range(1, num_observaciones):
        for s in range(num_estados):
            forward[s, t] = emisiones[s, observaciones[t]] * np.sum(forward[:, t-1] * transiciones[:, s])
    
    # Paso hacia atrás (backward)
    backward = np.zeros((num_estados, num_observaciones))
    backward[:, -1] = 1.0
    
    for t in reversed(range(num_observaciones-1)):
        for s in range(num_estados):
            backward[s, t] = np.sum(backward[:, t+1] * transiciones[s, :] * emisiones[:, observaciones[t+1]])
    
    # Calcular la distribución posterior
    posterior = forward * backward / np.sum(forward * backward, axis=0)
    
    return posterior

# Ejemplo de uso
observaciones = [0, 1, 0]  # Secuencia de observaciones
transiciones = np.array([[0.7, 0.3],  # Matriz de transiciones
                          [0.4, 0.6]])
emisiones = np.array([[0.9, 0.1],  # Matriz de emisiones
                      [0.2, 0.8]])
estado_inicial = np.array([0.5, 0.5])  # Distribución inicial de estados

posterior = forward_backward(observaciones, transiciones, emisiones, estado_inicial)
print("Distribución posterior de los estados ocultos:")
print(posterior)

