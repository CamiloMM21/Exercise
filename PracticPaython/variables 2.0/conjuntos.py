#creando un conjunto con set
conjunto = set(["jnuan 1"])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato 1","dato 2"])
conjunto2 = {conjunto1, "dato 3"}

#Teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,5,7,7}

#verificando si es un conjuto
resultado = conjunto1.issubset(conjunto2)
resultado = conjunto2 <= conjunto1

#verificando si es un superconjunto
resultado = conjunto1.issuperset(conjunto2)
resultado = conjunto2 > conjunto1

#verificando si hay algun resultado en comun
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado)