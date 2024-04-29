#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 73
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import numpy as np

# Definir las funciones de activación y sus derivadas
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

# Definir la estructura de la red neuronal
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, learning_rate):
        # Inicializar los pesos y sesgos de las capas ocultas y de salida
        self.weights_hidden = np.random.randn(input_size, hidden_size)
        self.bias_hidden = np.zeros((1, hidden_size))
        self.weights_output = np.random.randn(hidden_size, output_size)
        self.bias_output = np.zeros((1, output_size))
        # Tasa de aprendizaje
        self.learning_rate = learning_rate

    def forward_propagation(self, inputs):
        # Calcular las salidas de las capas ocultas y de salida
        self.hidden_output = sigmoid(np.dot(inputs, self.weights_hidden) + self.bias_hidden)
        self.output = sigmoid(np.dot(self.hidden_output, self.weights_output) + self.bias_output)

    def backward_propagation(self, inputs, targets):
        # Calcular el error y las derivadas para actualizar los pesos y sesgos
        error = targets - self.output
        output_delta = error * sigmoid_derivative(self.output)
        hidden_error = np.dot(output_delta, self.weights_output.T)
        hidden_delta = hidden_error * sigmoid_derivative(self.hidden_output)
        # Actualizar los pesos y sesgos
        self.weights_output += np.dot(self.hidden_output.T, output_delta) * self.learning_rate
        self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * self.learning_rate
        self.weights_hidden += np.dot(inputs.T, hidden_delta) * self.learning_rate
        self.bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * self.learning_rate

    def train(self, inputs, targets, epochs):
        for _ in range(epochs):
            self.forward_propagation(inputs)
            self.backward_propagation(inputs, targets)

# Datos de ejemplo para entrenamiento
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
targets = np.array([[0], [1], [1], [0]])

# Crear y entrenar la red neuronal
nn = NeuralNetwork(input_size=2, hidden_size=4, output_size=1, learning_rate=0.1)
nn.train(inputs, targets, epochs=10000)

# Mostrar las salidas después del entrenamiento
nn.forward_propagation(inputs)
print("Salidas después del entrenamiento:")
print(nn.output)
