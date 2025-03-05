with open("datos.txt", "w") as archivo:
    archivo.write("Hola, esto es un archivo de texto.\n")
    archivo.write("Segunda línea.\n")

with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
