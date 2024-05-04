#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 140
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text

# Cargar el dataset de flores Iris
iris = load_iris()

# Dividir el dataset en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=0)

# Crear un clasificador de árbol de decisión utilizando el algoritmo ID3
tree_classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
tree_classifier.fit(X_train, y_train)

# Mostrar el árbol de decisión generado por el algoritmo ID3
tree_rules = export_text(tree_classifier, feature_names=iris.feature_names)
print("Árbol de Decisión generado por ID3:")
print(tree_rules)

# Evaluar el rendimiento del árbol de decisión utilizando el conjunto de prueba
accuracy = tree_classifier.score(X_test, y_test)
print("\nPrecisión del árbol de decisión:", accuracy)
