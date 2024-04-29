#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 45
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


# Definir las probabilidades a priori y las probabilidades condicionales
prob_A = 0.3  # Probabilidad a priori de que A ocurra
prob_B_dado_A = 0.8  # Probabilidad condicional de que B ocurra dado que A ha ocurrido
prob_B = 0.5  # Probabilidad a priori de que B ocurra

# Calcular la probabilidad conjunta P(A ∩ B) utilizando la regla de la cadena
prob_A_interseccion_B = prob_B_dado_A * prob_A  # Alternativamente, prob_B * prob_A_dado_B

# Imprimir el resultado
print(f"La probabilidad conjunta P(A ∩ B) es: {prob_A_interseccion_B}")
