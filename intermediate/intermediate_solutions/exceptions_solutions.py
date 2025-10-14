# 1. Escribe una función que reciba una lista y devuelva el elemento en una posición dada, manejando el caso de índice fuera de rango.
def obtener_elemento(lista, posicion):
    try:
        return lista[posicion]
    except IndexError:
        return "Índice fuera de rango"

# 2. Escribe una función que abra un archivo y lea su contenido, manejando el caso de archivo no encontrado.
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "Archivo no encontrado"

# 3. Escribe una función que convierta una cadena a entero, manejando el caso de valor incorrecto.
def convertir_a_entero(cadena):
    try:
        return int(cadena)
    except ValueError:
        return "Valor incorrecto para conversión a entero"
