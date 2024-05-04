#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 131
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


from collections import deque

# Definir la clase para representar un estado en el espacio de estados
class Estado:
    def __init__(self, nombre, adyacentes=None):
        self.nombre = nombre
        self.adyacentes = adyacentes if adyacentes is not None else []

# Implementar la función de búsqueda en amplitud (BFS)
def bfs(estado_inicial, estado_objetivo):
    cola = deque([(estado_inicial, [estado_inicial])])  # Inicializar la cola con el estado inicial y el camino hasta ahora
    visitados = set()  # Conjunto para mantener los estados visitados

    while cola:
        estado_actual, camino = cola.popleft()  # Obtener el estado y el camino actual desde la cola
        if estado_actual.nombre == estado_objetivo.nombre:  # Si encontramos el estado objetivo, retornar el camino
            return camino
        visitados.add(estado_actual)  # Marcar el estado actual como visitado

        # Expandir el estado actual agregando sus estados adyacentes a la cola
        for adyacente in estado_actual.adyacentes:
            if adyacente not in visitados:  # Evitar estados visitados
                nueva_ruta = list(camino)  # Crear una nueva lista para la nueva ruta
                nueva_ruta.append(adyacente)  # Agregar el estado adyacente a la nueva ruta
                cola.append((adyacente, nueva_ruta))  # Agregar el estado adyacente y su nueva ruta a la cola

    return None  # Retornar None si no se encuentra un camino

# Crear los estados y definir sus adyacentes para representar el grafo
A = Estado("A")
B = Estado("B")
C = Estado("C")
D = Estado("D")
E = Estado("E")

A.adyacentes = [B, C]
B.adyacentes = [A, D, E]
C.adyacentes = [A]
D.adyacentes = [B, E]
E.adyacentes = [B, D]

# Definir el estado inicial y el estado objetivo
estado_inicial = A
estado_objetivo = D

# Ejecutar la búsqueda en amplitud (BFS) para encontrar el camino más corto
camino_mas_corto = bfs(estado_inicial, estado_objetivo)

# Imprimir el camino más corto encontrado
if camino_mas_corto:
    camino_nombres = [estado.nombre for estado in camino_mas_corto]
    print("Camino más corto:", camino_nombres)
else:
    print("No se encontró un camino desde el estado inicial al estado objetivo.")
