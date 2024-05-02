#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 85
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

# Cargar y preparar el conjunto de datos MNIST (dígitos escritos a mano)
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Normalizar los valores de píxeles al rango [0, 1]
train_images, test_images = train_images / 255.0, test_images / 255.0

# Expandir las dimensiones de las imágenes para que coincidan con el formato de entrada de la CNN
train_images = train_images[..., tf.newaxis]
test_images = test_images[..., tf.newaxis]

# Convertir las etiquetas a formato one-hot
train_labels = to_categorical(train_labels, num_classes=10)
test_labels = to_categorical(test_labels, num_classes=10)

# Crear el modelo de red neuronal convolucional (CNN)
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activati
