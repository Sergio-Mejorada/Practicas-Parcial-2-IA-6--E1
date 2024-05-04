#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 126
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

pip install pyDatalog


from pyDatalog import pyDatalog

# Habilitar el modo de razonamiento no monotónico
pyDatalog.create_terms('X, Y, Z, come, carnivoro, animal, mamifero')

# Definir reglas
+ carnivoro(X) <= animal(X) & come(X, Y) & mamifero(Y)

# Hechos iniciales
+ come('leon', 'cebra')
+ mamifero('cebra')
+ animal('leon')
+ animal('cebra')

# Consulta para determinar si el león es carnívoro
print(carnivoro('leon'))

# Añadir hecho contradictorio
+ come('vaca', 'pasto')

# Consulta nuevamente para determinar si el león es carnívoro
print(carnivoro('leon'))
