#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 150
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

pip install lark-parser

from lark import Lark, Transformer

# Definir la gramática para expresiones aritméticas
gramatica_aritmetica = """
    start: expr
    
    ?expr: term
        | expr "+" term  -> suma
        | expr "-" term  -> resta
        
    ?term: factor
        | term "*" factor  -> multiplicacion
        | term "/" factor  -> division
        
    ?factor: NUMBER  -> numero
        | "(" expr ")"
    
    %import common.NUMBER
    %import common.WS_INLINE
    
    %ignore WS_INLINE
"""

# Crear un parser utilizando la gramática definida
parser = Lark(gramatica_aritmetica, parser='lalr')

# Definir una clase Transformer para procesar el árbol sintáctico generado
class CalculadoraTransformer(Transformer):
    def suma(self, items):
        return float(items[0]) + float(items[1])
    
    def resta(self, items):
        return float(items[0]) - float(items[1])
    
    def multiplicacion(self, items):
        return float(items[0]) * float(items[1])
    
    def division(self, items):
        return float(items[0]) / float(items[1])
    
    def numero(self, items):
        return float(items[0])

# Ejemplo de expresión aritmética para analizar
expresion_aritmetica = "3 + (4 * 5) - 8 / 2"

# Analizar la expresión aritmética utilizando el parser y el transformer
arbol_sintactico = parser.parse(expresion_aritmetica)
resultado = CalculadoraTransformer().transform(arbol_sintactico)

# Imprimir el resultado de la expresión aritmética
print(f"Resultado de la expresión '{expresion_aritmetica}': {resultado}")


Resultado de la expresión '3 + (4 * 5) - 8 / 2': 17.0


