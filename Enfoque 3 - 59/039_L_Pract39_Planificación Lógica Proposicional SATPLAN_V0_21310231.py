#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 134
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

pip install python-sat

from pysat.solvers import Glucose3
from pysat.formula import CNF

def satplan(acciones, precondiciones, efectos, estado_inicial, objetivo):
    # Crear un objeto CNF para representar las restricciones del problema
    cnf = CNF()
    
    # Crear una instancia del solucionador SAT
    solver = Glucose3()

    # Agregar cláusulas para las acciones, precondiciones y efectos
    for accion, precondicion, efecto in zip(acciones, precondiciones, efectos):
        # Si una acción se puede aplicar, entonces su efecto debe ser cierto
        cnf.append([-efecto] + [precondicion])
        
        # Si una acción se aplica, entonces su efecto no puede ser falso
        cnf.append([efecto, -precondicion])
        
        # Si una acción se aplica, entonces su efecto no puede ser negativo
        cnf.append([efecto])

    # Agregar cláusulas para el estado inicial y el objetivo
    cnf.append(estado_inicial)
    cnf.append([-x for x in objetivo])

    # Resolver el problema SAT para encontrar un plan
    if solver.solve(cnf):
        plan = []
        for accion in acciones:
            if solver.get_model()[accion]:
                plan.append(accion)
        return plan
    else:
        return None

# Definir acciones, precondiciones y efectos
acciones = ['A', 'B', 'C']
precondiciones = [1, -1, 2]
efectos = [3, -2, -3]

# Definir estado inicial y objetivo
estado_inicial = [1]
objetivo = [3]

# Resolver el problema de planificación con SATPLAN
plan = satplan(acciones, precondiciones, efectos, estado_inicial, objetivo)

# Imprimir el plan obtenido
if plan:
    print("Plan encontrado:", plan)
else:
    print("No se encontró un plan.")
