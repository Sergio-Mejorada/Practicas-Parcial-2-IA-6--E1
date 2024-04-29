#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 41
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

# Definir la distribución de probabilidad discreta como un diccionario
distribucion_probabilidad = {'A': 0.3, 'B': 0.2, 'C': 0.1, 'D': 0.4}

# Función para calcular la probabilidad de un evento específico
def calcular_probabilidad(evento, distribucion):
    if evento in distribucion:
        return distribucion[evento]
    else:
        return 0  # Devolver 0 si el evento no está en la distribución

# Calcular la probabilidad de eventos específicos
evento_deseado = 'B'
probabilidad_evento = calcular_probabilidad(evento_deseado, distribucion_probabilidad)

# Imprimir la probabilidad del evento deseado
print(f"La probabilidad del evento '{evento_deseado}' es: {probabilidad_evento}")



