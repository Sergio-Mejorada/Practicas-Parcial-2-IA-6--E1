#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 81
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

pip install matplotlib


import matplotlib.pyplot as plt

# Datos para el gráfico
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 20, 12]

# Creación del gráfico de línea
plt.plot(x, y)

# Añadir etiquetas y título
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Gráfico de Línea')

# Mostrar el gráfico
plt.show()
