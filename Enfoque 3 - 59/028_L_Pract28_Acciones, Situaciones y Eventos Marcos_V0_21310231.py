#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 123
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


# Definir marcos de acciones, situaciones y eventos utilizando diccionarios
marcos = {
    "Marco1": {
        "Acciones": ["A1", "A2"],
        "Situacion": "S1",
        "Evento": "E1"
    },
    "Marco2": {
        "Acciones": ["A3", "A4"],
        "Situacion": "S2",
        "Evento": "E2"
    }
}

# Mostrar información de los marcos
for nombre_marco, datos_marco in marcos.items():
    print(f"Marco: {nombre_marco}")
    print(f"Acciones: {', '.join(datos_marco['Acciones'])}")
    print(f"Situación: {datos_marco['Situacion']}")
    print(f"Evento: {datos_marco['Evento']}")
    print()
