#creando diccionarios con dict()
diccionario = dict(nombre="camilo",apellido="muñoz")

#las listas no pueden ser claves y usamos fozenset para meter conjuntos
diccionario = {frozenset(["juan","muñoz"]):"JAJAJA"}

#creando diccionario con fromkeys()
diccionario = dict.fromkeys(["nombre","apellido"])
print(diccionario)