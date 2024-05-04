#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 130
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


pip install pyddl


from pyddl import Domain, Problem, Action, State, Planner

# Definir el dominio (enfoque ADL)
domain_parcial = Domain((
    Action('mover', parameters=('x', 'y'), preconditions=('en',), effects=('en', 'en y'),)),
    Action('ver', parameters=('x',), preconditions=('en',), effects=('en',)),
))

# Definir el problema
problem_parcial = Problem(
    domain_parcial,
    init=(('en',),),
    goals=(('en y'),),
)

# Resolver el problema con STRIPS
planner_strips = Planner()
plan_strips = planner_strips.solve(domain_parcial, problem_parcial)

# Resolver el problema con ADL
planner_adl = Planner()
plan_adl = planner_adl.solve(domain_parcial, problem_parcial)

# Imprimir el plan obtenido
print("Plan STRIPS:", plan_strips)
print("Plan ADL:", plan_adl)
