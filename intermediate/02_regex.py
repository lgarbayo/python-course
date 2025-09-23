import re

# El punto (.)
# Coincidir con (1) cualquier caracter excepto una nueva linea

text = "Hola mundo, H0la de nuevo, H$la otra vez"
pattern = r"H.la" # Hola, H0la, H$la # determinamos que lo siguiente es una expresion regular

found = re.findall(pattern, text)

if (found):
  print(found)
else:
  print("No se ha encontrado el patrón")


# Cómo usar la barra invertida para anular el significado de metacaracter
text = "Mi casa es blanca. Y el coche es negro."
pattern = r"\."

matches = re.findall(pattern, text)

print(matches)

# \d: coincide con cualquier dígito (0-9)
# \w: Coincide con cualquier caracter alfanumerico (a-z, A-Z, 0-9, _)
# \s: Coincide con cualqueir espacio en blanco (espacio, tabulación, salto de línea)
# ^: Coincide con el principio de una cadena
# $: Coincide con el final de una cadena
# \b: Coincide con el principio o final de una palabra
# |: Coincidr con una opción u otra