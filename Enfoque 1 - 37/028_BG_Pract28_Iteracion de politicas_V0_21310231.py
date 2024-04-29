#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 28
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

# Creamos una lista de políticas como ejemplo
politicas = [
    {"nombre": "Política A", "tipo": "Privacidad", "estado": "Activa"},
    {"nombre": "Política B", "tipo": "Seguridad", "estado": "Inactiva"},
    {"nombre": "Política C", "tipo": "Acceso", "estado": "Activa"},
    {"nombre": "Política D", "tipo": "Seguridad", "estado": "Activa"}
]

# Iteramos sobre cada política en la lista usando un bucle for
for politica in politicas:
    # Imprimimos información sobre cada política durante la iteración
    print("Nombre:", politica["nombre"])
    print("Tipo:", politica["tipo"])
    print("Estado:", politica["estado"])
    
    # Podemos realizar lógica específica basada en el tipo o estado de la política
    if politica["tipo"] == "Seguridad":
        print("Esta política es de seguridad")
    elif politica["tipo"] == "Privacidad":
        print("Esta política es de privacidad")
    else:
        print("Esta política es de acceso")
    
    if politica["estado"] == "Activa":
        print("Esta política está activa")
    else:
        print("Esta política está inactiva")
    
    # El bucle continuará iterando hasta que todas las políticas en la lista hayan sido procesadas

# Una vez que el bucle ha terminado, se ejecuta cualquier código que esté después del bucle
print("Iteración completa")
