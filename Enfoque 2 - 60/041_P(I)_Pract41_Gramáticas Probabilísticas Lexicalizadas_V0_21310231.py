#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 78
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


# Definición de la gramática LPCFG
lpcfg = {
    'S': [('NP VP', 1.0)],
    'NP': [('Det N', 0.6), ('Det Adj N', 0.4)],
    'VP': [('V NP', 0.9), ('VP PP', 0.1)],
    'PP': [('P NP', 1.0)],
    'Det': [('the', 0.6), ('a', 0.4)],
    'N': [('man', 0.5), ('dog', 0.3), ('cat', 0.2)],
    'Adj': [('big', 0.5), ('small', 0.5)],
    'V': [('runs', 0.6), ('eats', 0.4)],
    'P': [('on', 0.6), ('in', 0.4)]
}


# Definición de la gramática LPCFG
lpcfg = {
    'S': [('NP VP', 1.0)],
    'NP': [('Det N', 0.6), ('Det Adj N', 0.4)],
    'VP': [('V NP', 0.9), ('VP PP', 0.1)],
    'PP': [('P NP', 1.0)],
    'Det': [('the', 0.6), ('a', 0.4)],
    'N': [('man', 0.5), ('dog', 0.3), ('cat', 0.2)],
    'Adj': [('big', 0.5), ('small', 0.5)],
    'V': [('runs', 0.6), ('eats', 0.4)],
    'P': [('on', 0.6), ('in', 0.4)]
}


