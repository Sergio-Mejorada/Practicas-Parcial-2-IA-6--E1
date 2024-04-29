#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 50
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


from pgmpy.models import BayesianModel
from pgmpy.sampling import BayesianModelSampling
from pgmpy.inference import VariableElimination

# Definir la estructura de la Red Bayesiana
red_bayesiana = BayesianModel([('A', 'C'), ('B', 'C'), ('C', 'D'), ('C', 'E'), ('D', 'F'), ('E', 'F')])

# Crear un objeto para realizar inferencia en la red
inferencia = VariableElimination(red_bayesiana)

# Definir la evidencia observada en la red
evidencia = {'A': 0, 'B': 1}

# Realizar inferencia para calcular la verosimilitud de la evidencia observada
verosimilitud_evidencia = inferencia.query(variables=['A', 'B'], evidence=evidencia)

# Crear un objeto para realizar muestreo directo en la red
muestreo_directo = BayesianModelSampling(red_bayesiana)

# Generar muestras aleatorias de la red
muestras_directas = muestreo_directo.forward_sample(size=1000)

# Calcular la verosimilitud de las muestras generadas
verosimilitud_muestras = len(muestras_directas[(muestras_directas['A'] == 0) & (muestras_directas['B'] == 1)]) / 1000

# Calcular la ponderación de verosimilitud
ponderacion_verosimilitud = verosimilitud_evidencia.values[0] / verosimilitud_muestras

# Imprimir la ponderación de verosimilitud
print("Ponderación de Verosimilitud:", ponderacion_verosimilitud)


