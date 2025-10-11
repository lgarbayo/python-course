# --- Ejercicio 1: Mi Libro Favorito ---
#
# 1. Crea un diccionario llamado `favorite_book` que represente un libro.
#    Debe tener las siguientes claves: "title", "author", "year_published", "genre".
# 2. Imprime el título y el autor del libro en una frase como:
#    "Mi libro favorito es [título], escrito por [autor]."
# 3. Añade una nueva clave-valor al diccionario: "pages" con un número de páginas.
# 4. Modifica el año de publicación a un nuevo valor.
# 5. Imprime el diccionario completo.
#
# --- Ejercicio 2: Contador de Frecuencia de Palabras ---
#
# Crea una función llamada `count_word_frequency(text)` que reciba una cadena de texto.
# La función debe devolver un diccionario donde las claves son las palabras del texto
# y los valores son la cantidad de veces que cada palabra aparece.
#
# Pista: Convierte el texto a minúsculas y usa `.split()` para obtener una lista de palabras.
# Luego, itera sobre la lista y usa un diccionario para contar.
text_to_analyze = "Python es un lenguaje de programación. Python es popular."
#
# --- Ejercicio 3 (Avanzado): Encontrar Números Complementarios ---
#
# Crea una función `find_complementary_pairs(numbers, target)`.
# La función debe encontrar TODOS los pares de números en la lista `numbers` que sumen `target`.
# Debe devolver una lista de tuplas, donde cada tupla contiene un par de números.
#
# Ejemplo: `find_complementary_pairs([2, 7, 4, 1, 5], 6)` debería devolver `[(2, 4), (1, 5)]`.
numbers_list = [2, 7, 4, 1, 5, 3, 6]
target_sum = 8