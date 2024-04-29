#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 74
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


import numpy as np
import matplotlib.pyplot as plt

# Definir la clase del Mapa Autoorganizado de Kohonen (SOM)
class KohonenMap:
    def __init__(self, input_shape, map_shape, learning_rate=0.1, sigma=1.0):
        self.input_shape = input_shape  # Dimensionalidad de los datos de entrada
        self.map_shape = map_shape  # Dimensiones del mapa SOM
        self.learning_rate = learning_rate  # Tasa de aprendizaje
        self.sigma = sigma  # Parámetro sigma para el vecindario

        # Inicializar pesos aleatorios para cada neurona del mapa
        self.weights = np.random.random((map_shape[0], map_shape[1], input_shape))

    def update_weights(self, input_vector, winner):
        # Calcular la distancia euclidiana entre el vector de entrada y los pesos de todas las neuronas
        distances = np.linalg.norm(self.weights - input_vector, axis=2)
        # Encontrar la neurona ganadora (la más cercana al vector de entrada)
        winner_coords = np.unravel_index(np.argmin(distances), distances.shape)

        # Actualizar los pesos de todas las neuronas basándose en la neurona ganadora y su vecindario
        for i in range(self.map_shape[0]):
            for j in range(self.map_shape[1]):
                distance_to_winner = np.linalg.norm(np.array([i, j]) - np.array(winner_coords))
                neighborhood_factor = np.exp(-distance_to_winner / (2 * self.sigma**2))
                self.weights[i, j] += self.learning_rate * neighborhood_factor * (input_vector - self.weights[i, j])

    def train(self, input_data, epochs):
        for epoch in range(epochs):
            for input_vector in input_data:
                self.update_weights(input_vector, epoch / epochs)

    def visualize(self):
        plt.imshow(self.weights)
        plt.title('Mapa Autoorganizado de Kohonen')
        plt.colorbar()
        plt.show()

# Datos de ejemplo (2D)
input_data = np.array([[0.2, 0.8], [0.3, 0.6], [0.5, 0.4], [0.7, 0.3]])

# Crear e inicializar el mapa SOM
map_shape = (5, 5)  # Dimensiones del mapa SOM
input_shape = input_data.shape[1]  # Dimensionalidad de los datos de entrada
som = KohonenMap(input_shape, map_shape)

# Entrenar el mapa SOM con los datos de ejemplo
epochs = 100
som.train(input_data, epochs)

# Visualizar el mapa SOM
som.visualize()
