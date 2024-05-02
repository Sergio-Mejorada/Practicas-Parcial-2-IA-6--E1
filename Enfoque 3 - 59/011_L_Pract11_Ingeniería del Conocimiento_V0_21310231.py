#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 106
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


# Definir una función que representa una regla de conocimiento
def regla_de_conocimiento(hechos, conclusion):
    for hecho in hechos:
        if not hecho in conocimientos:
            return False
    return conclusion

# Definir un motor de inferencia que aplica las reglas de conocimiento
def motor_inferencia(reglas):
    for regla in reglas:
        hechos, conclusion = regla[:-1], regla[-1]
        if regla_de_conocimiento(hechos, conclusion):
            return conclusion
    return None

# Base de conocimiento (reglas de conocimiento)
conocimientos = {
    ('A', 'B', 'C'): 'D',  # Si A, B y C son verdaderos, entonces D es verdadero
    ('D', 'E'): 'F',       # Si D y E son verdaderos, entonces F es verdadero
    ('F',): 'G'            # Si F es verdadero, entonces G es verdadero
}

# Motor de inferencia
def sistema_experto(hechos):
    reglas = list(conocimientos.keys())
    conclusion = motor_inferencia(reglas)
    return conclusion

# Ejemplo de uso del sistema experto
hechos = ['A', 'B', 'C', 'D', 'E']
resultado = sistema_experto(hechos)

print("Hechos:", hechos)
print("Resultado del sistema experto:", resultado)
