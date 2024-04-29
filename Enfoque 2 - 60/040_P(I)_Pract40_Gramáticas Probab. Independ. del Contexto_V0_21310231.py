#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 77
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

# Definición de la gramática PCFG
pcfg = {
    'S': [('NP', 'VP', 0.8), ('VP', 'NP', 0.2)],
    'NP': [('Det', 'N', 0.6), ('Det', 'N', 0.4)],
    'VP': [('V', 'NP', 0.9), ('VP', 'PP', 0.1)],
    'PP': [('P', 'NP', 1.0)],
    'Det': [('the', 0.6), ('a', 0.4)],
    'N': [('man', 0.5), ('dog', 0.3), ('cat', 0.2)],
    'V': [('runs', 0.6), ('eats', 0.4)],
    'P': [('on', 0.6), ('in', 0.4)]
}


import random

def generate_sentence(grammar, start_symbol='S'):
    """
    Genera una oración aleatoria a partir de una gramática PCFG.

    Args:
    - grammar: La gramática PCFG definida como un diccionario.
    - start_symbol: El símbolo inicial de la gramática.

    Returns:
    Una oración generada aleatoriamente.
    """
    if start_symbol not in grammar:
        return start_symbol
    production = random.choices(grammar[start_symbol], weights=[prod[2] for prod in grammar[start_symbol]])[0]
    return ' '.join([generate_sentence(grammar, symbol) for symbol in production[:2]])

# Ejemplo de uso:
random_sentence = generate_sentence(pcfg)
print("Oración generada:", random_sentence)
