#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 108
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


# Función para realizar encadenamiento hacia adelante
def encadenamiento_adelante(base_conocimiento, hechos_iniciales, objetivo):
    hechos_verificados = set(hechos_iniciales)
    
    while True:
        algo_cambio = False
        
        for regla in base_conocimiento:
            antecedentes, consecuente = regla[:-1], regla[-1]
            if all(hecho in hechos_verificados for hecho in antecedentes) and consecuente not in hechos_verificados:
                hechos_verificados.add(consecuente)
                algo_cambio = True
        
        if algo_cambio == False:
            break
    
    return objetivo in hechos_verificados, hechos_verificados

# Ejemplo de uso del encadenamiento hacia adelante
base_conocimiento = [
    (['A'], 'B'),
    (['B'], 'C'),
    (['C'], 'D')
]
hechos_iniciales = ['A']
objetivo = 'D'

resultado, hechos_verificados = encadenamiento_adelante(base_conocimiento, hechos_iniciales, objetivo)

print("Resultado del encadenamiento hacia adelante:", resultado)
print("Hechos verificados:", hechos_verificados)


# Función para realizar encadenamiento hacia atrás
def encadenamiento_atras(base_conocimiento, objetivo, hechos_iniciales):
    if objetivo in hechos_iniciales:
        return True, set(hechos_iniciales)
    
    for regla in base_conocimiento:
        antecedentes, consecuente = regla[:-1], regla[-1]
        if consecuente == objetivo:
            todos_verificados = True
            nuevos_hechos_verificados = set(hechos_iniciales)
            
            for antecedente in antecedentes:
                resultado, hechos_verificados = encadenamiento_atras(base_conocimiento, antecedente, hechos_iniciales)
                todos_verificados = todos_verificados and resultado
                nuevos_hechos_verificados.update(hechos_verificados)
            
            if todos_verificados:
                return True, nuevos_hechos_verificados
    
    return False, set(hechos_iniciales)

# Ejemplo de uso del encadenamiento hacia atrás
base_conocimiento = [
    (['A'], 'B'),
    (['B'], 'C'),
    (['C'], 'D')
]
hechos_iniciales = ['A']
objetivo = 'D'

resultado, hechos_verificados = encadenamiento_atras(base_conocimiento, objetivo, hechos_iniciales)

print("Resultado del encadenamiento hacia atrás:", resultado)
print("Hechos verificados:", hechos_verificados)
