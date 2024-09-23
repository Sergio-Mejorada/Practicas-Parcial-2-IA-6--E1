#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 67
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import random
import math

# Definimos los límites del entorno
world_size = 100.0  # Espacio 1D de 0 a 100

# Función para añadir ruido a la medición
def gaussian(mu, sigma, x):
    return (1.0 / math.sqrt(2.0 * math.pi * sigma**2)) * math.exp(-0.5 * ((x - mu) / sigma)**2)

# Clase para representar el robot
class Robot:
    def __init__(self):
        self.position = random.uniform(0, world_size)
        self.noise = 0.0  # No hay ruido por defecto

    def set_noise(self, noise):
        self.noise = noise

    def move(self, delta):
        self.position += delta
        self.position %= world_size  # El entorno es cíclico

    def sense(self):
        # Medición del sensor con ruido
        return self.position + random.gauss(0, self.noise)

# Inicializamos el robot
robot = Robot()
robot.set_noise(2.0)  # Añadimos ruido a la medición del sensor

# Partículas (Monte Carlo)
num_particles = 1000
particles = [Robot() for _ in range(num_particles)]

# Algoritmo de localización Monte Carlo
def monte_carlo_localization(robot, particles, move_step):
    # Movimiento del robot
    robot.move(move_step)
    measurement = robot.sense()

    # Movimiento de las partículas
    for particle in particles:
        particle.move(move_step)

    # Actualización de las probabilidades (basado en la medición del sensor)
    weights = []
    for particle in particles:
        particle_measurement = particle.sense()
        weight = gaussian(measurement, robot.noise, particle_measurement)
        weights.append(weight)

    # Re-muestreo basado en los pesos
    new_particles = []
    index = int(random.random() * num_particles)
    beta = 0.0
    max_weight = max(weights)

    for _ in range(num_particles):
        beta += random.random() * 2.0 * max_weight
        while beta > weights[index]:
            beta -= weights[index]
            index = (index + 1) % num_particles
        new_particles.append(particles[index])

    return new_particles

# Simulación de 10 pasos de movimiento
for i in range(10):
    print(f"Paso {i+1}")
    particles = monte_carlo_localization(robot, particles, move_step=5)
    estimated_position = sum([p.position for p in particles]) / num_particles
    print(f"Posición estimada: {estimated_position:.2f}")
    print(f"Posición real: {robot.position:.2f}\n")
