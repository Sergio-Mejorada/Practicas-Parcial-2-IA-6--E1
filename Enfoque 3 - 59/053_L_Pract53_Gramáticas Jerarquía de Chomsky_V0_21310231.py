#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 148
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

pip install nltk

from nltk import CFG

# Definir una gramática tipo 0 (sin restricciones)
gramatica_tipo_0 = CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'the'
    N -> 'dog' | 'cat'
    V -> 'chased' | 'ate'
""")

# Imprimir la gramática tipo 0
print("Gramática Tipo 0:")
print(gramatica_tipo_0)

from nltk import CFG

# Definir una gramática tipo 1 (sensible al contexto)
gramatica_tipo_1 = CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP | V NP PP
    PP -> P NP
    Det -> 'the'
    N -> 'dog' | 'cat'
    V -> 'chased' | 'ate'
    P -> 'in' | 'on'
""")

# Imprimir la gramática tipo 1
print("Gramática Tipo 1:")
print(gramatica_tipo_1)


from nltk import CFG

# Definir una gramática tipo 2 (independiente del contexto)
gramatica_tipo_2 = CFG.fromstring("""
    S -> NP VP
    NP -> Det N | N
    VP -> V NP | V
    Det -> 'the'
    N -> 'dog' | 'cat'
    V -> 'chased' | 'ate'
""")

# Imprimir la gramática tipo 2
print("Gramática Tipo 2:")
print(gramatica_tipo_2)


from nltk import CFG

# Definir una gramática tipo 3 (regular)
gramatica_tipo_3 = CFG.fromstring("""
    S -> NP VP
    NP -> 'the' N | 'a' N
    VP -> V NP
    N -> 'dog' | 'cat'
    V -> 'chased' | 'ate'
""")

# Imprimir la gramática tipo 3
print("Gramática Tipo 3:")
print(gramatica_tipo_3)
