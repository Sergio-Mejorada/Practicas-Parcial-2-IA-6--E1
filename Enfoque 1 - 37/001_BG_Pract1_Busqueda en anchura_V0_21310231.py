#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 1
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

from collections import deque

def bfs(inicio, grafo):
    cola = deque()
    visitado = set()
    
    cola.append(inicio)
    visitado.add(inicio)
    
    while cola:
        nodo_actual = cola.popleft()
        print(nodo_actual)  # Aquí podrías realizar cualquier operación con el nodo
        
        for vecino in grafo[nodo_actual]:
            if vecino not in visitado:
                visitado.add(vecino)
                cola.append(vecino)

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
print("Recorrido BFS:")
bfs(inicio, grafo)
