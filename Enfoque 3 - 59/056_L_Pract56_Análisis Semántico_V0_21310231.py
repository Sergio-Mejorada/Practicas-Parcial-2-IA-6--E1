#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 151
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


# Definir una función para realizar el análisis semántico de una expresión aritmética
def analisis_semantico(expresion):
    # Dividir la expresión en tokens
    tokens = expresion.split()
    
    # Verificar la corrección de las operaciones y variables utilizadas
    for token in tokens:
        if token.isdigit():
            # Si el token es un número, seguir verificando la siguiente iteración
            continue
        elif token in ['+', '-', '*', '/']:
            # Si el token es un operador, seguir verificando la siguiente iteración
            continue
        else:
            # Si el token no es un número ni un operador, es una variable
            print(f"Error semántico: Variable '{token}' no está definida.")
            return False
    
    # Si no hay errores semánticos, la expresión es válida
    return True

# Ejemplo de expresión aritmética para analizar semánticamente
expresion_aritmetica = "3 + (4 * 5) - 8 / 2"

# Realizar el análisis semántico de la expresión aritmética
resultado_semantico = analisis_semantico(expresion_aritmetica)

# Imprimir el resultado del análisis semántico
if resultado_semantico:
    print("La expresión aritmética es semánticamente válida.")
else:
    print("La expresión aritmética contiene errores semánticos.")
