#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 120
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


pip install clipspy


import clips

# Crear un nuevo entorno CLIPS con FuzzyCLIPS activado
env = clips.Environment()
env.load("fuzzyclips.dll")

# Definir una regla difusa
env.build("(defrule regla-difusa\n"
          "   (temperatura ?t)\n"
          "   =>\n"
          "   (assert (flujo (fuzzy-value 20 50 80)))\n"
          ")")

# Cargar las reglas en el entorno
env.reset()
env.run()

# Obtener el valor inferido para flujo
flujo = env.find_fact("(?f flujo)")
if flujo:
    print("Valor inferido para el flujo:", flujo['fuzzy-value'])
else:
    print("No se encontró un valor inferido para el flujo")
