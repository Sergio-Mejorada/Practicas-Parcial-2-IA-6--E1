import re
from collections import Counter

# Definimos las palabras clave que vamos a buscar en los correos
PALABRAS_CLAVE = ["urgente", "reunión", "importante", "proyecto", "plazo", "recordatorio"]

#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 67
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())
import re
from collections import Counter

# Palabras clave relacionadas con reseñas de productos
PALABRAS_CLAVE = ["calidad", "precio", "envío", "atención", "devolución", "satisfacción", "problema"]

# Función para limpiar el texto
def limpiar_texto(texto):
    # Convertimos a minúsculas y eliminamos caracteres especiales
    texto_limpio = re.sub(r'[^a-záéíóúüñ\s]', '', texto.lower())
    return texto_limpio

# Función para hacer el análisis léxico
def analisis_lexico(texto, palabras_clave):
    # Limpiamos el texto
    texto_limpio = limpiar_texto(texto)
    
    # Convertimos el texto en una lista de palabras
    palabras = texto_limpio.split()
    
    # Contamos la frecuencia de las palabras clave
    conteo_palabras = Counter(palabra for palabra in palabras if palabra in palabras_clave)
    
    return conteo_palabras

# Función principal
def main():
    print("Programa de análisis léxico de reseñas de productos")

    # Simulación de entrada de texto de una reseña
    reseña = input("Introduce el contenido de la reseña del producto:\n")

    # Realizamos el análisis léxico
    resultado = analisis_lexico(reseña, PALABRAS_CLAVE)

    # Mostramos los resultados
    if resultado:
        print("\nPalabras clave encontradas en la reseña:")
        for palabra, frecuencia in resultado.items():
            print(f"{palabra}: {frecuencia} veces")
    else:
        print("\nNo se encontraron palabras clave en la reseña.")

if __name__ == "__main__":
    main()
