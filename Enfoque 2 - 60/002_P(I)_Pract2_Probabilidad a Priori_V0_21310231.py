#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 39
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

# Definimos una lista de eventos y sus respectivas probabilidades a priori
eventos = ['A', 'B', 'C']
probabilidades_priori = [0.3, 0.5, 0.2]

# Función para calcular la probabilidad a priori de un evento dado su nombre
def probabilidad_a_priori(evento, eventos, probabilidades_priori):
    if evento in eventos:
        indice_evento = eventos.index(evento)
        return probabilidades_priori[indice_evento]
    else:
        return None  # Si el evento no está en la lista, devolvemos None

# Ejemplo de uso de la función
evento_deseado = 'B'
prob_a_priori_evento_deseado = probabilidad_a_priori(evento_deseado, eventos, probabilidades_priori)

# Imprimimos la probabilidad a priori del evento deseado
if prob_a_priori_evento_deseado is not None:
    print(f"La probabilidad a priori del evento '{evento_deseado}' es: {prob_a_priori_evento_deseado}")
else:
    print(f"El evento '{evento_deseado}' no está en la lista de eventos.")

    
