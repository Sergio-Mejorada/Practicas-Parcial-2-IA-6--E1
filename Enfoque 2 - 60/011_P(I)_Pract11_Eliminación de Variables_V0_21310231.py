#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 48
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination

# Definir la estructura de la Red Bayesiana
red_bayesiana = BayesianModel([('A', 'C'), ('B', 'C'), ('C', 'D'), ('C', 'E'), ('D', 'F'), ('E', 'F')])

# Crear un objeto para realizar inferencia en la red
inferencia = VariableElimination(red_bayesiana)

# Definir la evidencia observada en la red
evidencia = {'A': 0, 'B': 1}

# Realizar inferencia por eliminación de variables para calcular P(D|A=0, B=1)
resultado_inferencia = inferencia.query(variables=['D'], evidence=evidencia, elimination_order=['C'])

# Imprimir el resultado de la inferencia
print("Resultado de la inferencia por eliminación de variables:")
print(resultado_inferencia)
