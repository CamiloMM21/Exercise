#2 listas, una con nombres otra con apellidos

nombres = ["lucas","roberto","julian","mateo","simon"]
apellidos = ["mosquera","rivera","robertix","tarado","Zing"]

#REgistrar esta informacion en un TXT de forma óptima

with open("archivos_problemas\\nombres_i_apellidos.text","w")as arch:
    arch.writelines("los datos sin:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n-------\n") for n,a in zip(nombres,apellidos)]