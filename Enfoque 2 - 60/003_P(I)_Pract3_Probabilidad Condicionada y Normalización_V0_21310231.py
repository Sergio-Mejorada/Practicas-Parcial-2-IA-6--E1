#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 40
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


# Definimos la probabilidad conjunta P(A, B) y las probabilidades marginales P(A) y P(B)
prob_conjunta = {'A': {'B': 0.3, '¬B': 0.2}, '¬A': {'B': 0.1, '¬B': 0.4}}
prob_marginal_A = prob_conjunta['A']['B'] + prob_conjunta['A']['¬B']
prob_marginal_B = prob_conjunta['A']['B'] + prob_conjunta['¬A']['B']

# Función para calcular la probabilidad condicionada P(A | B)
def probabilidad_condicionada(A, B, prob_conjunta):
    return prob_conjunta[A][B] / prob_marginal_B

# Calcular la probabilidad condicionada P(A | B) para eventos específicos
evento_A = 'A'
evento_B = 'B'
prob_condicionada = probabilidad_condicionada(evento_A, evento_B, prob_conjunta)

# Normalizar las probabilidades condicionadas P(A | B) y P(¬A | B)
prob_condicionada_no_A = 1 - prob_condicionada
prob_normalizada = {'A': prob_condicionada, '¬A': prob_condicionada_no_A}

# Imprimir resultados
print("Probabilidad condicionada P(A | B):", prob_condicionada)
print("Probabilidad condicionada P(¬A | B):", prob_condicionada_no_A)
print("Probabilidades normalizadas:", prob_normalizada)
