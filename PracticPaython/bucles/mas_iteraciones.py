
frutas= ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena="holaCamilo"
numeros=[1,3,5,6,7]

#evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == "manzana":
        continue
    print(f"me voy a comer una {fruta}")

#evitar que el bucle sega ejecutandose (el else no se ejecuta tampoco)
for fruta in frutas:
    print(f"mira chico la: te cayó mal") 
    if fruta =="naranja":
        break
else:
    print("bucle terminado")

#recorrer una cadena de texto
for letra in cadena:
    print(letra)

#for en una sola linea de codigo (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]

print(numeros_duplicados)