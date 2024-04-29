#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 59
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import speech_recognition as sr

# Crear un objeto reconocedor
recognizer = sr.Recognizer()

# Definir la fuente de audio (en este caso, un archivo de audio)
audio_file = "audio.wav"

# Cargar el archivo de audio
with sr.AudioFile(audio_file) as source:
    # Escuchar el archivo de audio y reconocer el habla
    audio_data = recognizer.record(source)
    try:
        # Utilizar Google Web Speech API para el reconocimiento del habla
        texto_reconocido = recognizer.recognize_google(audio_data)
        print("Texto reconocido:", texto_reconocido)
    except sr.UnknownValueError:
        print("No se pudo reconocer el habla")
    except sr.RequestError as e:
        print(f"Error en la solicitud: {e}")
