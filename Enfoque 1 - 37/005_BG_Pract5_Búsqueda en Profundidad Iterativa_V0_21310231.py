#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 5
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())
def dfs_limitado(nodo, grafo, visitado, limite):#Búsqueda en Profundidad Iterativa (IDFS por sus siglas en inglés, Iterative Deepening Depth-First Search)
    if limite == 0:
        return
    if nodo not in visitado:
        print(nodo)  # Aquí podrías realizar cualquier operación con el nodo
        visitado.add(nodo)
        for vecino in grafo[nodo]:
            dfs_limitado(vecino, grafo, visitado, limite - 1)

def idfs(inicio, grafo, limite_max):
    for profundidad_limite in range(limite_max + 1):
        visitado = set()
        print(f"Recorrido en Busqueda en profundidad iterativa con límite de profundidad {profundidad_limite}:")
        dfs_limitado(inicio, grafo, visitado, profundidad_limite)

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
limite_max = 2
idfs(inicio, grafo, limite_max)
