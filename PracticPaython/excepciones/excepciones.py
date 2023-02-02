#creando funcion que suma numeros
def sumar_dos():
    #iniciando un bucle
    while True:
        #pidiendo numeros
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        #intentando convertirlos a entero y sumarlos
        try:
            resultado = int(a) + int(b)
            #si lanza una exepción, pedirle que reingrese los datos
        except:
            print("Te pedi un numero salame")
            #si todo salio bien terminamos el bucle
        else:
            break
        finally:
            print("Esto se ejecuta siempre finalizado")
        return resultado

print(sumar_dos())
