cadena1 =  "soy,camilo"
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
busqueda_find = cadena1.find("soy")

#buscamos una cadena en otra cadena, si no hay coincidencia lanza una excepción
busqueda_index = cadena1.index("a")

#si es un numerico, devolvemos true sino devolvemos false
es_numerico = cadena1.isnumeric()

#si es alfanumerico devolvemos true, sino devolvemos false 
es_alfamunmerico = cadena1.isalpha()

#contamos las coincidencias de una cadena, dentro de otra cadena, devuelve la cantidad de coincidencia
contar_coincidencias = cadena1.count("soy ")

#contamos cuantos carateres tiene una cadena
contar_caracteres =len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith("h")

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena1.endswith("h")

#remplaza un pedazo de la cadena original dada, por otra dada 
cadena_nueva = cadena1.replace("soy", "mi")

#separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")

print(cadena_separada[1])
