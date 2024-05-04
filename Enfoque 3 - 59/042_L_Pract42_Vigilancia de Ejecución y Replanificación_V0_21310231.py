#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 137
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


class Planificador:
    def __init__(self, acciones):
        self.acciones = acciones

    def ejecutar_plan(self):
        for accion in self.acciones:
            print(f"Ejecutando acción: {accion}")
            # Simular ejecución de la acción
            # Aquí podrías agregar lógica para verificar el estado de la acción ejecutada

    def replanificar(self, cambios):
        print("Se detectaron cambios en el entorno. Replanificando...")
        # Aquí podrías implementar la lógica de replanificación basada en los cambios detectados

# Crear un planificador con un conjunto inicial de acciones
planificador = Planificador(["Accion1", "Accion2", "Accion3"])

# Ejecutar el plan inicial
planificador.ejecutar_plan()

# Simular cambios en el entorno que requieren replanificación
cambios_entorno = True

if cambios_entorno:
    planificador.replanificar(cambios_entorno)
    # Ejecutar el nuevo plan generado después de la replanificación
    nuevo_plan = ["Accion4", "Accion5"]
    planificador.acciones = nuevo_plan
    planificador.ejecutar_plan()
