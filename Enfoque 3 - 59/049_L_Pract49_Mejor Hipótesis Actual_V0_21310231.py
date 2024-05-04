#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 144
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargar el dataset de flores Iris
iris = load_iris()

# Dividir el dataset en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Crear un clasificador KNN con un vecino para demostrar el concepto de "Mejor Hipótesis Actual"
knn = KNeighborsClassifier(n_neighbors=1)  # Utilizamos un vecino para ilustrar el concepto
knn.fit(X_train, y_train)

# Realizar predicciones utilizando el conjunto de prueba
y_pred = knn.predict(X_test)

# Calcular la precisión del clasificador KNN
accuracy = accuracy_score(y_test, y_pred)

print("Precisión del clasificador KNN con 1 vecino:", accuracy)
