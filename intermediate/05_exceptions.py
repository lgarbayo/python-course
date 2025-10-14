# Manejo y captura de excepciones en Python

"""
En Python, las excepciones son eventos que interrumpen el flujo normal de ejecución de un programa cuando ocurre un error. 
Capturar excepciones permite manejar errores de forma controlada y evitar que el programa termine abruptamente.
Existen tres tipos principales:

1. Checked Exceptions (comprobadas):
   - Deben ser gestionadas explícitamente con try-catch o declaradas con throws en la firma del método.
   - Ejemplo: IOException, SQLException.
   - El compilador obliga a tratarlas.
   
   // Ejemplo en Java:
   try {
       FileReader fr = new FileReader("archivo.txt");
   } catch (IOException e) {
       System.out.println("Error de entrada/salida");
   }

2. Unchecked Exceptions (no comprobadas):
   - Heredan de RuntimeException.
   - No requieren manejo explícito, el compilador no obliga a tratarlas.
   - Ejemplo: NullPointerException, IndexOutOfBoundsException.
   
   // Ejemplo en Java:
   String s = null;
   System.out.println(s.length()); // NullPointerException

3. Errors:
   - Situaciones graves que normalmente no se capturan.
   - Ejemplo: OutOfMemoryError, StackOverflowError.
   - Indican problemas del entorno de ejecución.
   
   // Ejemplo en Java:
   // while(true) { makeRecursiveCall(); } // StackOverflowError

Resumen:
- Checked: el compilador obliga a gestionarlas.
- Unchecked: no es obligatorio gestionarlas.
- Errors: problemas graves, no suelen capturarse.
"""

# --- Sintaxis básica de try-except ---
try:
    # Codigo que puede lanzar una excepción
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero.")

# --- Bloques else y finally ---
try:
    print("Intentando abrir archivo...")
    f = open("archivo.txt")
except FileNotFoundError:
    print("Archivo no encontrado.")
else: # se ejecuta solo si no ocurre ninguna excepcion en try
    # util para codigo que depende de que todo haya ido bien
    print("Archivo abierto correctamente.")
    f.close()
finally: # siempre se ejecuta, haya o no excepcion (liberar recursos, cerrar archivos, conexiones, etc)
    print("Bloque finally: se ejecuta siempre.")

# --- Captura de múltiples excepciones ---
try:
    x = int("abc") # Esto lanza ValueError porque "abc" no es convertible a entero
except (ValueError, TypeError) as e: # se incluyen ambos porque ambos pueden ocurrir en operaciones similares de conversión
    # o manipulación de tipos de datos
    print("Error de tipo o valor:", e)
    # e contiene la instancia de la excepción capturada

# --- Captura genérica de cualquier excepción ---
try:
    y = 1 / 0
except Exception as e: # captura cualquier excepción que herede de Exception
    print("Ocurrió una excepción genérica:", type(e).__name__, e)
    # type(e).__name__ obtiene el nombre de la clase de la excepcion capturada

# --- Lanzar(raise) excepciones manualmente ---
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero.")
    return a / b

# --- Tipos comunes de errores en Python ---

# SyntaxError: ocurre cuando el código no sigue las reglas de sintaxis de Python
# print "¡Hola comunidad!" # Descomentar para Error
from math import pi
import math
print("¡Hola comunidad!")

# NameError: ocurre cuando se intenta acceder a una variable no definida
language = "Spanish"  # Comentar para Error
print(language)

# IndexError: ocurre cuando se intenta acceder a un índice fuera del rango de una lista
my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
# print(my_list[5]) # Descomentar para Error

# ModuleNotFoundError: ocurre cuando se intenta importar un módulo que no existe
# import maths # Descomentar para Error

# AttributeError: ocurre cuando se intenta acceder a un atributo que no existe
# print(math.PI) # Descomentar para Error
print(math.pi)

# KeyError: ocurre cuando se intenta acceder a una clave que no existe en un diccionario
my_dict = {"Nombre": "Luis", "Apellido": "Garbayo", "Edad": 22, 1: "Python"}
print(my_dict["Edad"])
# print(my_dict["Apelido"]) # Descomentar para Error
print(my_dict["Apellido"])

# TypeError: ocurre cuando se intenta realizar una operación incompatible con el tipo de dato
# print("Hola" + 5) # Descomentar para Error
# print(my_list["0"]) # Descomentar para Error
print(my_list[0])
print(my_list[False])

# ImportError: ocurre cuando no se puede importar un módulo o un atributo específico de un módulo
# from math import PI # Descomentar para Error
print(pi)

# ValueError: ocurre cuando se intenta convertir un valor a un tipo incompatible
# my_int = int("10 Años") # Descomentar para Error
my_int = int("10")
print(type(my_int))

# ZeroDivisionError: ocurre cuando se intenta dividir por cero
# print(4/0) # Descomentar para Error
print(4/2)

# --- Ejemplo de uso de varios tipos de excepciones ---
try:
    lista = [1, 2, 3]
    print(lista[5])  # IndexError
    d = {'a': 1}
    print(d['b'])    # KeyError
    x = int('abc')   # ValueError
except IndexError:
    print('Error: índice fuera de rango.')
except KeyError:
    print('Error: clave no encontrada.')
except ValueError:
    print('Error: valor incorrecto.')

# --- Buenas prácticas ---
# - Captura solo las excepciones que esperas y puedes manejar.
# - Evita usar except sin especificar el tipo de excepción.
# - Usa finally para liberar recursos (archivos, conexiones, etc).
# - Documenta los posibles errores que puede lanzar tu función.


### --- Ejercicios propuestos ---
# 1. Escribe una función que reciba una lista y devuelva el elemento en una posición dada, manejando el caso de índice fuera de rango.
# 2. Escribe una función que abra un archivo y lea su contenido, manejando el caso de archivo no encontrado.
# 3. Escribe una función que convierta una cadena a entero, manejando el caso de valor incorrecto.
