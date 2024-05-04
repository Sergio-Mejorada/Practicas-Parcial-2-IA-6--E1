#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 147
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

pip install pyfoil

from pyfoil import Foil
from pyfoil.models import Example

# Definir ejemplos positivos y negativos
positivos = [
    Example("sunny", "hot", "high", "false", True),  # Ejemplo positivo
    Example("overcast", "mild", "normal", "false", True),  # Ejemplo positivo
]

negativos = [
    Example("rainy", "mild", "high", "true", False),  # Ejemplo negativo
    Example("sunny", "cool", "normal", "true", False),  # Ejemplo negativo
]

# Crear una instancia de FOIL y entrenarla con los ejemplos
foil = Foil()
foil.learn(positivos, negativos)

# Obtener la regla lógica aprendida por FOIL
regla = foil.to_rule()

# Imprimir la regla lógica aprendida
print("Regla lógica aprendida por FOIL:")
print(regla)
