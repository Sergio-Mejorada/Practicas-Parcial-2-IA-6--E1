#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 67
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import math

# Función para calcular la media
def calcular_media(mediciones):
    return sum(mediciones) / len(mediciones)

# Función para calcular la incertidumbre estándar
def calcular_incertidumbre(mediciones, media):
    suma_cuadrados = sum((x - media) ** 2 for x in mediciones)
    incertidumbre = math.sqrt(suma_cuadrados / (len(mediciones) - 1))
    return incertidumbre

# Función principal
def main():
    print("Programa de cálculo de incertidumbre de mediciones")
    print("Introduce las mediciones de longitud en milímetros (mm).")

    # Lista para almacenar las mediciones
    mediciones = []

    while True:
        entrada = input("Introduce una medición (o escribe 'fin' para terminar): ")
        if entrada.lower() == 'fin':
            break
        try:
            medicion = float(entrada)
            mediciones.append(medicion)
        except ValueError:
            print("Por favor, introduce un número válido.")

    if len(mediciones) < 2:
        print("Se necesitan al menos dos mediciones para calcular la incertidumbre.")
        return

    # Cálculos
    media = calcular_media(mediciones)
    incertidumbre = calcular_incertidumbre(mediciones, media)

    # Incertidumbre de la herramienta (regla)
    incertidumbre_regla = 0.5  # mm, puedes cambiar esto según la precisión de tu regla
    incertidumbre_total = math.sqrt(incertidumbre**2 + incertidumbre_regla**2)

    # Resultados
    print(f"\nResultado de las mediciones:")
    print(f"Media de las mediciones: {media:.2f} mm")
    print(f"Incertidumbre estándar de las mediciones: {incertidumbre:.2f} mm")
    print(f"Incertidumbre total (incluyendo la regla): {incertidumbre_total:.2f} mm")

if __name__ == "__main__":
    main()
