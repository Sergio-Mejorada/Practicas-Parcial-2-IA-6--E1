#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 96
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


import itertools

# Definir las variables de la expresión lógica y sus posibles valores
variables = ['A', 'B', 'C']
valores_posibles = [True, False]

# Generar todas las combinaciones posibles de valores para las variables
combinaciones = list(itertools.product(valores_posibles, repeat=len(variables)))

# Definir la expresión lógica (ejemplo: (A AND B) OR (NOT C))
def expresion_logica(A, B, C):
    return (A and B) or (not C)

# Imprimir encabezado de la tabla de verdad
encabezado = '\t'.join(variables + ['Resultado'])
print(encabezado)

# Calcular y mostrar los resultados para cada combinación de valores
for combinacion in combinaciones:
    valores_combinacion = dict(zip(variables, combinacion))
    resultado = expresion
