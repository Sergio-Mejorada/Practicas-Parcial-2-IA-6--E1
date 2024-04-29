#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 23
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

def calcular_utilidad_esperada(opciones):
    utilidad_total = 0
    for opcion in opciones:
        resultado = opcion['resultado']
        probabilidad = opcion['probabilidad']
        utilidad_total += resultado * probabilidad
    return utilidad_total

# Definir las opciones y sus probabilidades asociadas
opcion_1 = {'resultado': 100, 'probabilidad': 0.6}
opcion_2 = {'resultado': 200, 'probabilidad': 0.4}

opciones = [opcion_1, opcion_2]

# Calcular la utilidad esperada de cada opción
utilidad_opcion_1 = calcular_utilidad_esperada(opciones)

# Imprimir los resultados
print("Utilidad esperada de la opción 1:", utilidad_opcion_1)

