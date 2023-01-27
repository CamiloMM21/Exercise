cadena1 =  "holasoycamilo"
cadena2 = "Bienvenido guitarrista"

#dir me permite ver todos los metodos que puede utilizar en cada tipo de dato
#los metodos funciona de la siguiente manera  DATO.METHODO esto es si se requiere utilizar parametros()

#convierte a mayusculas
resultado = cadena1.upper()

#convierte a minusculas
resultado = cadena1.lower()

#primera letra en mayuscula
primera_letra_mayuscula = resultado = cadena1.capitalize()

#buscamos una cadena en otra cadena
busqueda_find = cadena1.find("a")

#buscamos una cadena en otra cadena, si no hay coincidencia lanza una excepción
busqueda_index = cadena1.index("a")

#si es un numerico, devolvemos true sino devolvemos false
es_numerico = cadena1.isnumeric()

#si es alfanumerico devolvemos true, sino devolvemos false 
es_alfamunmerico = cadena1.isalpha("2")

#contamos las coincidencias de una cadena, dentro de otra cadena, devuelve la cantidad de coincidencia
contar_coincidencias = cadena1.count("hola")


print(es_alfamunmerico)
