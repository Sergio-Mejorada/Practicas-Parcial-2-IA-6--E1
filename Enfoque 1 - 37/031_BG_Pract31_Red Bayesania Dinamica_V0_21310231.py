#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 31
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

from pgmpy.models import DynamicBayesianNetwork as DBN
from pgmpy.factors.discrete import TabularCPD

# Creamos el modelo de la Red Bayesiana Dinámica (DBN)
dbn_model = DBN()

# Definimos los nodos de la DBN y sus posibles estados
nodos_temporales = ['t0', 't1', 't2']  # Ejemplo con 3 pasos temporales
nodos_estados = {'A': ['Alto', 'Bajo'],
                 'B': ['Alto', 'Bajo']}

# Añadimos los nodos al modelo DBN
for nodo in nodos_temporales:
    for variable, estados in nodos_estados.items():
        dbn_model.add_node(variable + '_' + nodo, state=estados)

# Definimos las Tablas de Probabilidad Condicional (CPDs) para cada nodo
cpd_a_t0 = TabularCPD(variable='A_t0', variable_card=2, 
                       values=[[0.6, 0.4]])
cpd_b_t0 = TabularCPD(variable='B_t0', variable_card=2, 
                       values=[[0.3, 0.7]])
cpd_a_t1 = TabularCPD(variable='A_t1', variable_card=2, 
                       values=[[0.7, 0.3],
                               [0.4, 0.6]],
                       evidence=['A_t0'], evidence_card=[2])
cpd_b_t1 = TabularCPD(variable='B_t1', variable_card=2, 
                       values=[[0.5, 0.5],
                               [0.2, 0.8]],
                       evidence=['B_t0'], evidence_card=[2])
cpd_a_t2 = TabularCPD(variable='A_t2', variable_card=2, 
                       values=[[0.8, 0.2],
                               [0.1, 0.9]],
                       evidence=['A_t1'], evidence_card=[2])
cpd_b_t2 = TabularCPD(variable='B_t2', variable_card=2, 
                       values=[[0.9, 0.1],
                               [0.6, 0.4]],
                       evidence=['B_t1'], evidence_card=[2])

# Añadimos las CPDs al modelo DBN
dbn_model.add_cpds(cpd_a_t0, cpd_b_t0, cpd_a_t1, cpd_b_t1, cpd_a_t2, cpd_b_t2)

# Verificamos si el modelo es válido
print("El modelo es válido:", dbn_model.check_model())
