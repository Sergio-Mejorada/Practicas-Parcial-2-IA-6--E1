#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 138
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


class Agente:
    def __init__(self, id_agente, posicion_inicial):
        self.id_agente = id_agente
        self.posicion_actual = posicion_inicial

    def moverse(self, nueva_posicion):
        print(f"Agente {self.id_agente}: Moviendo de {self.posicion_actual} a {nueva_posicion}")
        self.posicion_actual = nueva_posicion

# Crear agentes y definir posiciones iniciales
agente1 = Agente(1, (0, 0))
agente2 = Agente(2, (3, 5))
agente3 = Agente(3, (2, 1))

# Ejecutar la planificación continua y multiagente
objetivo_completado = False

while not objetivo_completado:
    # Aquí podrías implementar la lógica de planificación continua y multiagente
    # Por ejemplo, cada agente puede decidir su próxima acción de acuerdo a un objetivo compartido o individual
    
    # Supongamos que los agentes deciden moverse a una nueva posición de manera aleatoria para este ejemplo
    nueva_posicion_agente1 = (1, 1)
    agente1.moverse(nueva_posicion_agente1)

    nueva_posicion_agente2 = (4, 3)
    agente2.moverse(nueva_posicion_agente2)

    nueva_posicion_agente3 = (3, 2)
    agente3.moverse(nueva_posicion_agente3)

    # Aquí podrías agregar condiciones para verificar si se ha completado el objetivo o se requiere replanificación
    # En este ejemplo, supondremos que el objetivo se completa después de un cierto número de iteraciones
    if len(nueva_posicion_agente1) == 2 and len(nueva_posicion_agente2) == 2 and len(nueva_posicion_agente3) == 2:
        objetivo_completado = True

print("Objetivo completado. Terminando la ejecución.")
