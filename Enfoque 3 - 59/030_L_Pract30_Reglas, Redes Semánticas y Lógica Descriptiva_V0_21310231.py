#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 125
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


pip install rdflib


from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, RDFS

# Crear un grafo RDF
g = Graph()

# Definir los namespaces
onto_uri = URIRef("http://ejemplo.com/ontologia#")
g.bind("onto", onto_uri)

# Definir clases y propiedades
g.add((onto_uri.Persona, RDF.type, RDFS.Class))
g.add((onto_uri.Edad, RDF.type, RDFS.Class))
g.add((onto_uri.tieneEdad, RDF.type, RDF.Property))

# Agregar instancias y relaciones
g.add((onto_uri.Juan, RDF.type, onto_uri.Persona))
g.add((onto_uri.Juan, onto_uri.tieneEdad, Literal(30)))

# Consulta SPARQL para recuperar la edad de Juan
consulta = """
    PREFIX onto: <http://ejemplo.com/ontologia#>
    SELECT ?edad
    WHERE {
        onto:Juan onto:tieneEdad ?edad .
    }
"""
resultado = g.query(consulta)

# Mostrar el resultado de la consulta
print("Edad de Juan:")
for fila in resultado:
    print(f"Edad: {fila['edad']}")
