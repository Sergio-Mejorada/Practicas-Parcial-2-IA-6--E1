#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 62
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import numpy as np

# Generar datos de ejemplo con dos distribuciones gaussianas
np.random.seed(0)
mu1, sigma1 = 0, 1
mu2, sigma2 = 5, 1
n_muestras = 100
X = np.concatenate([np.random.normal(mu1, sigma1, n_muestras),
                     np.random.normal(mu2, sigma2, n_muestras)])

# Inicializar los parámetros iniciales de las distribuciones
mu_estimado1, sigma_estimado1 = -1, 1
mu_estimado2, sigma_estimado2 = 1, 1
p1 = 0.5
p2 = 0.5

# Implementar el algoritmo EM
n_iteraciones = 100
for _ in range(n_iteraciones):
    # Paso de expectación (E-step): calcular las probabilidades de pertenencia a cada componente
    gamma1 = p1 * np.exp(-0.5 * ((X - mu_estimado1) / sigma_estimado1)**2)  # Probabilidad de pertenecer a la primera componente
    gamma2 = p2 * np.exp(-0.5 * ((X - mu_estimado2) / sigma_estimado2)**2)  # Probabilidad de pertenecer a la segunda componente
    total_gamma = gamma1 + gamma2
    gamma1 /= total_gamma  # Normalizar las probabilidades
    gamma2 /= total_gamma
    
    # Paso de maximización (M-step): actualizar los parámetros
    n1 = np.sum(gamma1)  # Número de muestras en la primera componente
    n2 = np.sum(gamma2)  # Número de muestras en la segunda componente
    
    mu_estimado1 = np.sum(gamma1 * X) / n1  # Media estimada de la primera componente
    mu_estimado2 = np.sum(gamma2 * X) / n2  # Media estimada de la segunda componente
    
    sigma_estimado1 = np.sqrt(np.sum(gamma1 * (X - mu_estimado1)**2) / n1)  # Desviación estándar estimada de la primera componente
    sigma_estimado2 = np.sqrt(np.sum(gamma2 * (X - mu_estimado2)**2) / n2)  # Desviación estándar estimada de la segunda componente
    
    p1 = n1 / (n1 + n2)  # Proporción de muestras en la primera componente
    p2 = n2 / (n1 + n2)  # Proporción de muestras en la segunda componente

print("Parámetros estimados de la primera componente:")
print("Media:", mu_estimado1)
print("Desviación estándar:", sigma_estimado1)
print("Proporción:", p1)
print("\nParámetros estimados de la segunda componente:")
print("Media:", mu_estimado2)
print("Desviación estándar:", sigma_estimado2)
print("Proporción:", p2)
