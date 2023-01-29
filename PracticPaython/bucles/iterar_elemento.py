animales = {"pez","gato","perro","loro","cocodrilo"}
numeros= {52,16,14,72,27}

#recorrriendo la conjunto animales
for animal in animales:
    print(f"Ahora la variables animal es a:{animal}")

#recorriendo la conjunto numeros y multiplicaciopnes cada valor por 10
for numero in numeros:
    resultado = numero *10
    print(resultado)

#iterando dos conjuntos del mismo tamaño al mismo tiempo
for numero,animal in zip(numeros,animales):
    print(f"recorriendo conjunto 1: {numero}")
    print(f"recorriendo conjunto 2: {animal}")




# forma optima pra recorrer una conjunto con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'indice es: {indice} y el valor es: {valor}')

#usando el for/else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")

#todo lo anterior funciona exactamente igual para tuplas y conjuntos


#forma no optima de recorrer una lista con su indice(no funciona en conjuntos)
for num in range(len(numeros)):
    print(numeros[num])