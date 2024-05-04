#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 132
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

pip install pyddl


from pyddl import Domain, Problem, Action, State, Planner

# Definir el dominio para la planificación de orden parcial
domain_orden_parcial = Domain((
    Action('accion1', preconditions=('en',), effects=('hacer1',)),
    Action('accion2', preconditions=('en',), effects=('hacer2',)),
    Action('accion3', preconditions=('en',), effects=('hacer3',)),
    Action('accion4', preconditions=('en',), effects=('hacer4',)),
    Action('accion5', preconditions=('hacer2', 'hacer3'), effects=('hacer5',)),
))

# Definir el problema
problem_orden_parcial = Problem(
    domain_orden_parcial,
    init=(('en',),),
    goals=(('hacer5'),),
)

# Resolver el problema de orden parcial
planner_orden_parcial = Planner()
plan_orden_parcial = planner_orden_parcial.solve(domain_orden_parcial, problem_orden_parcial)

# Imprimir el plan obtenido
print("Plan de orden parcial:", plan_orden_parcial)
