#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 82
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    'Nombre': ['Alice', 'Bob', 'Charlie', 'David', 'Emily', None],
    'Edad': [25, 30, 35, None, 40, 45],
    'Ciudad': ['New York', 'Los Angeles', 'Chicago', 'Miami', 'San Francisco', 'Boston']
}
df = pd.DataFrame(data)

# Imprimir el DataFrame original
print("DataFrame original:")
print(df)

# Filtrar filas con datos nulos en la columna 'Edad'
df_filtrado_nulos = df[df['Edad'].notnull()]

# Imprimir el DataFrame filtrado por nulos
print("\nDataFrame filtrado por datos nulos en 'Edad':")
print(df_filtrado_nulos)

# Filtrar filas con edad mayor o igual a 35
df_filtrado_edad = df[df['Edad'] >= 35]

# Imprimir el DataFrame filtrado por edad
print("\nDataFrame filtrado por edad mayor o igual a 35:")
print(df_filtrado_edad)

# Seleccionar solo las columnas 'Nombre' y 'Ciudad'
df_seleccionado_columnas = df[['Nombre', 'Ciudad']]

# Imprimir el DataFrame con columnas seleccionadas
print("\nDataFrame con columnas 'Nombre' y 'Ciudad' seleccionadas:")
print(df_seleccionado_columnas)
