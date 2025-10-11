# --- Solución Ejercicio 1: Calificador de Notas ---
print("--- Ejercicio 1: Calificador de Notas ---")
try:
    note = float(input("Introduce tu nota (0-10): "))
    if note >= 9 and note <= 10:
        print("Sobresaliente")
    elif note >= 7:
        print("Notable")
    elif note >= 5:
        print("Aprobado")
    elif note >= 0:
        print("Suspenso")
    else:
        print("Nota fuera de rango.")
except ValueError:
    print("Entrada inválida. Debes introducir un número.")


# --- Solución Ejercicio 2: Precio de Entrada al Cine ---
print("\n--- Ejercicio 2: Precio de Entrada al Cine ---")
try:
    age = int(input("Introduce tu edad: "))
    if age < 0:
        print("La edad no puede ser negativa.")
    elif age < 12:
        price = 5
        print(f"El precio de tu entrada es de {price}€.")
    elif age <= 17:
        price = 7
        print(f"El precio de tu entrada es de {price}€.")
    elif age > 65:
        price = 4
        print(f"El precio de tu entrada es de {price}€.")
    else:
        price = 10
        print(f"El precio de tu entrada es de {price}€.")
except ValueError:
    print("Edad inválida. Debes introducir un número entero.")


# --- Solución Ejercicio 3: Adivina el Número (Bucle `while`) ---
print("\n--- Ejercicio 3: Adivina el Número ---")
secret_number = 42
guess = -1

while guess != secret_number:
    try:
        guess = int(input("Adivina el número secreto: "))
        if guess == secret_number:
            print("¡Felicidades, has adivinado!")
        else:
            print("Incorrecto. ¡Inténtalo de nuevo!")
    except ValueError:
        print("Eso no es un número. Intenta de nuevo.")


# --- Solución Ejercicio 4: Contador de Vocales (Bucle `for`) ---
print("\n--- Ejercicio 4: Contador de Vocales ---")
phrase = input("Introduce una frase: ")
vowel_count = 0
vowels = "aeiou"

for char in phrase.lower(): # Convertimos a minúsculas para contar todas las vocales
    if char in vowels:
        vowel_count += 1

print(f"La frase tiene {vowel_count} vocales.")


# --- Solución Ejercicio 5: Números Pares al Cuadrado (List Comprehension) ---
print("\n--- Ejercicio 5: Números Pares al Cuadrado ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_evens = [num**2 for num in numbers if num % 2 == 0]
print(f"Lista original: {numbers}")
print(f"Cuadrado de los pares: {squared_evens}")


# --- Solución Ejercicio 6: FizzBuzz ---
print("\n--- Ejercicio 6: FizzBuzz ---")
for num in range(1, 101):
    # La condición más específica (múltiplo de ambos) debe ir primero.
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


# --- Solución Ejercicio 7: Clasificador de Números (Ternario) ---
print("\n--- Ejercicio 7: Clasificador de Números ---")
try:
    number_input = int(input("Introduce un número: "))
    message = "Es par" if number_input % 2 == 0 else "Es impar"
    print(message)
except ValueError:
    print("Entrada inválida. Debes introducir un número entero.")
