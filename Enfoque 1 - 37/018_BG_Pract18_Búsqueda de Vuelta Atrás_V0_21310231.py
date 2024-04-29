#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 17
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

# Búsqueda de Vuelta Atrás (Backtracking)
def es_valida(tablero, fila, columna):
    for i in range(fila):
        if tablero[i] == columna or \
            tablero[i] - i == columna - fila or \
            tablero[i] + i == columna + fila:
            return False
    return True

def colocar_reina(tablero, fila, n):
    if fila == n:
        return [tablero[:]]  # Devolver una copia del tablero como lista de listas
    
    soluciones = []
    for columna in range(n):
        if es_valida(tablero, fila, columna):
            tablero[fila] = columna
            soluciones.extend(colocar_reina(tablero, fila + 1, n))
            tablero[fila] = -1
    
    return soluciones


def resolver_n_reinas(n):
    tablero = [-1] * n
    return colocar_reina(tablero, 0, n)

# Ejemplo de resolución del problema de las 8 reinas
n = 8
solucion = resolver_n_reinas(n)
if solucion:
    print("Solución encontrada:")
    for fila in solucion:
        print(fila)
else:
    print("No se encontró solución.")
