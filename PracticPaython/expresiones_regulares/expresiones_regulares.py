import re

texto = """Hola maestro, esta es la cadena 1, como estas mi capitan
Esta es la linea 2 de texto 
Y Esta es la final (linea 3) definitivamente mi capitan """

#Haciendo una busqueda simple
#resultado = re.findall("Esta",texto)

#\d -> busca digitos numericos del 0 - 9
#resultado = re.findall(r"\d",texto)

#\D -< busca TODO MENOS disgitos numéricos del 0 - 9
resultado = re.findall(r"\D",texto)

#\W -< busca TODO MENOS caracteres alfanumericos [a-z A-Z 0-9]
resultado = re.findall(r"\D",texto)


#\s -> busca espacios en blanco -> espacios, tabs, saltos de line
#resultado = re.findall(r"\s",texto)

#\ -> cancelar carateres especiales, cancelando la funcion del punto y buscamos puntos
resultado = re.findall(r"\.",texto)

#$ -> buscamos el final de una linea
resultado = re.findall(f'capitan$',texto,flags=re.M)

#{n} -> busca n cantidad de veces el valor de la izquierda
resultado = re.findall(r'\d{4}',texto)

#{n,m}-> al menos n, como maximop m
resultado = re.findall(r'\d{2,4}',texto)

# | -> busca una cosa o la otra
resultado = re.findall(r'\d{2,3}|Hola',texto)
print(resultado)
