#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 128
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


pip install pyknow


from pyknow import *

# Define un hecho (hecho inicial)
class Sintomas(Fact):
    pass

# Define la regla del sistema experto
class DiagnosticoES(KnowledgeEngine):
    @Rule(Sintomas(fiebre=P(lambda x: x >= 38.0)))
    def tiene_fiebre(self):
        print("El paciente tiene fiebre.")
        self.declare(Sintomas(diagnostico="Posible infección"))

    @Rule(Sintomas(fiebre=P(lambda x: x < 38.0)))
    def no_tiene_fiebre(self):
        print("El paciente no tiene fiebre.")
        self.declare(Sintomas(diagnostico="Sin infección"))

# Función para ejecutar el sistema experto
def ejecutar_sistema_experto(fiebre):
    engine = DiagnosticoES()
    engine.reset()
    engine.declare(Sintomas(fiebre=fiebre))
    engine.run()

# Ejemplo de uso
fiebre = 37.5
ejecutar_sistema_experto(fiebre)
