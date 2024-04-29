#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 64
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


pip install hmmlearn


import numpy as np
from hmmlearn import hmm

# Definir los estados ocultos del HMM y los posibles valores observados
estados_ocultos = ['soleado', 'nublado', 'lluvioso']
valores_observados = ['caminar', 'comer', 'dormir']

# Crear matrices de transición y de emisión (probabilidades iniciales)
matriz_transicion = np.array([[0.7, 0.2, 0.1],
                               [0.3, 0.5, 0.2],
                               [0.4, 0.4, 0.2]])

matriz_emision = np.array([[0.1, 0.4, 0.5],
                            [0.6, 0.3, 0.1],
                            [0.3, 0.3, 0.4]])

prob_inicial = np.array([0.3, 0.4, 0.3])

# Crear y entrenar el modelo HMM
modelo_hmm = hmm.MultinomialHMM(n_components=len(estados_ocultos))
modelo_hmm.startprob_ = prob_inicial
modelo_hmm.transmat_ = matriz_transicion
modelo_hmm.emissionprob_ = matriz_emision

# Generar secuencia de observaciones
np.random.seed(0)
observaciones, estados = modelo_hmm.sample(n_samples=10, random_state=0)

# Ajustar el modelo HMM a las observaciones
modelo_hmm.fit(observaciones)

# Predecir la secuencia de estados ocultos
secuencia_estados = modelo_hmm.predict(observaciones)

# Imprimir resultados
print("Secuencia de observaciones:", [valores_observados[i] for i in observaciones])
print("Secuencia de estados ocultos predicha:", [estados_ocultos[i] for i in secuencia_estados])
