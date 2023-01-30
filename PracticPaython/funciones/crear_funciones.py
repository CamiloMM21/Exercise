#creando una funcion simple
# def saludar():
#     print("Hola juan, mi maestro ¿Como andas?")

#     saludar()
#     saludar()
#     saludar()

#crear un a funcion que tenga parametros
def saludar(nombre,sexo):
    sexo = sexo.lower()#es un parametro que me convierte el string en minuscula
    if(sexo == "mujer"):
        adjetivo = "reina"
    elif(sexo == "hombre"):
        adjetivo = "titan"
    else:
        adjetivo = "cariño"

    print(f"Hola {nombre}, mi {adjetivo} ¿Como andas?")

saludar("Camila","Mujer")

#crear una funcion que me retorne multiples valores
def crear_contraseña_random(num):
    chars = "abcde"
    num_entero =str(num)
    num = int(num_entero[0])
    c1 =num -2
    c2 =num
    c3 =num -5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num

#desempaquetando la funcion
passsword,primer_numero = crear_contraseña_random(254)

#mostrando los resultados obtenidos y los datos utilizados para obtenerlo
frase =f"tu contraseña es: {passsword}"
frase1 =f"tu contraseña es: {primer_numero}"
print(frase)
print(frase1)