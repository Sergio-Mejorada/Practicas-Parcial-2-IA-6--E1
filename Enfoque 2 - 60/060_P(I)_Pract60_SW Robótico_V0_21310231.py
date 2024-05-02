#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 95
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import pygame
import time

# Inicializar Pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Definir dimensiones de la ventana
ANCHO = 800
ALTO = 600

# Crear la ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption('Simulación de Robot')

# Coordenadas del robot
robot_x = ANCHO // 2
robot_y = ALTO // 2

# Velocidad del robot
velocidad = 5

# Bucle principal
ejecutando = True
while ejecutando:
    ventana.fill(BLANCO)  # Limpiar la pantalla
    
    # Dibujar el robot (un rectángulo por simplicidad)
    pygame.draw.rect(ventana, NEGRO, (robot_x, robot_y, 50, 50))
    
    # Actualizar la pantalla
    pygame.display.flip()
    
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                robot_x -= velocidad
            elif evento.key == pygame.K_RIGHT:
                robot_x += velocidad
            elif evento.key == pygame.K_UP:
                robot_y -= velocidad
            elif evento.key == pygame.K_DOWN:
                robot_y += velocidad
    
    # Limitar la velocidad de actualización
    time.sleep(0.02)

# Finalizar Pygame
pygame.quit()
