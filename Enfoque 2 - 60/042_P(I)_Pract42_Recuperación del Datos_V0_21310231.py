#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 78
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

# Base de datos como una lista de diccionarios
database = [
    {"id": 1, "name": "John Doe", "age": 30, "city": "New York"},
    {"id": 2, "name": "Jane Smith", "age": 25, "city": "Los Angeles"},
    {"id": 3, "name": "Michael Johnson", "age": 35, "city": "Chicago"}
]

def retrieve_data_by_id(database, id):
    """
    Recupera información de la base de datos basándose en el ID proporcionado.

    Args:
    - database: Lista de diccionarios que representa la base de datos.
    - id: El ID de la entrada que se desea recuperar.

    Returns:
    La entrada correspondiente al ID proporcionado, o None si no se encuentra.
    """
    for entry in database:
        if entry["id"] == id:
            return entry
    return None

# Ejemplo de uso:
id_to_retrieve = 2
retrieved_entry = retrieve_data_by_id(database, id_to_retrieve)

if retrieved_entry:
    print("Información recuperada:", retrieved_entry)
else:
    print("No se encontró ninguna entrada con el ID proporcionado.")


