#Sergio Alejandro Mejorada Gonzalez
#21310231  5° E1
#Practica 152
# _*_ codificación: cp1252 _*_
# _*_ cdoing: 850 _*_
# _*_ codificación: utf-8 _*_
mensaje = "Bienvenido a python su majestad."
print(mensaje.title())


% Definir una gramática causal para analizar oraciones simples en inglés

% Reglas gramaticales
oracion --> sujeto, verbo, objeto.
sujeto --> pronombre | nombre_propio.
verbo --> verbo_transitivo | verbo_intransitivo.
objeto --> pronombre | nombre_comun.

% Diccionario de palabras
pronombre --> [he].
pronombre --> [she].
nombre_propio --> [john].
nombre_propio --> [mary].
verbo_transitivo --> [likes].
verbo_intransitivo --> [sleeps].
nombre_comun --> [apple].
nombre_comun --> [cat].

% Ejemplos de oraciones
ejemplo1 :- oracion([he, likes, apple], []).
ejemplo2 :- oracion([mary, sleeps], []).

% Consultas de ejemplos
% Consulta: ejemplo1.
% Consulta: ejemplo2.
