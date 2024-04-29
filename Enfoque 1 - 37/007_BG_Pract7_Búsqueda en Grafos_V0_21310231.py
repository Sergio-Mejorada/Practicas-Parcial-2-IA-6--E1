#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 7
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

# Ejemplo de función heurística (en este caso, distancia euclidiana)
def distancia_euclidiana(nodo, objetivo):
    # Suponiendo que los nodos son coordenadas en un espacio bidimensional
    x1, y1 = nodo
    x2, y2 = objetivo
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Ejemplo de grafo representado como un diccionario de listas de adyacencia
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

inicio = 'A'
objetivo = 'F'

# Ejecutar la búsqueda
if greedy_best_first_search(grafo, inicio, objetivo, distancia_euclidiana):
    print(f"Se encontró un camino desde {inicio} hasta {objetivo}")
else:
    print(f"No se encontró un camino desde {inicio} hasta {objetivo}")


