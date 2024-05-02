#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 99
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


import sympy as sp

# Función para verificar la equivalencia de dos expresiones lógicas
def verificar_equivalencia(expresion1, expresion2):
    e1 = sp.sympify(expresion1)
    e2 = sp.sympify(expresion2)
    return e1.equals(e2)

# Función para verificar la validez de una expresión lógica
def verificar_validez(expresion):
    e = sp.sympify(expresion)
    return e.is_valid

# Función para verificar la satisfacibilidad de una expresión lógica
def verificar_satisfacibilidad(expresion):
    e = sp.sympify(expresion)
    return e.satisfiable()

# Ejemplo de uso de las funciones
expresion1 = 'A & B'
expresion2 = 'B & A'
expresion3 = 'A | ~A'
expresion4 = 'A & B | ~A & ~B'

print(f"Las expresiones '{expresion1}' y '{expresion2}' son equivalentes:", verificar_equivalencia(expresion1, expresion2))
print(f"La expresión '{expresion3}' es válida:", verificar_validez(expresion3))
print(f"La expresión '{expresion4}' es satisfacible:", verificar_satisfacibilidad(expresion4))

