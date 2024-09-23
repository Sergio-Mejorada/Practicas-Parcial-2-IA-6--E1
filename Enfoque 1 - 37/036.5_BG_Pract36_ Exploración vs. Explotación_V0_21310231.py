#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 67
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import random

# Lista de restaurantes (nombres ficticios)
restaurants = ['Restaurante A', 'Restaurante B', 'Restaurante C', 'Restaurante D', 'Restaurante E']

# Diccionario para almacenar la calificación de los restaurantes que ya se han probado
ratings = {restaurant: None for restaurant in restaurants}

# Función para obtener una calificación aleatoria (simulando la calidad del restaurante)
def get_rating():
    return round(random.uniform(1, 5), 1)

# Función para mostrar las calificaciones conocidas
def show_known_ratings():
    print("\nRestaurantes y sus calificaciones:")
    for restaurant, rating in ratings.items():
        if rating is not None:
            print(f"{restaurant}: {rating} estrellas")
        else:
            print(f"{restaurant}: No probado aún")
    print()

# Función principal
def restaurant_decision():
    print("¡Bienvenido al selector de restaurantes!")

    while True:
        # Mostrar las calificaciones conocidas hasta el momento
        show_known_ratings()

        # Preguntar al usuario si quiere explorar o explotar
        decision = input("\n¿Quieres 'explorar' un nuevo restaurante o 'explotar' uno conocido? (escribe 'salir' para terminar): ").lower()

        if decision == 'salir':
            print("¡Gracias por jugar! Que disfrutes de tu comida.")
            break

        elif decision == 'explorar':
            # Explorar un nuevo restaurante
            available = [r for r in restaurants if ratings[r] is None]
            if not available:
                print("¡Ya has probado todos los restaurantes!")
            else:
                new_restaurant = random.choice(available)
                new_rating = get_rating()
                ratings[new_restaurant] = new_rating
                print(f"\nProbaste {new_restaurant} y recibió una calificación de {new_rating} estrellas.\n")

        elif decision == 'explotar':
            # Explotar uno de los conocidos
            known = [r for r in restaurants if ratings[r] is not None]
            if not known:
                print("Aún no has probado ningún restaurante, deberías explorar primero.")
            else:
                best_restaurant = max(known, key=lambda r: ratings[r])
                print(f"\nElegiste {best_restaurant} con una calificación de {ratings[best_restaurant]} estrellas. ¡A disfrutar!\n")

        else:
            print("Por favor, escribe 'explorar', 'explotar' o 'salir'.")

# Ejecutar el programa
restaurant_decision()
