# --- Solución Ejercicio 1: Mi Libro Favorito ---
print("--- Ejercicio 1 ---")
favorite_book = {
    "title": "Cien Años de Soledad",
    "author": "Gabriel García Márquez",
    "year_published": 1967,
    "genre": "Realismo mágico"
}

print(f"Mi libro favorito es {favorite_book['title']}, escrito por {favorite_book['author']}.")

favorite_book["pages"] = 432
favorite_book["year_published"] = 1982 # Edición de premio Nobel

print("Diccionario actualizado:", favorite_book)


# --- Solución Ejercicio 2: Contador de Frecuencia de Palabras ---
print("\n--- Ejercicio 2 ---")
def count_word_frequency(text: str) -> dict:
    """Cuenta la frecuencia de cada palabra en un texto."""
    words = text.lower().replace('.', '').split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

text_to_analyze = "Python es un lenguaje de programación. Python es popular."
word_counts = count_word_frequency(text_to_analyze)
print("Frecuencia de palabras:", word_counts)

# --- Solución Ejercicio 3 (Avanzado): Encontrar Números Complementarios ---
print("\n--- Ejercicio 3 ---")
def find_complementary_pairs(numbers: list, target: int) -> list:
    """Encuentra todos los pares de números que suman el objetivo."""
    seen_numbers = set()
    pairs = []
    for num in numbers:
        complement = target - num
        if complement in seen_numbers:
            pairs.append((complement, num))
        seen_numbers.add(num)
    return pairs

numbers_list = [2, 7, 4, 1, 5, 3, 6]
target_sum = 8
found_pairs = find_complementary_pairs(numbers_list, target_sum)
print(f"Pares que suman {target_sum}: {found_pairs}")