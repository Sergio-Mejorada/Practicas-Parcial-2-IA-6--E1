#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 72
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


pip install tensorflow keras


import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical

# Cargar y preprocesar los datos de MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0  # Normalizar los datos

# Convertir las etiquetas a one-hot encoding
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

# Construir el modelo de red neuronal multicapa
model = Sequential([
    Flatten(input_shape=(28, 28)),  # Capa de aplanamiento para convertir las imágenes 2D en un vector 1D
    Dense(128, activation='relu'),  # Primera capa oculta con 128 neuronas y activación ReLU
    Dense(64, activation='relu'),   # Segunda capa oculta con 64 neuronas y activación ReLU
    Dense(10, activation='softmax') # Capa de salida con 10 neuronas (una por cada clase) y activación Softmax
])

# Compilar el modelo con la función de pérdida, optimizador y métricas
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

# Entrenar el modelo con los datos de entrenamiento
model.fit(x_train, y_train, epochs=5, batch_size=32, validation_data=(x_test, y_test))

# Evaluar el modelo con los datos de prueba
test_loss, test_acc = model.evaluate(x_test, y_test)
print("Precisión del modelo en datos de prueba:", test_acc)
