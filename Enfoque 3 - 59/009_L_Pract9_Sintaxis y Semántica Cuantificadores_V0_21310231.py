#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 104
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import sympy as sp

# Definir variables simbólicas
x, y = sp.symbols('x y')

# Ejemplo de cuantificador existencial (∃x)
expresion_existencial = sp.Exists(x, x > 0)
print("Expresión con cuantificador existencial (∃x):", expresion_existencial)

# Ejemplo de cuantificador universal (∀y)
expresion_universal = sp.ForAll(y, y < 10)
print("Expresión con cuantificador universal (∀y):", expresion_universal)

# Evaluar cuantificadores
print("Evaluación de la expresión existencial para algunos valores de x:")
print(expresion_existencial.subs(x, 5))  # True si x > 0 para x = 5, False de lo contrario
print(expresion_existencial.subs(x, -3))  # True si x > 0 para x = -3, False de lo contrario

print("Evaluación de la expresión universal para algunos valores de y:")
print(expresion_universal.subs(y, 5))  # True si y < 10 para y = 5, False de lo contrario
print(expresion_universal.subs(y, 15))  # True si y < 10 para y = 15, False de lo contrario
