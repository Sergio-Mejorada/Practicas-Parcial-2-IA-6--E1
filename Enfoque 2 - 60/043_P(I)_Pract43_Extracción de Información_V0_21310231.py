#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 79
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


import re

def extract_information(text):
    """
    Extrae información relevante de un texto utilizando expresiones regulares.

    Args:
    - text: El texto del cual se desea extraer información.

    Returns:
    Un diccionario con la información extraída.
    """
    # Patrones de expresiones regulares para buscar información específica
    name_pattern = r"Name: (\w+)"
    age_pattern = r"Age: (\d+)"
    email_pattern = r"Email: (\w+@\w+\.\w+)"
    phone_pattern = r"Phone: (\d{3}-\d{3}-\d{4})"

    # Buscar patrones en el texto utilizando expresiones regulares
    name_match = re.search(name_pattern, text)
  
