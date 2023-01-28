diccionario = {
     "nombre":'camilo',
     "muñoz": 'muñoz',
     "gano":100000000
}
#nos devuelve un objeto dict:item
claves = diccionario.keys()

#obteniendo un elemento con get()(si no me encuentra nada el programa continua)
valor_de_sedf = diccionario.get("sedf")

#eliminando todos los diccionario
# diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop("nombre")

#obteniendo un elemento dict_items iterable
diccionario_iterable = diccionario.items()

print(diccionario_iterable)