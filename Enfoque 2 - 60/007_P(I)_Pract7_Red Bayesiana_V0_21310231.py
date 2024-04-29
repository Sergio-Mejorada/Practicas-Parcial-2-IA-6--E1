#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 44
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD

# Definir la estructura de la Red Bayesiana
red_bayesiana = BayesianModel([('D', 'G'), ('I', 'G'), ('G', 'L'), ('I', 'S')])

# Definir las Tablas de Probabilidad Condicional (CPDs)
cpd_d = TabularCPD(variable='D', variable_card=2, values=[[0.6], [0.4]])
cpd_i = TabularCPD(variable='I', variable_card=2, values=[[0.7], [0.3]])
cpd_g = TabularCPD(variable='G', variable_card=3, 
                    values=[[0.3, 0.05, 0.9,  0.5],
                            [0.4, 0.25, 0.08, 0.3],
                            [0.3, 0.7,  0.02, 0.2]],
                    evidence=['I', 'D'], evidence_card=[2, 2])
cpd_l = TabularCPD(variable='L', variable_card=2, 
                    values=[[0.1, 0.4, 0.99],
                            [0.9, 0.6, 0.01]],
                    evidence=['G'], evidence_card=[3])
cpd_s = TabularCPD(variable='S', variable_card=2, 
                    values=[[0.95, 0.2],
                            [0.05, 0.8]],
                    evidence=['I'], evidence_card=[2])

# Asociar las Tablas de Probabilidad Condicional (CPDs) con los nodos de la Red Bayesiana
red_bayesiana.add_cpds(cpd_d, cpd_i, cpd_g, cpd_l, cpd_s)

# Verificar si la Red Bayesiana es válida
es_valida = red_bayesiana.check_model()
print("¿Es la Red Bayesiana válida?", es_valida)

# Imprimir las Tablas de Probabilidad Condicional (CPDs) asociadas a cada nodo
for nodo in red_bayesiana.nodes():
    cpd = red_bayesiana.get_cpds(nodo)
    print(f"\nCPD para el nodo {nodo}:")
    print(cpd)

