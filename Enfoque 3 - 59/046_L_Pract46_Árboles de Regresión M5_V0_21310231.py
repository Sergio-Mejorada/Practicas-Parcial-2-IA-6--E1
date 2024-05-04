#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 141
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

pip install M5Prime

import pandas as pd
from sklearn.datasets import load_boston
from M5Prime import M5Base

# Cargar el dataset de Boston Housing
boston = load_boston()
df = pd.DataFrame(boston.data, columns=boston.feature_names)
df['target'] = boston.target

# Crear un objeto M5Base para construir el árbol de regresión M5
m5 = M5Base()

# Entrenar el árbol de regresión M5 utilizando el dataset
m5.fit(df, 'target', ['LSTAT', 'RM'])  # Características que se utilizarán para el árbol

# Mostrar el árbol de regresión M5
print("Árbol de Regresión M5:")
print(m5.tree_)
