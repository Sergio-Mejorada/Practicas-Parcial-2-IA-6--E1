#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 154
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())

pip install scikit-learn


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from nltk import CFG, ChartParser

# Definir ejemplos de entrada y salida para la inducción gramatical
ejemplos_entrada = ['the cat chased the mouse',
                    'the dog barked at the cat',
                    'the bird flew away',
                    'the mouse ate the cheese']

ejemplos_salida = ['S -> NP VP',
                   'S -> NP VP',
                   'S -> NP VP',
                   'S -> NP VP']

# Crear un pipeline para el proceso de inducción gramatical
pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', RandomForestClassifier())
])

# Dividir los ejemplos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(ejemplos_entrada, ejemplos_salida, test_size=0.2, random_state=42)

# Entrenar el pipeline utilizando los ejemplos de entrada y salida
pipeline.fit(X_train, y_train)

# Realizar predicciones sobre ejemplos de prueba
predicciones = pipeline.predict(X_test)

# Calcular la precisión de las predicciones
precision = accuracy_score(y_test, predicciones)

# Imprimir la precisión de la inducción gramatical
print(f"Precisión de la inducción gramatical: {precision}")

# Extraer la gramática inductiva aprendida
gramatica_inductiva = CFG.fromstring(predicciones)

# Imprimir la gramática inductiva aprendida
print("Gramática Inductiva Aprendida:")
print(gramatica_inductiva)

# Ejemplo de uso de la gramática inductiva aprendida
entrada_nueva = 'the bird sang a song'
parser = ChartParser(gramatica_inductiva)
for tree in parser.parse(entrada_nueva.split()):
    print(tree)
