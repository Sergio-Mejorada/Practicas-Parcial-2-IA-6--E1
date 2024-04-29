#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 25
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

def calcular_voi(valor_informacion, rendimiento_sin_info):
    rendimiento_con_info = rendimiento_sin_info + valor_informacion
    voi = rendimiento_con_info - rendimiento_sin_info
    return voi

# Rendimiento esperado de las acciones sin información adicional
rendimiento_sin_info_A = 1000
rendimiento_sin_info_B = 800

# Rendimiento esperado de las acciones con información adicional
rendimiento_con_info_A = 1200
rendimiento_con_info_B = 900

# Calcular el valor de la información para cada acción
voi_A = calcular_voi(rendimiento_con_info_A - rendimiento_sin_info_A, rendimiento_sin_info_A)
voi_B = calcular_voi(rendimiento_con_info_B - rendimiento_sin_info_B, rendimiento_sin_info_B)

# Imprimir los resultados
print("Valor de la información para la acción A:", voi_A)
print("Valor de la información para la acción B:", voi_B)
