#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 75
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


def hamming_distance(s1, s2):
    """
    Calcula la distancia de Hamming entre dos cadenas binarias.

    Args:
    - s1: Primera cadena binaria.
    - s2: Segunda cadena binaria.

    Returns:
    La distancia de Hamming entre las cadenas s1 y s2.
    """
    if len(s1) != len(s2):
        raise ValueError("Las cadenas deben tener la misma longitud.")
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

# Ejemplo de uso:
cadena1 = "101010"
cadena2 = "110011"
distancia = hamming_distance(cadena1, cadena2)
print("Distancia de Hamming:", distancia)


import numpy as np

class HopfieldNetwork:
    def __init__(self, pattern_size):
        """
        Inicializa una red de Hopfield.

        Args:
        - pattern_size: Tamaño de los patrones a almacenar.
        """
        self.pattern_size = pattern_size
        self.weights = np.zeros((pattern_size, pattern_size))

    def train(self, patterns):
        """
        Entrena la red de Hopfield con los patrones dados.

        Args:
        - patterns: Lista de patrones binarios (matriz numpy).
        """
        for pattern in patterns:
            pattern = np.array(pattern).reshape(-1, 1)
            self.weights += np.dot(pattern, pattern.T)
            np.fill_diagonal(self.weights, 0)

    def recall(self, input_pattern, max_iterations=100):
        """
        Recupera un patrón almacenado dado un patrón de entrada.

        Args:
        - input_pattern: Patrón de entrada binario (matriz numpy).
        - max_iterations: Número máximo de iteraciones para convergencia.

        Returns:
        El patrón recuperado (matriz numpy).
        """
        for _ in range(max_iterations):
            activation = np.dot(self.weights, input_pattern)
            output_pattern = np.where(activation > 0, 1, -1)
            if np.array_equal(output_pattern, input_pattern):
                return output_pattern
            input_pattern = output_pattern
        raise RuntimeError("La red no ha convergido después de {} iteraciones.".format(max_iterations))

# Ejemplo de uso:
patterns = [
    [1, -1, 1],
    [-1, 1, -1],
    [1, 1, 1]
]

hopfield_net = HopfieldNetwork(pattern_size=3)
hopfield_net.train(patterns)

input_pattern = np.array([1, 1, -1]).reshape(-1, 1)
output_pattern = hopfield_net.recall(input_pattern)
print("Patrón recuperado:", output_pattern.flatten())


import numpy as np

def hebb_rule(inputs, targets):
    """
    Aplica la regla de Hebb para aprender los pesos sinápticos.

    Args:
    - inputs: Matriz de entradas.
    - targets: Matriz de objetivos.

    Returns:
    La matriz de pesos sinápticos calculada con la regla de Hebb.
    """
    num_inputs, num_neurons = inputs.shape
    weights = np.zeros((num_inputs, num_neurons))
    for i in range(num_inputs):
        for j in range(num_neurons):
            weights[i, j] = sum(inputs[i, k] * targets[k, j] for k in range(num_neurons))
    return weights

# Ejemplo de uso:
inputs = np.array([[1, 0, 1], [0, 1, 1]])
targets = np.array([[1, 0], [0, 1], [1, 1]])
weights = hebb_rule(inputs, targets)
print("Pesos sinápticos aprendidos:")
print(weights)

import torch
import torch.nn as nn

class RBM(nn.Module):
    def __init__(self, visible_size, hidden_size):
        super(RBM, self).__init__()
        self.visible_size = visible_size
        self.hidden_size = hidden_size
        self.W = nn.Parameter(torch.randn(visible_size, hidden_size))
        self.b_v = nn.Parameter(torch.randn(visible_size))
        self.b_h = nn.Parameter(torch.randn(hidden_size))

    def forward(self, v):
        h = torch.sigmoid(torch.matmul(v, self.W) + self.b_h)
        return h, torch.bernoulli(h)

    def backward(self, h):
        v = torch.sigmoid(torch.matmul(h, self.W.T) + self.b_v)
        return v, torch.bernoulli(v)

# Ejemplo de uso:
visible_size = 4
hidden_size = 3
rbm = RBM(visible_size, hidden_size)
v = torch.tensor([[1, 0, 1, 0]], dtype=torch.float32)
h, _ = rbm.forward(v)
reconstructed_v, _ = rbm.backward(h)
print("Patrón de entrada:", v)
print("Patrón reconstruido:", reconstructed_v)
