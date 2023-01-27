#creando una lista (se puede modificar)
lista=["juan camilo", "soy camilo", True,1.89]
#creando una tubla (no puede modificar)
tupla= ("juan ", "soy camilo", True,1.89)

#esto es valido
lista[3]="maquinola"
#esto no
#tupla[3]="maquinola"

#creando un conjusto (set)

#un conjunto no me permite tener datos duplicados
conjunto= {"juan ", "soy camilo", True,1.89}



#creando un diccionario (dict)(la estrutura es key: value y separados comas)
diccionario= {
    'nombre': "juan camilo",
    'esta_emocionado': True,
    'altura': 1.89
}
print(diccionario['altura'])
print(lista[3])