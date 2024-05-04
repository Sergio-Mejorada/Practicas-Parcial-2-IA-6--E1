#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 133
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

pip install graphplan

from graphplan import GraphPlan

# Definir acciones y su precondición y efecto
acciones = [
    ('A', [], ['en']),
    ('B', ['en'], ['hacer1']),
    ('C', ['en'], ['hacer2']),
    ('D', ['hacer1', 'hacer2'], ['hacer3']),
]

# Crear un objeto GraphPlan y resolver el problema
gp = GraphPlan(acciones)
solucion = gp.solve()

# Imprimir la solución obtenida
if solucion:
    print("Solución encontrada:")
    for nivel, acciones in enumerate(solucion):
        print(f"Nivel {nivel}: {acciones}")
else:
    print("No se encontró solución.")
