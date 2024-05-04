#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 129
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


pip install numpy


import numpy as np

def modelo_probabilista_racional(probabilidad_lluvia, umbral_decision):
    if probabilidad_lluvia >= umbral_decision:
        decision = "Llevar un paraguas"
    else:
        decision = "No llevar un paraguas"
    return decision

# Ejemplo de uso
probabilidad_lluvia = 0.7
umbral_decision = 0.5

decision = modelo_probabilista_racional(probabilidad_lluvia, umbral_decision)
print("Probabilidad de lluvia:", probabilidad_lluvia)
print("Umbral de decisión:", umbral_decision)
print("Decisión:", decision)
