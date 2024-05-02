#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 100
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())




import sympy as sp

# Función para obtener la Forma Normal Conjuntiva (FNC) de una expresión lógica
def obtener_fnc(expresion):
    e = sp.sympify(expresion)
    fnc = sp.to_cnf(e, True)
    return fnc

# Ejemplo de uso de la función
expresion = '(A | B) & (~A | C)'
fnc = obtener_fnc(expresion)
print(f"Expresión original: {expresion}")
print(f"Forma Normal Conjuntiva (FNC): {fnc}")
