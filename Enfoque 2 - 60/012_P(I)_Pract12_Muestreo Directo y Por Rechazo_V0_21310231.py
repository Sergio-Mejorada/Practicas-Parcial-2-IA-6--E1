#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 49
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


from pgmpy.inference import VariableElimination
from pgmpy.sampling import RejectionSampling

# Definir la estructura de la Red Bayesiana
red_bayesiana = BayesianModel([('A', 'C'), ('B', 'C'), ('C', 'D'), ('C', 'E'), ('D', 'F'), ('E', 'F')])

# Crear un objeto para realizar inferencia en la red
inferencia = VariableElimination(red_bayesiana)

# Definir la evidencia observada en la red
evidencia = {'A': 0, 'B': 1}

# Crear un objeto para realizar muestreo por rechazo en la red
muestreo_rechazo = RejectionSampling(red_bayesiana)

# Generar muestras aleatorias utilizando muestreo por rechazo
muestras_rechazo = muestreo_rechazo.forward_sample(size=1000, evidence=evidencia)

# Imprimir algunas de las muestras generadas
print("Muestras generadas mediante muestreo por rechazo:")
print(muestras_rechazo.head())


from pgmpy.inference import VariableElimination
from pgmpy.sampling import RejectionSampling

# Definir la estructura de la Red Bayesiana
red_bayesiana = BayesianModel([('A', 'C'), ('B', 'C'), ('C', 'D'), ('C', 'E'), ('D', 'F'), ('E', 'F')])

# Crear un objeto para realizar inferencia en la red
inferencia = VariableElimination(red_bayesiana)

# Definir la evidencia observada en la red
evidencia = {'A': 0, 'B': 1}

# Crear un objeto para realizar muestreo por rechazo en la red
muestreo_rechazo = RejectionSampling(red_bayesiana)

# Generar muestras aleatorias utilizando muestreo por rechazo
muestras_rechazo = muestreo_rechazo.forward_sample(size=1000, evidence=evidencia)

# Imprimir algunas de las muestras generadas
print("Muestras generadas mediante muestreo por rechazo:")
print(muestras_rechazo.head())
