#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 4
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

def dlfs(nodo, grafo, visitado, limite):#Búsqueda en Profundidad Limitada (DLFS por sus siglas en inglés, Depth-Limited Search)
    if limite >= 0:
        if nodo not in visitado:
            print(nodo)  # Aquí podrías realizar cualquier operación con el nodo
            visitado.add(nodo)
            for vecino in grafo[nodo]:
                dlfs(vecino, grafo, visitado, limite - 1)

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
visitado = set()
limite_profundidad = 2
print(f"Recorrido Busqueda en profundidad Limitado a Profundidad {limite_profundidad}:")
dlfs(inicio, grafo, visitado, limite_profundidad)
