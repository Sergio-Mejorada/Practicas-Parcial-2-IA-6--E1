#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 105
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


import sympy as sp

# Definir variables simbólicas
A, B, C, D = sp.symbols('A B C D')

# Definir reglas de diagnóstico
reglas_diagnosticos = [
    (A & B, C),  # Si A y B son verdaderos, entonces C es verdadero
    (C, D)       # Si C es verdadero, entonces D es verdadero
]

# Función para evaluar reglas de diagnóstico
def evaluar_diagnosticos(reglas, observaciones):
    conocimientos = set(observaciones)  # Convertir observaciones a un conjunto de conocimientos
    nuevos_conocimientos = set()  # Conjunto para almacenar nuevos conocimientos inferidos
    
    for antecedente, consecuente in reglas:
        if antecedente in conocimientos and consecuente not in conocimientos:
            nuevos_conocimientos.add(consecuente)
    
    conocimientos.update(nuevos_conocimientos)
    return conocimientos

# Ejemplo de uso de reglas de diagnóstico
observaciones = [A, B]  # Síntomas observados
conocimientos = evaluar_diagnosticos(reglas_diagnosticos, observaciones)

print("Observaciones:", observaciones)
print("Conocimientos inferidos:", conocimientos)
