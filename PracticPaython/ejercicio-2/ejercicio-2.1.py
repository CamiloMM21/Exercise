#falsto el profe y los pibes van a armar la clase
#pedir el nombre y la edad de los compañeros que vieron hoy a clase

def obtener_compañero(cantidad_de_compañeros):
    compañeros = []
    for i in range(cantidad_de_compañeros):
        nombre = input("ingrese el nombre del compañero: ")
        edad = int(input("ingrese la edad del compañero: "))
        compañero = (nombre,edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros [-1][0]
    return asistente,profesor

asistente,profesor = obtener_compañero(4)
print(f"el nombre del profesor es: {profesor} y del asistente es: {asistente}")

