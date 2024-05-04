#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 143
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargar el dataset de flores Iris
iris = load_iris()

# Dividir el dataset en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

# Crear un clasificador de árbol de decisión
decision_tree = DecisionTreeClassifier(random_state=42)
decision_tree.fit(X_train, y_train)

# Realizar predicciones utilizando el conjunto de prueba
y_pred = decision_tree.predict(X_test)

# Calcular la precisión del clasificador
accuracy = accuracy_score(y_test, y_pred)

print("Precisión del clasificador de Árbol de Decisión:", accuracy)


# Definir una función ficticia para simular un árbol de decisión "K-DT"
def k_decision_tree(X_train, y_train, X_test):
    # Lógica de división múltiple en cada nodo (ficticia)
    y_pred = []  # Lista para almacenar las predicciones

    for muestra in X_test:
        # Lógica de decisión ficticia para simular un árbol "K-DT"
        if muestra[0] < 5:
            y_pred.append(0)
        elif muestra[1] < 3:
            y_pred.append(1)
        else:
            y_pred.append(2)

    return y_pred

# Utilizar la función ficticia para realizar predicciones
y_pred_kdt = k_decision_tree(X_train, y_train, X_test)

# Calcular la precisión del clasificador "K-DT" (ficticio)
accuracy_kdt = accuracy_score(y_test, y_pred_kdt)

print("Precisión del clasificador de Árbol de Decisión 'K-DT' (ficticio):", accuracy_kdt)
