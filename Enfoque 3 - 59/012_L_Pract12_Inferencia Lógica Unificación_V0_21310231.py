#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 107
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


# Función para realizar unificación entre dos términos
def unificar(termino1, termino2, sustitucion=None):
    # Si no se proporciona una sustitución inicial, se crea una nueva
    if sustitucion is None:
        sustitucion = {}
    
    # Caso base: si los términos son iguales, la unificación es exitosa
    if termino1 == termino2:
        return sustitucion
    
    # Caso 1: si alguno de los términos es una variable, se realiza la sustitución
    if es_variable(termino1):
        return unificar_variable(termino1, termino2, sustitucion)
    elif es_variable(termino2):
        return unificar_variable(termino2, termino1, sustitucion)
    
    # Caso 2: si ambos términos son compuestos, se unifican sus sub-términos
    if es_compuesto(termino1) and es_compuesto(termino2):
        return unificar(termino1[1:], termino2[1:], unificar(termino1[0], termino2[0], sustitucion))
    
    # Si ningún caso se cumple, la unificación falla
    return None

# Función para realizar unificación cuando uno de los términos es una variable
def unificar_variable(variable, termino, sustitucion):
    if variable in sustitucion:
        return unificar(sustitucion[variable], termino, sustitucion)
    elif termino in sustitucion:
        return unificar(variable, sustitucion[termino], sustitucion)
    else:
        sustitucion[variable] = termino
        return sustitucion

# Funciones auxiliares para verificar si un término es una variable o compuesto
def es_variable(termino):
    return isinstance(termino, str) and termino.islower()

def es_compuesto(termino):
    return isinstance(termino, list) and len(termino) > 0

# Ejemplo de uso de la unificación
termino1 = ['f', 'X', 'a']
termino2 = ['f', 'b', 'Y']
sustitucion = unificar(termino1, termino2)

print("Término 1:", termino1)
print("Término 2:", termino2)
print("Unificación:", sustitucion)
