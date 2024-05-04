#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 113
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-

class SistemaDiagnostico:
    def __init__(self):
        self.reglas_diagnosticos = {
            "faringitis": ["fiebre", "dolor de garganta"],
            "sarampion": ["fiebre", "erupcion cutanea"]
        }

    def diagnosticar_sintomas(self, sintomas):
        for enfermedad, condiciones in self.reglas_diagnosticos.items():
            if all(condicion in sintomas for condicion in condiciones):
                return enfermedad
        return "No se pudo diagnosticar la enfermedad"


# Crear una instancia del sistema de diagnóstico
sistema = SistemaDiagnostico()

# Síntomas del paciente
sintomas_paciente = ["fiebre", "dolor de garganta"]

# Diagnosticar enfermedad
enfermedad_diagnosticada = sistema.diagnosticar_sintomas(sintomas_paciente)
print("Enfermedad diagnosticada:", enfermedad_diagnosticada)
