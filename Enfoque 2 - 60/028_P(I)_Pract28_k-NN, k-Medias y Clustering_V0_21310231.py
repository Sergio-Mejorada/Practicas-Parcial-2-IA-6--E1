#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 65
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# Generar datos de ejemplo con dos clústeres
X, y = make_blobs(n_samples=300, centers=2, cluster_std=1.0, random_state=42)

# Crear y entrenar el modelo k-NN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

# Predecir las etiquetas para nuevos puntos
nuevos_puntos = [[-2, -2], [2, 2]]
predicciones = knn.predict(nuevos_puntos)

# Visualizar los datos y las predicciones
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', edgecolors='k')
plt.scatter(nuevos_puntos[:, 0], nuevos_puntos[:, 1], c=predicciones, cmap='viridis', marker='x', s=100, edgecolors='r')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.title('k-NN - Clasificación de Nuevos Puntos')
plt.show()


from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Crear datos de ejemplo
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Crear y entrenar el modelo k-Means
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)

# Obtener las etiquetas de clúster para cada muestra
labels = kmeans.labels_

# Visualizar los datos y los clústeres
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', edgecolors='k')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='x', s=300, c='red', label='Centroides')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.title('k-Means - Agrupamiento de Datos')
plt.legend()
plt.show()

from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt

# Crear datos de ejemplo
X, _ = make_blobs(n_samples=300, centers=3, cluster_std=0.60, random_state=0)

# Crear y entrenar el modelo de clustering aglomerativo
agglomerative = AgglomerativeClustering(n_clusters=3)
agglomerative.fit(X)

# Obtener las etiquetas de clúster para cada muestra
labels = agglomerative.labels_

# Visualizar los datos y los clústeres
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', edgecolors='k')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.title('Clustering Aglomerativo - Agrupamiento de Datos')
plt.show()

