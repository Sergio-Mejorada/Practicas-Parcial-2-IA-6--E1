#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 127
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import numpy as np

def calcular_incertidumbre(valores):
    media = np.mean(valores)
    varianza = np.var(valores)
    desviacion_estandar = np.sqrt(varianza)
    return media, desviacion_estandar

def calcular_factores_certeza(valores, incertidumbre):
    factores = []
    for valor in valores:
        factor = np.exp(-0.5 * ((valor - incertidumbre[0]) / incertidumbre[1])**2)
        factores.append(factor)
    return factores

# Ejemplo de uso
datos = [10, 12, 15, 14, 17]
media, desviacion_estandar = calcular_incertidumbre(datos)
factores = calcular_factores_certeza(datos, (media, desviacion_estandar))

print("Media:", media)
print("Desviación estándar:", desviacion_estandar)
print("Factores de certeza:", factores)
