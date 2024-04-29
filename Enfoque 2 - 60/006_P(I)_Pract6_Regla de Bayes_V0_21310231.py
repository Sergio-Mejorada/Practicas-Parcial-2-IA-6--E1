#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 43
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


# Definir las probabilidades a priori y las probabilidades condicionales
prob_A = 0.3  # Probabilidad a priori de que A ocurra
prob_B_dado_A = 0.8  # Probabilidad condicional de que B ocurra dado que A ha ocurrido
prob_B_dado_no_A = 0.2  # Probabilidad condicional de que B ocurra dado que A no ha ocurrido

# Calcular la probabilidad condicional P(A|B) utilizando la regla de Bayes
def regla_de_bayes(prob_A, prob_B_dado_A, prob_B_dado_no_A):
    prob_B = (prob_B_dado_A * prob_A) + (prob_B_dado_no_A * (1 - prob_A))  # P(B) según la ley de la probabilidad total
    prob_A_dado_B = (prob_B_dado_A * prob_A) / prob_B  # Aplicar la regla de Bayes
    return prob_A_dado_B

# Calcular la probabilidad condicional P(A|B) utilizando la regla de Bayes
prob_A_dado_B = regla_de_bayes(prob_A, prob_B_dado_A, prob_B_dado_no_A)

# Imprimir el resultado
print(f"La probabilidad condicional P(A|B) es: {prob_A_dado_B}")
