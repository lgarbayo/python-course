# Mostrar informacion en consola
# Como en cada lenguaje siemptre se empieza por el mitico:
print("Hola Mundo") 
print("Hello World")
print('hola amigos')

print("py", "th", "on")
print("py", "th", "on", end= " ") # por defecto el end es un salto de linea \n
print("py", "th", "on", sep="")
# ejecuta el código en la terminal y debería ver algo así:
# py th on
# py th on python

## Ejercicios propuesto:
#
# Mostrar en consola la frase: "Estoy aprendiendo Python gracias al curso del mejor profesor: Luis!!"
#
# Tienes 3 productos para comprar en un supermercado. Tu objetivo es imprimirlos en una sola línea separados por una coma y un espacio
# Ejemplo: Huevos, Bacon, Morcilla
#
# Tienes 3 productos para comprar en un supermercado. Tu objetivo es imprimir: "huevos, bacon y morcilla"
# Ejemplo: Huevos, Bacon, Morcilla
#
# Ejercicio final: Construir una URL con separadores personalizados
# Imagina que tienes las partes de una URL en una lista. Tu tarea es imprimir la URL completa y funcional en una sola línea utilizando la 
# función print() y sus parámetros `sep` y `end`.
url_parts = ["https", "www.python.org", "downloads"]


## Tipos de datos
print(5)
# types: int, float, complex, str, bool, NoneType, list, tuple, dict, range, set...
print(type(-5))
print(type(3.14))
print(type(1.0))
print(type(1e3))
print(type(1 + 2j))
print(type("str:"))
print(type("""
      """)) # str: cadena multilínea o cadena de texto, pueden ser comillas simples, dobles o triples
# la cadena multilinea se suele usar para documentacion
print(type(True))
print(type(False))
print(type(1 < 2))
print(type(None)) # tipo nulo

## Ejercicio propuesto:
#
# Ahora, piensa en el tipo de dato que resultará de las siguientes operaciones.
# Escribe tu predicción en un comentario y luego verifica con type().
operacion_a = 5 + 5.0
operacion_b = "5" + "5"
operacion_c = len("Python") == 6


# Casting de tipos
print("Conversion de tipos")
print(type(100)) # tipado fuerte, no realiza conversiones de tipos automaticas
#print("100" + 2) :error porque el primero es str, entonces + actua como concat cadenas
    # al reves el + seria de suma
print(2 + int("100"))
print("100" + str(2))
print(float(3.16))
print(int(3.1416)) # convierte en entero pierdes decimales
print(bool(3))
print(bool(0)) # unico q se convierte a false
print(bool(1))
print(bool("")) # unico str q se convierte a false porq es cadena vacia, con un espacio ya tiene algo
print(bool(" "))
print(bool("False"))

print(round(3.5))
print(round(2.5))
#round justo en .5 en python redondea al PAR más cercano

## Ejercicios propuesto:
#
# El siguiente código intenta sumar dos números, pero están guardados como cadenas de texto. Corrígelo para que la suma sea matemática.
numero_str_1 = "150"
numero_str_2 = "50"
# TODO: Modifica la siguiente línea para que el resultado sea 200
resultado_suma = numero_str_1 + numero_str_2
print(f"El resultado de la suma es: {resultado_suma}")
#
# ¿Cuál será el resultado de las siguientes operaciones de redondeo?
# Escribe tu predicción en el comentario.
redondeo_a = round(4.5)
redondeo_b = round(5.5)