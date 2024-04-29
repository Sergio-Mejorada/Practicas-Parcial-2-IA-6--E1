#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 8
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())
import heapq

def a_estrella(grafo, inicio, objetivo, heuristica):
    cola_prioridad = [(0, inicio)]
    visitado = set()
    costo_acumulado = {inicio: 0}
    
    while cola_prioridad:
        costo, nodo_actual = heapq.heappop(cola_prioridad)
        
        if nodo_actual == objetivo:
            return True  # Se encontró el objetivo
        
        if nodo_actual in visitado:
            continue
        
        visitado.add(nodo_actual)
        
        for vecino, costo_arista in grafo[nodo_actual]:
            nuevo_costo = costo_acumulado[nodo_actual] + costo_arista
            if vecino not in costo_acumulado or nuevo_costo < costo_acumulado[vecino]:
                costo_acumulado[vecino] = nuevo_costo
                heapq.heappush(cola_prioridad, (nuevo_costo + heuristica(vecino, objetivo), vecino))
    
    return False  # No se encontró el objetivo
