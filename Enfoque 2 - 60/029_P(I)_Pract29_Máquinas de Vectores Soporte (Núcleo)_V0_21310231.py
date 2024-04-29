#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 66
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import matplotlib.pyplot as plt

# Generar datos de ejemplo
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, random_state=42)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo SVM con núcleo (RBF Kernel)
svm_model = SVC(kernel='rbf', C=1.0, gamma='scale')
svm_model.fit(X_train, y_train)

# Calcular la precisión del modelo en el conjunto de prueba
accuracy = svm_model.score(X_test, y_test)
print("Precisión del modelo:", accuracy)

# Visualizar los datos y las fronteras de decisión
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', edgecolors='k')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.title('SVM con Núcleo (RBF Kernel) - Fronteras de Decisión')
plt.legend()
plt.show()
