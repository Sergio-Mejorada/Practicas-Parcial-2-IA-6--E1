#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 80
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


import nltk
from nltk.translate import IBMModel1

# Ejemplo de textos en dos idiomas (inglés y español)
english_sentences = [
    "the cat is on the mat",
    "she speaks Spanish"
]

spanish_sentences = [
    "el gato está en la alfombra",
    "ella habla español"
]

# Tokenización de los textos
english_tokenized = [nltk.word_tokenize(sent) for sent in english_sentences]
spanish_tokenized = [nltk.word_tokenize(sent) for sent in spanish_sentences]

# Entrenamiento del modelo de traducción automática IBM Model 1
ibm_model1 = IBMModel1(english_tokenized, spanish_tokenized, 10)

# Traducción de un texto de ejemplo del inglés al español
example_text = "the cat is on the mat"
translated_text = ibm_model1.translate(nltk.word_tokenize(example_text))

print("Texto original en inglés:", example_text)
print("Texto traducido al español:", " ".join(translated_text))
