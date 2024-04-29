#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 76
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

import nltk
from nltk.corpus import reuters

nltk.download('reuters')
corpus = reuters.sents()  # Obtenemos las oraciones del corpus Reuters


# Concatenamos todas las oraciones en una lista de palabras
corpus_words = [word.lower() for sent in corpus for word in sent]


from nltk import TrigramCollocationFinder, TrigramAssocMeasures

# Creamos un buscador de trigramas y calculamos las frecuencias
finder = TrigramCollocationFinder.from_words(corpus_words)
trigram_freqs = finder.ngram_fd

# Creamos el modelo de trigramas con su frecuencia relativa
trigram_pml = {trigram: freq / corpus_words.count(trigram[0]) for trigram, freq in trigram_freqs.items()}


def pml_probability(sequence, model):
    """
    Calcula la probabilidad de ocurrencia de una secuencia de palabras dada un modelo PML.

    Args:
    - sequence: La secuencia de palabras como lista.
    - model: El modelo PML creado.

    Returns:
    La probabilidad de ocurrencia de la secuencia dada el modelo.
    """
    prob = 1.0
    for i in range(2, len(sequence)):
        trigram = tuple(sequence[i - 2: i + 1])
        if trigram in model:
            prob *= model[trigram]
    return prob

# Ejemplo de uso:
sentence = ["the", "price", "of", "oil"]
sentence_prob = pml_probability(sentence, trigram_pml)
print("Probabilidad de la secuencia:", sentence_prob)
