#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 98
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

      # Definir la base de conocimiento como un diccionario de reglas lógicas
base_conocimiento = {
    'reglas': [
        ('A AND B', 'C'),  # Regla 1: Si A y B son verdaderos, entonces C es verdadero
        ('C OR D', 'E'),   # Regla 2: Si C o D son verdaderos, entonces E es verdadero
        ('NOT E', 'F')     # Regla 3: Si E es falso, entonces F es verdadero
    ]
}

# Función para evaluar una expresión lógica
def evaluar_expresion(expresion, hechos):
    expresion_evaluada = expresion
    for hecho, valor in hechos.items():
        expresion_evaluada = expresion_evaluada.replace(hecho, str(valor))
    return eval(expresion_evaluada)

# Función para realizar inferencia lógica
def inferencia_logica(base_conocimiento, hechos):
    reglas = base_conocimiento['reglas']
    nuevo_hecho = True
    while nuevo_hecho:
        nuevo_hecho = False
        for regla in reglas:
            antecedente, consecuente = regla
            if evaluar_expresion(antecedente, hechos) and consecuente not in hechos:
                hechos[consecuente] = True
                nuevo_hecho = True

# Ejemplo de inferencia lógica
hechos = {'A': True, 'B': True}  # Hechos iniciales conocidos
inferencia_logica(base_conocimiento, hechos)
print("Hechos inferidos después de aplicar las reglas:")
for hecho, valor in hechos.items():
    print(f"{hecho}: {valor}")

    
