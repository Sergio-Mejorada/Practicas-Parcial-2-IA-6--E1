#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 102
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())



# Función para verificar si se puede colocar una reina en una posición específica del tablero
def es_seguro(tablero, fila, columna, N):
    # Verificar si hay otra reina en la misma columna
    for i in range(fila):
        if tablero[i][columna] == 1:
            return False
    
    # Verificar si hay otra reina en la diagonal izquierda superior
    for i, j in zip(range(fila, -1, -1), range(columna, -1, -1)):
        if tablero[i][j] == 1:
            return False
    
    # Verificar si hay otra reina en la diagonal derecha superior
    for i, j in zip(range(fila, -1, -1), range(columna, N)):
        if tablero[i][j] == 1:
            return False
    
    return True

# Función para resolver el problema de las N reinas utilizando backtracking
def resolver_n_reinas(tablero, fila, N):
    # Caso base: todas las reinas han sido colocadas
    if fila >= N:
        return True
    
    for i in range(N):
        # Verificar si es seguro colocar una reina en la posición actual
        if es_seguro(tablero, fila, i, N):
            # Colocar una reina en la posición actual
            tablero[fila][i] = 1
            
            # Resolver recursivamente para la siguiente fila
            if resolver_n_reinas(tablero, fila + 1, N):
                return True
            
            # Si no se puede colocar una reina en la posición actual, retroceder (backtracking)
            tablero[fila][i] = 0
    
    return False

# Función para imprimir el tablero con las reinas colocadas
def imprimir_tablero(tablero):
    for fila in tablero:
        print(fila)

# Ejemplo de uso de backtracking para resolver el problema de las 4 reinas
N = 4
tablero = [[0] * N for _ in range(N)]
if resolver_n_reinas(tablero, 0, N):
    print("Solución encontrada:")
    imprimir_tablero(tablero)
else:
    print("No se encontró solución para el problema de las N reinas.")
