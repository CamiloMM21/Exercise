animales = ["pez","gato","perro","loro","cocodrilo"]
numeros= [52,16,14,72,27]

#recorrriendo la lista animales
for animal in animales:
    print(f"Ahora la variables animal es a:{animal}")

#recorriendo la lista numeros y multiplicaciopnes cada valor por 10
for numero in numeros:
    resultado = numero *10
    print(resultado)

#iterando dos listas del mismo tamaño al mismo tiempo
for numero,animal in zip(numeros,animales):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")

#forma no optima de recorrer una lista
for num in range(len(numeros)):
    print(numeros[num])


# forma optima pra recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'indice es: {indice} y el valor es: {valor}')