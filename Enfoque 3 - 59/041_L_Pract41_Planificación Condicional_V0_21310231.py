#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 136
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

def planificacion_condicional(condicion, accion_true, accion_false):
    if condicion:
        accion_true()
    else:
        accion_false()

# Ejemplo de uso
def accion_verdadera():
    print("La condición es verdadera. Realizando la acción verdadera.")

def accion_falsa():
    print("La condición es falsa. Realizando la acción falsa.")

# Definir una condición
condicion = True

# Ejecutar la planificación condicional
planificacion_condicional(condicion, accion_verdadera, accion_falsa)
