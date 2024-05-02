#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 111
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

pip install aima-python


from aima.logic import *

# Definir un modelo para la lógica proposicional
p = Symbol('P')
q = Symbol('Q')

# Definir una fórmula lógica
formula = And(p, q)

# Definir un agente lógico
class LogicalAgent:
    def __init__(self, model):
        self.model = model
    
    def evaluate(self, formula):
        return pl_true(formula, self.model)

# Crear un agente lógico con un modelo específico
agent = LogicalAgent({p: True, q: False})

# Evaluar la fórmula lógica con el agente
resultado = agent.evaluate(formula)

# Mostrar el resultado
print("La fórmula es verdadera:", resultado)
