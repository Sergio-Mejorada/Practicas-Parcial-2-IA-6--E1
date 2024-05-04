#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 116
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


# Definición de la base de conocimiento en forma de diccionario
base_conocimiento = {
    "humano": ["juan", "maría", "pedro"],
    "mortal": ["juan", "maría", "pedro"]
}

# Función para hacer una consulta sobre la base de conocimiento
def consulta(conocimiento, pregunta):
    """
    Realiza una consulta sobre la base de conocimiento.
    
    Args:
        conocimiento (dict): Base de conocimiento representada como un diccionario.
        pregunta (str): Pregunta sobre la base de conocimiento.
    
    Returns:
        bool: True si la pregunta es verdadera según la base de conocimiento, False en caso contrario.
    """
    # Remover caracteres especiales y dividir la pregunta en palabras
    palabras = pregunta.replace("¿", "").replace("?", "").split()
    if "es" in palabras:
        # Encontrar el índice de "es"
        index_es = palabras.index("es")
        # Obtener el atributo y el objeto de la pregunta
        atributo = palabras[index_es - 1]
        objeto = palabras[index_es + 1]
        # Verificar si el objeto tiene el atributo en la base de conocimiento
        return objeto in conocimiento.get(atributo, [])
    else:
        return False  # La pregunta no sigue el formato esperado

# Ejemplo de consulta
pregunta = "¿juan es mortal?"
resultado = consulta(base_conocimiento, pregunta)
print("Respuesta:", resultado)


