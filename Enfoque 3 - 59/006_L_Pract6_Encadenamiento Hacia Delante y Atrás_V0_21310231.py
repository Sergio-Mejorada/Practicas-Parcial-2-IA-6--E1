#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 101
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())





# Definir la base de conocimiento como un diccionario de reglas
base_conocimiento_adelante = {
    'reglas': [
        ('A', 'B'),  # Si A es verdadero, entonces B es verdadero
        ('B', 'C'),  # Si B es verdadero, entonces C es verdadero
        ('C', 'D'),  # Si C es verdadero, entonces D es verdadero
        ('E', 'F'),  # Si E es verdadero, entonces F es verdadero
    ]
}

# Función para encadenamiento hacia adelante
def encadenamiento_adelante(base_conocimiento, hechos_iniciales):
    reglas = base_conocimiento['reglas']
    nuevos_hechos = []
    while True:
        hecho_agregado = False
        for antecedente, consecuente in reglas:
            if antecedente in hechos_iniciales and consecuente not in hechos_iniciales:
                hechos_iniciales.add(consecuente)
                nuevos_hechos.append(consecuente)
                hecho_agregado = True
        if not hecho_agregado:
            break
    return hechos_iniciales, nuevos_hechos

# Ejemplo de encadenamiento hacia adelante
hechos_iniciales_adelante = {'A', 'E'}
hechos_resultantes_adelante, nuevos_hechos_adelante = encadenamiento_adelante(base_conocimiento_adelante, hechos_iniciales_adelante)
print("Hechos iniciales:", hechos_iniciales_adelante)
print("Hechos resultantes:", hechos_resultantes_adelante)
print("Nuevos hechos inferidos:", nuevos_hechos_adelante)

# Definir la base de conocimiento como un diccionario de reglas
base_conocimiento_atras = {
    'reglas': [
        ('A', 'B'),  # Si B es verdadero, entonces A es verdadero
        ('B', 'C'),  # Si C es verdadero, entonces B es verdadero
        ('C', 'D'),  # Si D es verdadero, entonces C es verdadero
        ('E', 'F'),  # Si F es verdadero, entonces E es verdadero
    ]
}

# Función para encadenamiento hacia atrás
def encadenamiento_atras(base_conocimiento, hechos_objetivo):
    reglas = base_conocimiento['reglas']
    hechos_faltantes = hechos_objetivo.copy()
    while hechos_faltantes:
        hecho_objetivo = hechos_faltantes.pop()
        for antecedente, consecuente in reglas:
            if hecho_objetivo == consecuente:
                hechos_faltantes.add(antecedente)
    return hechos_objetivo

# Ejemplo de encadenamiento hacia atrás
hechos_objetivo_atras = {'D', 'F'}
hechos_resultantes_atras = encadenamiento_atras(base_conocimiento_atras, hechos_objetivo_atras)
print("Hechos objetivo:", hechos_objetivo_atras)
print("Hechos inferidos:", hechos_resultantes_atras)


