#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 38
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

from scipy.stats import norm

# Definir el valor medio y la desviación estándar de una distribución normal
mu = 0  # Valor medio
sigma = 1  # Desviación estándar

# Calcular la probabilidad de que un valor esté dentro de un rango específico
rango_inicio = -1
rango_fin = 1
probabilidad_incertidumbre = norm.cdf(rango_fin, mu, sigma) - norm.cdf(rango_inicio, mu, sigma)

print(f"La probabilidad de incertidumbre dentro del rango [{rango_inicio}, {rango_fin}] es: {probabilidad_incertidumbre}")

