#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 46
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

# Obtener el Manto de Markov del nodo 'C'
manto_markov = inferencia.markov_blanket('C')

# Imprimir el Manto de Markov
print("El Manto de Markov del nodo 'C' es:", manto_markov)
