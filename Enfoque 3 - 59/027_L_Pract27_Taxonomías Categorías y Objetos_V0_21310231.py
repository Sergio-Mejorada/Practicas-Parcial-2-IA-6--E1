#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 122
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


# Definir la taxonomía como un diccionario
taxonomia = {
    "Animales": {
        "Mamíferos": ["Perro", "Gato", "Elefante"],
        "Aves": ["Pato", "Águila", "Pingüino"]
    },
    "Frutas": {
        "Cítricos": ["Naranja", "Limón", "Mandarina"],
        "Tropicales": ["Piña", "Mango", "Papaya"]
    }
}

# Mostrar la taxonomía completa
print("Taxonomía completa:")
for categoria, subcategorias in taxonomia.items():
    print(f"- {categoria}:")
    for subcategoria, objetos in subcategorias.items():
        print(f"  - {subcategoria}: {', '.join(objetos)}")

# Obtener objetos de una categoría específica
categoria_seleccionada = "Frutas"
if categoria_seleccionada in taxonomia:
    objetos_categoria = [objeto for subcategorias in taxonomia[categoria_seleccionada].values() for objeto in subcategorias]
    print(f"\nObjetos en la categoría '{categoria_seleccionada}': {', '.join(objetos_categoria)}")
else:
    print(f"\nLa categoría '{categoria_seleccionada}' no se encuentra en la taxonomía")
