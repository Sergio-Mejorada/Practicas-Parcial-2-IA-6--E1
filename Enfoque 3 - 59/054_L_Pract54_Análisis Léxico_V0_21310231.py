#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 149
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import re

# Definir el código fuente como una cadena de texto
codigo_fuente = """
if x > 5:
    print("El número es mayor que 5")
else:
    print("El número es menor o igual a 5")
"""

# Definir patrones de expresiones regulares para tokens
patrones = [
    (r'\bif\b', 'IF'),
    (r'\belse\b', 'ELSE'),
    (r'\bwhile\b', 'WHILE'),
    (r'\bprint\b', 'PRINT'),
    (r'[a-zA-Z][a-zA-Z0-9_]*', 'IDENTIFIER'),  # Identificadores
    (r'\d+', 'NUMBER'),  # Números enteros
    (r'\s+', 'SPACE')  # Espacios en blanco (ignorados)
]

# Función para realizar el análisis léxico
def analisis_lexico(codigo_fuente, patrones):
    tokens = []
    texto_restante = codigo_fuente

    while texto_restante:
        for patron, etiqueta in patrones:
            match = re.match(patron, texto_restante)
            if match:
                token = match.group(0)
                if etiqueta != 'SPACE':
                    tokens.append((etiqueta, token))
                texto_restante = texto_restante[len(token):]
                break
        else:
            raise ValueError(f"No se puede analizar el texto restante: {texto_restante}")

    return tokens

# Realizar el análisis léxico del código fuente
tokens = analisis_lexico(codigo_fuente, patrones)

# Imprimir los tokens generados
print("Tokens generados:")
for token in tokens:
    print(token)
