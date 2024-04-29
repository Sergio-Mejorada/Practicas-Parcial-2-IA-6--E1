#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 3
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

def dfs(nodo, grafo, visitado): #Búsqueda en Profundidad (DFS por sus siglas en inglés, Depth-First Search) 
    if nodo not in visitado:
        print(nodo)  # Aquí podrías realizar cualquier operación con el nodo
        visitado.add(nodo)
        for vecino in grafo[nodo]:
            dfs(vecino, grafo, visitado)

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
print("Recorrido de Busqueda de profundidad:")
dfs(inicio, grafo, visitado)
