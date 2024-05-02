#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 109
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


from prologpy import *

# Definir la base de conocimiento
knowledge_base = """
    hombre(socrates).
    mortal(X) :- hombre(X).
"""

# Crear un motor de inferencia Prolog
prolog = Prolog()
prolog.consult(knowledge_base)

# Realizar consultas
for result in prolog.query("mortal(socrates)"):
    print("¿Es Sócrates mortal?", result)

for result in prolog.query("mortal(platon)"):
    print("¿Es Platón mortal?", result)


from clips import Environment, Symbol

# Crear un entorno CLIPS
env = Environment()

# Cargar reglas en el entorno
env.load("clips_rules.clp")

# Definir hechos
env.assert_string("(hombre socrates)")

# Ejecutar el entorno
env.run()

# Obtener resultados
for fact in env.facts():
    if "mortal" in str(fact):
        print("¿Es Sócrates mortal?", fact)
