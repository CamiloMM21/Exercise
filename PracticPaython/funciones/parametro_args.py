#forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])
resultado_total = suma_total([3,453,5,345,])

print(f"el resultado es: {resultado_total}")

#lo mismo que arriba pero utilizando el parametro * como parametro (args)

def suma(nombre,*numeros):
    return f"{nombre}, tus numeros es: {sum(numeros)} "
resultado = suma("julian",5,3,5)
# print(resultado)

