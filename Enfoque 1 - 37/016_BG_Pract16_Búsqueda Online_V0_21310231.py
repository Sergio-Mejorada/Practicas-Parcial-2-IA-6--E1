#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 15
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())
import time
import random

def busqueda_en_linea():
    objetivo = 42  # Valor que queremos encontrar
    while True:
        nueva_informacion = random.randint(1, 100)  # Simulación de nueva información recibida
        print("Nueva información recibida:", nueva_informacion)
        
        if nueva_informacion == objetivo:
            print("¡Objetivo encontrado!")
            break
        
        time.sleep(1)  # Simulación de procesamiento en tiempo real
        
        # Verificar si se ha ingresado una señal para detener el bucle
        if input("Presiona 'q' y Enter para detener la búsqueda en línea: ") == 'q':
            print("Búsqueda en línea detenida.")
            break

# Ejecutar la búsqueda en línea
busqueda_en_linea()

