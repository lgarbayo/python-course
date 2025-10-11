### 01

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

# Construir una URL con separadores personalizados
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

# El siguiente código intenta sumar dos números, pero están guardados como cadenas de texto. Corrígelo para que la suma sea matemática.
# TODO: Modifica la siguiente línea para que el resultado sea 200
numero_str_1 = "150"
numero_str_2 = "50"
resultado_suma = int(numero_str_1) + int(numero_str_2)
print(f"El resultado de la suma es: {resultado_suma}")

# ¿Cuál será el resultado de las siguientes operaciones de redondeo?
# Escribe tu predicción en el comentario.
redondeo_a = round(4.5)
redondeo_b = round(5.5)
print(f"round(4.5) es {redondeo_a}")
print(f"round(5.5) es {redondeo_b}")



### 02

# Tienes 3 productos para comprar en un supermercado. Tu objetivo es imprimir: "huevos, bacon y morcilla"
# Ejemplo: Huevos, Bacon, Morcilla
item1 = "huevos"
item2 = "bacon"
item3 = "morcilla"
print(f"{item1}, {item2} y {item3}")



### 03

# Pide al usuario su nombre y edad, y calcula la edad que tendrá el próximo año.
name = input("What is your name?\n")
current_age_str = input("How old are you?\n")
current_age_int = int(current_age_str)
future_age = current_age_int + 1
print(f"Hello {name}, next year you will be {future_age} years old.")

# Pide al usuario dos números, los suma y muestra el resultado.
# Se usa float() para permitir números con decimales.
num1_str = input("Enter the first number: ")
num2_str = input("Enter the second number: ")
total_sum = float(num1_str) + float(num2_str)
print(f"The sum of {num1_str} and {num2_str} is {total_sum}")

# Pide al usuario su nombre y apellido en una sola línea y le da la bienvenida.
first_name, last_name = input("Enter your first and last name, separated by a space:\n").split()
print(f"Welcome, {first_name} {last_name}.")