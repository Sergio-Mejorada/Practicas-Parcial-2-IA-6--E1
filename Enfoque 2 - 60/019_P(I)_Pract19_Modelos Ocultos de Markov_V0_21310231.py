#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 56
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


from hmmlearn import hmm
import numpy as np

# Definir el modelo oculto de Markov
model = hmm.MultinomialHMM(n_components=2, n_iter=100)

# Datos de entrenamiento
secuencias_observaciones = [[0, 1, 0, 1, 0], [1, 0, 1, 0, 1]]
longitudes_secuencias = [len(seq) for seq in secuencias_observaciones]
observaciones = np.concatenate(secuencias_observaciones)

# Entrenar el modelo
model.fit(observaciones.reshape(-1, 1), longitudes_secuencias)

# Generar una secuencia de estados y observaciones
longitud_generacion = 10
secuencia_generada, estados_generados = model.sample(longitud_generacion)

print("Secuencia de observaciones generada:", secuencia_generada.flatten())
print("Secuencia de estados generada:", estados_generados.flatten())
