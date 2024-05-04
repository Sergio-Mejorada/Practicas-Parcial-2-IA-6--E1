#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 119
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

pip install scikit-fuzzy


import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Crear variables de entrada y salida
temperatura = ctrl.Antecedent(np.arange(0, 101, 1), 'temperatura')
velocidad = ctrl.Antecedent(np.arange(0, 101, 1), 'velocidad')
flujo = ctrl.Consequent(np.arange(0, 101, 1), 'flujo')

# Definir funciones de membresía
temperatura['baja'] = fuzz.trimf(temperatura.universe, [0, 0, 50])
temperatura['media'] = fuzz.trimf(temperatura.universe, [20, 50, 80])
temperatura['alta'] = fuzz.trimf(temperatura.universe, [50, 100, 100])

velocidad['baja'] = fuzz.trimf(velocidad.universe, [0, 0, 50])
velocidad['media'] = fuzz.trimf(velocidad.universe, [20, 50, 80])
velocidad['alta'] = fuzz.trimf(velocidad.universe, [50, 100, 100])

flujo['bajo'] = fuzz.trimf(flujo.universe, [0, 0, 50])
flujo['medio'] = fuzz.trimf(flujo.universe, [20, 50, 80])
flujo['alto'] = fuzz.trimf(flujo.universe, [50, 100, 100])

# Visualizar las funciones de membresía
temperatura.view()
velocidad.view()
flujo.view()

# Crear reglas de inferencia
regla1 = ctrl.Rule(temperatura['baja'] & velocidad['baja'], flujo['bajo'])
regla2 = ctrl.Rule(temperatura['media'] & velocidad['media'], flujo['medio'])
regla3 = ctrl.Rule(temperatura['alta'] & velocidad['alta'], flujo['alto'])

# Crear el sistema de control
sistema_control = ctrl.ControlSystem([regla1, regla2, regla3])
simulador = ctrl.ControlSystemSimulation(sistema_control)

# Asignar valores de entrada
simulador.input['temperatura'] = 75
simulador.input['velocidad'] = 40

# Realizar la inferencia
simulador.compute()

# Obtener el resultado
print("Valor inferido para el flujo:", simulador.output['flujo'])
flujo.view(sim=simulador)
