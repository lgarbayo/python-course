# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=15524

### File Handling ###

#import xml
import csv
import json
#import os

# .txt file

# Leer, escribir y sobrescribir si ya existe
txt_file = open("my_file.txt", "w+") # modo escritura y lectura
# Si el fichero no existe, lo crea. Si existe, lo sobrescribe
"""
    Las opciones más comunes para abrir archivos en Python con open() son:
        "r": Lectura (read). El archivo debe existir.
        "w": Escritura (write). Crea el archivo o lo sobrescribe si existe.
        "a": Añadir (append). Escribe al final del archivo, sin borrar el contenido anterior.
        "r+": Lectura y escritura. El archivo debe existir.
        "w+": Escritura y lectura. Crea o sobrescribe el archivo.
        "a+": Añadir y lectura. Permite leer y añadir al final del archivo.
    También puedes añadir "b" para modo binario (por ejemplo, "rb", "wb").
"""

txt_file.write(
    "Me gusta este curso!\n")
txt_file.write("Estoy aprendiendo mucho de Python\n")

# Posiciona el cursor al inicio del fichero
txt_file.seek(0)

# Lee e imprime todo el contenido del fichero
print(txt_file.read())

# Lee e imprime 10 caracteres desde el inicio del fichero
txt_file.seek(0)
print(txt_file.read(10))

# Lee e imprime el resto de la línea actual desde la posición 11
print(txt_file.readline())

# Lee e imprime la siguiente línea
print(txt_file.readline())

# Lee e imprime las líneas restantes del fichero
for line in txt_file.readlines():
    print(line)

# Escribe una nueva línea en el fichero
txt_file.write("\nAunque también me gusta Spring Java")

# Posiciona el cursor al inicio del fichero, lee e imprime todo su contenido
txt_file.seek(0)
print(txt_file.read())

# Cierra el fichero
txt_file.close()

# Agrega una nueva línea en el fichero
with open("my_file.txt", "a") as my_other_file:
    my_other_file.write("\nY Swift")
# with cierra el fichero automáticamente

# os.remove("intermediate/my_file.txt")


# .json file

json_file = open("intermediate/my_file.json", "w+")

json_test = {
    "name": "Luis",
    "surname": "GF",
    "age": 22
}

json.dump(json_test, json_file, indent=2) # lo guarda con una indentacion 2
"""
    Otros atributos útiles de json.dump():
        sort_keys=True: Ordena las claves alfabéticamente en el archivo.
        separators=(',', ':'): Cambia los separadores entre elementos y claves/valores.
        ensure_ascii=False: Permite escribir caracteres Unicode (acentos, eñes, etc.).
        default: Permite especificar una función para serializar objetos no estándar.
"""

json_file.close()

with open("intermediate/my_file.json") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

json_dict = json.load(open("intermediate/my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])


# .csv file

csv_file = open("intermediate/my_file.csv", "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname", "age", "language", "website"])
csv_writer.writerow(["Luis", "GF", 22, "Python", "https://github.com/lgarbayo"])

csv_file.close()

with open("intermediate/my_file.csv") as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# .xlsx file
# import xlrd # Debe instalarse el módulo

# .xml file

# Se depa propuesto al lector investigar por su cuenta cómo manejar archivos XML en Python.