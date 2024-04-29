#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 63
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Generar datos de ejemplo con 3 grupos/clústeres
X, _ = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)

# Crear y entrenar el modelo K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X)

# Obtener las etiquetas de los clústeres y los centroides
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

# Visualizar los datos y los clústeres
plt.figure(figsize=(8, 6))
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', edgecolors='k')
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=300, c='red', label='Centroides')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.title('Agrupamiento No Supervisado - K-Means')
plt.legend()
plt.show()
