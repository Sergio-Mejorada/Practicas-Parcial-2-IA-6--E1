#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 70
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


import numpy as np

class Perceptron:
    def __init__(self, n_inputs, learning_rate=0.1, epochs=100):
        self.weights = np.zeros(n_inputs + 1)  # Inicializar los pesos, incluyendo el sesgo
        self.learning_rate = learning_rate  # Tasa de aprendizaje
        self.epochs = epochs  # Número de iteraciones de entrenamiento

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]  # Suma ponderada más el sesgo
        return 1 if summation > 0 else 0  # Función de activación escalón unitario

    def train(self, training_inputs, labels):
        for _ in range(self.epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs  # Actualizar los pesos
                self.weights[0] += self.learning_rate * (label - prediction)  # Actualizar el sesgo

class Adaline:
    def __init__(self, n_inputs, learning_rate=0.01, epochs=100):
        self.weights = np.random.randn(n_inputs + 1)  # Inicializar los pesos, incluyendo el sesgo
        self.learning_rate = learning_rate  # Tasa de aprendizaje
        self.epochs = epochs  # Número de iteraciones de entrenamiento

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]  # Suma ponderada más el sesgo
        return summation  # Función de activación lineal

    def train(self, training_inputs, labels):
        for _ in range(self.epochs):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)
                error = label - prediction
                self.weights[1:] += self.learning_rate * error * inputs  # Actualizar los pesos
                self.weights[0] += self.learning_rate * error  # Actualizar el sesgo

class Madaline:
    def __init__(self, n_inputs, n_outputs, learning_rate=0.01, epochs=100):
        self.layers = [Adaline(n_inputs, learning_rate, epochs) for _ in range(n_outputs)]

    def predict(self, inputs):
        return np.array([layer.predict(inputs) for layer in self.layers])

    def train(self, training_inputs, labels):
        for layer, label in zip(self.layers, labels):
            layer.train(training_inputs, label)

