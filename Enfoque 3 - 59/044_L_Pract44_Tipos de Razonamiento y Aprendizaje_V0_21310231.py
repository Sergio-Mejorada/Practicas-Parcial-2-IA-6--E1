#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 139
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

pip install scikit-learn pandas

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans

# Cargar el dataset de flores Iris
iris = load_iris()

# Convertir el dataset en un DataFrame de pandas
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Aprendizaje supervisado: Clasificador de vecinos más cercanos (K-Nearest Neighbors)
X_train, X_test, y_train, y_test = train_test_split(df[iris.feature_names], df['target'], random_state=0)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# Predicciones
predicciones = knn.predict(X_test)

# Imprimir las predicciones y el rendimiento del clasificador
print("Predicciones del clasificador KNN:")
print(predicciones)
print("Precisión del clasificador KNN:", knn.score(X_test, y_test))

# Aprendizaje no supervisado: Algoritmo de clustering K-Means
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(df[iris.feature_names])

# Imprimir los centroides de los clusters y las etiquetas de cluster asignadas a cada muestra
print("\nCentroides de los clusters:")
print(kmeans.cluster_centers_)
print("Etiquetas de cluster asignadas:")
print(kmeans.labels_)
