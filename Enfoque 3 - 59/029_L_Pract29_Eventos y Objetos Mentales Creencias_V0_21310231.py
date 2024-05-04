#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 124
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


# Definir una estructura de creencias utilizando un diccionario
creencias = {
    "Creencia1": {
        "Evento": "E1",
        "Objeto": "O1"
    },
    "Creencia2": {
        "Evento": "E2",
        "Objeto": "O2"
    }
}

# Mostrar información de las creencias
for nombre_creencia, datos_creencia in creencias.items():
    print(f"Creencia: {nombre_creencia}")
    print(f"Evento: {datos_creencia['Evento']}")
    print(f"Objeto: {datos_creencia['Objeto']}")
    print()
