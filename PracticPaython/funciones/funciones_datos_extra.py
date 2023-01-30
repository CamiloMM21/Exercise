#creando una funcion de 3 parametros

def frase(nombre,apellido,adjetivo):
    return f"Hola {nombre} {apellido} eres un {adjetivo}"
#utilizando keyword argumento  
frase_result = frase(nombre="juan",apellido="muñoz",adjetivo="titan")

print(frase_result)