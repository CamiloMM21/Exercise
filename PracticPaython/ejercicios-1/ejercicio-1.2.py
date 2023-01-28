frase = input("Decime una frase y te calculo cuanto tardarias si tuvieras que decirla: ")
cantidad_de_palabras = frase.split(" ")
cantidad_de_palabras =len(cantidad_de_palabras)
if cantidad_de_palabras >12:
    print("para flaco tampoco le pedi un testamento")
print(f'Digiste {cantidad_de_palabras} palabras, y tardaria {cantidad_de_palabras/2}segundos en decirlo')
print(f'rancio lo dice {cantidad_de_palabras * 100 // 2*1.3 /100} segundos')
