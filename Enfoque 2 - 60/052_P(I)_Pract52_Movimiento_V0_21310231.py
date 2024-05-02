#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 87
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


}import cv2

# Inicializar la captura de video desde la cámara
cap = cv2.VideoCapture(0)

# Capturar el primer frame para establecer el fondo
ret, fondo = cap.read()

# Convertir el fondo a escala de grises
fondo_gris = cv2.cvtColor(fondo, cv2.COLOR_BGR2GRAY)

while True:
    # Capturar el frame actual
    ret, frame = cap.read()
    
    # Convertir el frame a escala de grises
    frame_gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Calcular la diferencia absoluta entre el frame actual y el fondo
    diferencia = cv2.absdiff(fondo_gris, frame_gris)
    
    # Aplicar umbralización a la diferencia para obtener la máscara de movimiento
    _, mascara = cv2.threshold(diferencia, 30, 255, cv2.THRESH_BINARY)
    
    # Aplicar
