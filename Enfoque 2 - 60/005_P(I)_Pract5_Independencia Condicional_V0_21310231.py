#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 42
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

# Definir el conjunto de datos
datos = [('S', 'H', 'L'), ('R', 'L', 'H'), ('S', 'H', 'H'), ('R', 'H', 'L'), ('R', 'L', 'L')]

# Contar la frecuencia de ocurrencia de los estados de A, B y C
frecuencia_A = {'S': 0, 'R': 0}
frecuencia_B = {'H': 0, 'L': 0}
frecuencia_C = {'H': 0, 'L': 0}

for tupla in datos:
    estado_A, estado_B, estado_C = tupla
    frecuencia_A[estado_A] += 1
    frecuencia_B[estado_B] += 1
    frecuencia_C[estado_C] += 1

# Calcular la probabilidad condicional P(A | B, C) y verificar la independencia condicional
def probabilidad_condicional(A, B, C, datos):
    conteo_A_B_C = sum(1 for tupla in datos if tupla[0] == A and tupla[1] == B and tupla[2] == C)
    conteo_B_C = sum(1 for tupla in datos if tupla[1] == B and tupla[2] == C)
    prob_condicional = conteo_A_B_C / conteo_B_C if conteo_B_C > 0 else 0
    return prob_condicional

# Ejemplo de uso para verificar la independencia condicional
evento_A = 'S'
evento_B = 'H'
evento_C = 'L'
prob_condicional_ABC = probabilidad_condicional(evento_A, evento_B, evento_C, datos)

# Imprimir resultados y verificar independencia condicional
print(f"La probabilidad condicional P({evento_A} | {evento_B}, {evento_C}) es: {prob_condicional_ABC}")

# Verificar independencia condicional
independencia_condicional = prob_condicional_ABC == frecuencia_A[evento_A] / len(datos)
print("¿Son A y B condicionalmente independientes dado C?", independencia_condicional)


