#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 135
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


class Tarea:
    def __init__(self, nombre, sub_tareas=None):
        self.nombre = nombre
        self.sub_tareas = sub_tareas if sub_tareas is not None else []

    def agregar_sub_tarea(self, sub_tarea):
        self.sub_tareas.append(sub_tarea)

# Crear las tareas principales
tarea_principal1 = Tarea("Tarea Principal 1")
tarea_principal2 = Tarea("Tarea Principal 2")

# Crear las subtareas para la Tarea Principal 1
sub_tarea1_1 = Tarea("Subtarea 1.1")
sub_tarea1_2 = Tarea("Subtarea 1.2")

tarea_principal1.agregar_sub_tarea(sub_tarea1_1)
tarea_principal1.agregar_sub_tarea(sub_tarea1_2)

# Crear las subtareas para la Tarea Principal 2
sub_tarea2_1 = Tarea("Subtarea 2.1")
sub_tarea2_2 = Tarea("Subtarea 2.2")

tarea_principal2.agregar_sub_tarea(sub_tarea2_1)
tarea_principal2.agregar_sub_tarea(sub_tarea2_2)

# Función para imprimir la estructura de la red jerárquica
def imprimir_red_tareas(tarea, nivel=0):
    print("  " * nivel + tarea.nombre)
    for sub_tarea in tarea.sub_tareas:
        imprimir_red_tareas(sub_tarea, nivel + 1)

# Imprimir la red jerárquica de tareas
print("Red Jerárquica de Tareas:")
imprimir_red_tareas(tarea_principal1)
imprimir_red_tareas(tarea_principal2)
