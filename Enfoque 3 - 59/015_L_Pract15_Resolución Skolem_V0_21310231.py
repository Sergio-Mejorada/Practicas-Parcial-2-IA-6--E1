#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 110
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

from sympy import symbols, Or, Not, Ask, ask

# Definir variables simbólicas
x, y = symbols('x y')

# Definir la fórmula lógica con cuantificador existencial
formula = Or(x, Not(y))

# Mostrar la fórmula original
print("Fórmula original:", formula)

# Aplicar la resolución Skolem
formula_skolem = ask(formula, Ask.skolemize)
print("Fórmula después de Skolemización:", formula_skolem)
