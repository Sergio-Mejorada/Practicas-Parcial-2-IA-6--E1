#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 97
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

# Definir la base de conocimiento como un diccionario
base_conocimiento = {
    'animal': {
        'perro': ['ladra', 'tiene cuatro patas'],
        'gato': ['maulla', 'tiene cuatro patas'],
        'pájaro': ['canta', 'tiene alas']
    },
    'color': {
        'rojo': ['es el color de la sangre', 'es un color cálido'],
        'azul': ['es el color del cielo', 'es un color frío'],
        'verde': ['es el color de la naturaleza', 'es un color relajante']
    }
}

# Función para consultar la base de conocimiento
def consultar_base_conocimiento(categoria, concepto):
    if categoria in base_conocimiento and concepto in base_conocimiento[categoria]:
        return base_conocimiento[categoria][concepto]
    else:
        return f"No se encontró información sobre '{concepto}' en la categoría '{categoria}'."

# Ejemplo de consulta a la base de conocimiento
categoria_consulta = 'animal'
concepto_consulta = 'perro'
info_concepto = consultar_base_conocimiento(categoria_consulta, concepto_consulta)
print(f"Información sobre '{concepto_consulta}': {info_concepto}")

# Ejemplo de consulta no existente en la base de conocimiento
categoria_consulta = 'vehículo'
concepto_consulta = 'automóvil'
info_concepto = consultar_base_conocimiento(categoria_consulta, concepto_consulta)
print(info_concepto)
