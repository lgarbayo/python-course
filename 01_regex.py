# Importar el módulo de expresiones regulares "re"
import re
# Crear un patrón, que es una cadena de texto que describe lo que queremos encontrar
pattern = "Hola"
# El texto donde queremos buscar
text = "Hola mundo"
# Usar la función de búsqueda de "re"
result = re.search(pattern, text)

if result:
  print("He encontrado el patrón en el texto")
else:
  print("No he encontrado el patrón en el texto")
# atajo de teclado: run selection line in pyhton repl -> MAYUS + ENTER

# .group() devuelve la cadena que coincide con el pattern
print(result.group())

# .start() devolver la posición inicial de la coincidencia
print(result.start())

# .end() devolver la posición final de la coincidencia
print(result.end())

# .findall() devuelve una lista con todas las coincidencias
text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Python"
matches = re.findall(pattern, text)
print(len(matches)) # con len sabemos las veces que aparece

# iter() devuelve un iterador que contiene todos los resultados de la búsqueda
text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Python"
matches = re.finditer(pattern, text)
for match in matches:
  print(match.group(), match.start(), match.end())

# Los modificadores son opciones que se pueden agregar a un patrón para cambiar su comportamiento
# re.IGNORECASE: Ignora las mayúsculas y minúsculas
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero la ia no es tan mala. ¡Viva la Ia!"
pattern = "IA"
found = re.findall(pattern, text, re.IGNORECASE)
if found: print(found)

# .sub() reemplaza todas las coincidencias de un patrón en un texto
text = "Hola, mundo! Hola de nuevo. Hola otra vez."
pattern = "hola"
replacement = "Adiós"
new_text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
print(new_text)

# Los cuantificadores se utilizan para especificar cuántas ocurrencias de un carácter o grupo de caracteres se deben encontrar en una cadena.
# *: Puede aparecer 0 o más veces
text = "aaaba"
pattern = "a*"
matches = re.findall(pattern, text)
print(matches)

# +: Una a más veces
text = "dddd aaa ccc a bb aa casa"
pattern = "a+"
matches = re.findall(pattern, text)
print(matches)

# ?: Cero o una vez
text = "aaabacb"
pattern = "a?b"
matches = re.findall(pattern, text)
print(matches)

# {n}: Exactamente n veces
text = "aaaaaa         aa   aaaa"
pattern = "a{3}"
matches = re.findall(pattern, text)
print(matches)

# {n, m}: De n a m veces
text = "u uu uuu u"
pattern = r"\w{2,3}"
matches = re.findall(pattern, text)
print(matches)

# [:] Coincide con cualquier caracter dentro de los corchetes
username = "lu.cho+55"
pattern = r"^[\w._%+-]+$"

match = re.search(pattern, username)
if match:
  print("El nombre de usuario es válido: ", match.group())
else:
  print("El nombre de usuario no es válido")


# Buscar todas las vocales de una palabra
text = "Hola mundo"
pattern = r"[aeiou]"
matches = re.findall(pattern, text)
print(matches)

# Una Regex para encontrar las palabras man, fan y ban
# pero ignora el resto
text = "man ran fan ñan ban"
pattern = r"[mfb]an"

matches = re.findall(pattern, text)
print(matches)

# Ejercicio:
# Nos han complicado el asunto, porque ahora hay palabras que encajan pero no empiezan por esas letras.
# Solo queremos las palabras man, fan y ban
text = "omniman fanatico man bandana"
# \b 

text = "22"
pattern = r"[4-9]"

matches = re.findall(pattern, text)
print(matches)


# Ejercicio final con todo lo aprendido
# Mejorar esto: https://www.computerhope.com/jargon/r/regular-expression.png

## Buscar corner cases que no pasa y arreglarlo:
"lo.que+sea@shopping.online"
"michael@gov.co.uk"

# [^]: Coincide con cualquier caracter que no esté dentro de los corchetes
text = "Hola mundo"
pattern = r"[^aeiou]"
matches = re.findall(pattern, text)
print(matches)