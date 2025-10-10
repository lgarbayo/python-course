# Mostrar en consola la frase: "Estoy aprendiendo Python gracias al curso del mejor profesor: Luis!!"
print("Estoy aprendiendo Python gracias al curso del mejor profesor: Luis!!")

# Tienes 3 productos para comprar en un supermercado. Tu objetivo es imprimirlos en una sola línea separados por una coma y un espacio
# Ejemplo: Huevos, Bacon, Morcilla
item1 = "huevos"
item2 = "bacon"
item3 = "morcilla"
print(item1, item2, item3, sep=", ")

# Tienes 3 productos para comprar en un supermercado. Tu objetivo es imprimir: "huevos, bacon y morcilla"
# Ejemplo: Huevos, Bacon, Morcilla
print(item1, item2, sep=", ", end=" y ")
print(item3)
print(f"{item1}, {item2} y {item3}")

# Ejercicio final: Construir una URL con separadores personalizados
# Imagina que tienes las partes de una URL en una lista. Tu tarea es imprimir la URL completa y funcional en una sola línea utilizando la 
# función print() y sus parámetros `sep` y `end`.
url_parts = ["https", "www.python.org", "downloads"]
print(url_parts[0], end="://")
print(url_parts[1], url_parts[2], sep="/", end="/\n")

# Ahora, piensa en el tipo de dato que resultará de las siguientes operaciones.
# Escribe tu predicción en un comentario y luego verifica con type().
operacion_a = 5 + 5.0
print(f"El resultado de operacion_a es de tipo: {type(operacion_a)}")
operacion_b = "5" + "5"
print(f"El resultado de operacion_b es de tipo: {type(operacion_b)}")
operacion_c = len("Python") == 6
print(f"El resultado de operacion_c es de tipo: {type(operacion_c)}")