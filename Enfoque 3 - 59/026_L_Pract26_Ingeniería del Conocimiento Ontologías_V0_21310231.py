#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 121
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

# Definir un URI para la ontología y sus clases
onto_uri = URIRef("http://ejemplo.com/ontologia#")
clase_persona = URIRef(onto_uri + "Persona")
clase_empleado = URIRef(onto_uri + "Empleado")

# Definir propiedades
propiedad_nombre = URIRef(onto_uri + "tieneNombre")
propiedad_edad = URIRef(onto_uri + "tieneEdad")
propiedad_puesto = URIRef(onto_uri + "tienePuesto")

# Añadir triples al grafo
g.add((clase_persona, RDF.type, RDFS.Class))
g.add((clase_empleado, RDF.type, RDFS.Class))
g.add((propiedad_nombre, RDF.type, RDF.Property))
g.add((propiedad_edad, RDF.type, RDF.Property))
g.add((propiedad_puesto, RDF.type, RDF.Property))

# Añadir información sobre instancias
persona_juan = URIRef(onto_uri + "Juan")
g.add((persona_juan, RDF.type, clase_persona))
g.add((persona_juan, propiedad_nombre, Literal("Juan Pérez")))
g.add((persona_juan, propiedad_edad, Literal(30)))

empleado_maria = URIRef(onto_uri + "Maria")
g.add((empleado_maria, RDF.type, clase_empleado))
g.add((empleado_maria, propiedad_nombre, Literal("Maria López")))
g.add((empleado_maria, propiedad_edad, Literal(35)))
g.add((empleado_maria, propiedad_puesto, Literal("Gerente")))

# Serializar y mostrar el grafo RDF
print(g.serialize(format='turtle').decode("utf-8"))
