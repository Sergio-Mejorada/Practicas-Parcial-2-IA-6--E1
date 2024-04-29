#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 16
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

#Problemas de Satisfacción de Restricciones (CSP, por sus siglas en inglés)
def resolver_csp():
    for a in range(2):
        for b in range(2):
            for c in range(2):
                if a + b + c == 2:
                    return (a, b, c)
    return None

# Ejecutar la función para resolver el CSP
solucion = resolver_csp()
print("Solución encontrada:", solucion)

