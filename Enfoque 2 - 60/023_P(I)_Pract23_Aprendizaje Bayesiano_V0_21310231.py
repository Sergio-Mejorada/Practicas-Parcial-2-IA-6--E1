#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 60
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import numpy as np
import pymc3 as pm
import matplotlib.pyplot as plt

# Datos de ejemplo
np.random.seed(42)
datos = np.random.normal(5, 2, 100)

# Modelo Bayesiano
with pm.Model() as modelo_bayesiano:
    # Definir las distribuciones a priori para los parámetros
    media = pm.Normal('media', mu=0, sigma=10)
    desviacion_estandar = pm.HalfNormal('desviacion_estandar', sigma=10)
    
    # Definir la distribución likelihood (verosimilitud) con los datos observados
    observaciones = pm.Normal('observaciones', mu=media, sigma=desviacion_estandar, observed=datos)
    
    # Realizar la inferencia bayesiana
    traza = pm.sample(1000, tune=1000)

# Visualizar los resultados
pm.traceplot(traza)
plt.show()
