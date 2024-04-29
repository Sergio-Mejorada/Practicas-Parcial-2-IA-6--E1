#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 71
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import numpy as np
import matplotlib.pyplot as plt

# Generar datos de ejemplo linealmente separables
np.random.seed(0)
class1 = np.random.normal(loc=0, scale=1, size=(100, 2))
class2 = np.random.normal(loc=2, scale=1, size=(100, 2))

# Concatenar las dos clases y crear etiquetas
X = np.concatenate((class1, class2))
y = np.array([0] * 100 + [1] * 100)

# Crear y entrenar el Perceptrón
class Perceptron:
    def __init__(self, learning_rate=0.1, epochs=100):
        self.weights = np.zeros(X.shape[1] + 1)  # Inicializar los pesos, incluyendo el sesgo
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

perceptron = Perceptron()
perceptron.train(X, y)

# Graficar los datos y la línea de separación
plt.scatter(class1[:, 0], class1[:, 1], color='blue', label='Clase 1')
plt.scatter(class2[:, 0], class2[:, 1], color='red', label='Clase 2')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')

# Graficar la línea de separación (hiperplano)
x_values = np.linspace(-2, 4, 100)
y_values = -(perceptron.weights[1] * x_values + perceptron.weights[0]) / perceptron.weights[2]
plt.plot(x_values, y_values, color='green', label='Línea de Separación')

plt.legend()
plt.title('Separabilidad Lineal con Perceptrón')
plt.show()
