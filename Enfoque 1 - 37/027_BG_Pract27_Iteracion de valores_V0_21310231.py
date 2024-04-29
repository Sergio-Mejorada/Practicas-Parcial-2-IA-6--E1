#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 27
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

# Definimos una lista de números como ejemplo
numeros = [1, 2, 3, 4, 5]

# Iteramos sobre cada valor en la lista usando un bucle for
for numero in numeros:
    # Imprimimos cada valor durante la iteración
    print(numero)
    # Podemos realizar operaciones o lógica aquí dentro del bucle
    # Por ejemplo, podríamos sumar 1 a cada número e imprimir el resultado
    resultado = numero + 1
    print("Resultado:", resultado)
    # También podríamos verificar si el número es par o impar
    if numero % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")
    # El bucle continuará iterando hasta que todos los elementos de la lista hayan sido procesados

# Una vez que el bucle ha terminado, se ejecuta cualquier código que esté después del bucle
print("Iteración completa")
