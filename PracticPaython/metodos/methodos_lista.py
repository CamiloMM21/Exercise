#Creando una lista con list()
lista= list([53,326,True,])

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista
lista.append(78)

#agregando un elemento a la lista en un indice especifico
lista.insert(3,5)

#agregando varios elementos a la lista
lista.extend([False,2030])

#eliminando un elemento  de la lista(por su indice)
lista.pop(0)# -1 para eliminar el ultimo, -2 para eleminar elanteultimo, y asi sucesivamente

#removiendo un elemento de la lista por su valor
lista.remove(5)

#eliminando todos los elementos de la lista
# lista.clear()

#ordenando la lista de forma acendente(si usamos el parametro reverse=True lo ordena en reversa)
lista.sort()

#invirtiendo los elementos de una lista
lista.reverse()

#verificar si un elemento se encuentra en la lista
elemento_encontrado = lista.index(326)

print(dir(set(["hpasd","dasd",254])))


#los conjuntos se hace con set()