#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 145
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

class VersionSpaceAlgorithm:
    def __init__(self, attributes):
        self.attributes = attributes
        self.hypotheses = [{}]

    def update_hypotheses(self, instance, label):
        new_hypotheses = []

        for h in self.hypotheses:
            if self.consistent_with(h, instance, label):
                new_hypotheses.append(h)

        self.hypotheses = new_hypotheses

    def consistent_with(self, hypothesis, instance, label):
        for attr in self.attributes:
            if attr in hypothesis:
                if hypothesis[attr] != instance[attr]:
                    return False
            else:
                hypothesis[attr] = instance[attr]

        return label == 1  # Consideramos que 1 es positivo y 0 es negativo

    def add_instance(self, instance, label):
        self.update_hypotheses(instance, label)

    def get_version_space(self):
        return self.hypotheses

# Ejemplo de uso
attributes = ['Outlook', 'Temperature', 'Humidity', 'Windy']

vs_algorithm = VersionSpaceAlgorithm(attributes)

# Ejemplos de entrenamiento
training_data = [
    {'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Windy': 'False'},  # Positivo
    {'Outlook': 'Sunny', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Windy': 'True'},  # Negativo
    {'Outlook': 'Overcast', 'Temperature': 'Mild', 'Humidity': 'High', 'Windy': 'False'},  # Positivo
    {'Outlook': 'Rainy', 'Temperature': 'Mild', 'Humidity': 'High', 'Windy': 'False'},  # Positivo
]

labels = [1, 0, 1, 1]  # Etiquetas correspondientes a los ejemplos de entrenamiento

# Entrenar el algoritmo AQ con los ejemplos de entrenamiento
for instance, label in zip(training_data, labels):
    vs_algorithm.add_instance(instance, label)

# Obtener el espacio de versiones resultante
version_space = vs_algorithm.get_version_space()

# Imprimir el espacio de versiones
print("Espacio de Versiones:")
for h in version_space:
    print(h)
