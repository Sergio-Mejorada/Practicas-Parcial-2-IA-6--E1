#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 153
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

pip install nltk

from nltk import CFG, parse

# Definir una gramática ambigua
gramatica_ambigua = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | NP PP
    VP -> V NP | VP PP
    PP -> P NP
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat'
    V -> 'chased' | 'ate'
    P -> 'in' | 'on'
""")

# Crear un parser utilizando la gramática ambigua
parser = parse.ChartParser(gramatica_ambigua)

# Definir una cadena de entrada ambigua
cadena_ambigua = 'the dog chased the cat on the mat'

# Realizar el análisis sintáctico ambiguo de la cadena de entrada
arboles_sintacticos = list(parser.parse(cadena_ambigua.split()))

# Imprimir los árboles sintácticos generados (interpretaciones ambiguas)
print("Árboles sintácticos generados (interpretaciones ambiguas):")
for arbol in arboles_sintacticos:
    print(arbol)
