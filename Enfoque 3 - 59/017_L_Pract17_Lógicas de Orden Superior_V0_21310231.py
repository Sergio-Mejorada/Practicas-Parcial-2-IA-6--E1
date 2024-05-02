#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 112
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

from sympy import symbols, Function, Q, ask, ask_generated
from sympy.logic.boolalg import Implies

# Definir variables simbólicas y funciones
x, y = symbols('x y')
f = Function('f')

# Definir una fórmula lógica de orden superior
formula = Implies(Q(x, ask(Q(y, f(x, y)), ask_generated=True)), ask(Q(x, f(x, x)), ask_generated=True))

# Mostrar la fórmula
print("Fórmula lógica de orden superior:", formula)

# Evaluar la fórmula
resultado = ask(formula, ask_generated=True)

# Mostrar el resultado
print("El resultado de la evaluación es:", resultado)
