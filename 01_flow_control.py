edad = 18
if edad >= 18:
  print("Eres mayor de edad")
  print("¡Felicidades!")

edad = 15
if edad >= 18:
  print("Eres mayor de edad")
  print("¡Felicidades!")

edad = 15
if edad >= 18:
  print("Eres mayor de edad")
else:
  print("Eres menor de edad")

nota = 5
if nota >= 9:
  print("¡Sobresaliente!")
elif nota >= 7:
  print("Notable!")
elif nota >= 5:
  print("¡Aprobado!")
else:
  print("¡No está calificado!")

# Los operadores lógicos en Python son:
# and: True si ambos operandos son verdaderos
# or: True si al menos uno de los operandos es verdadero
edad = 16
tiene_carnet = True
if edad >= 18 and tiene_carnet:
  print("Puedes conducir 🚗")
else:
  print("POLICIA 🚔!!!1!!!")

# También tenemos el operador lógico "not"
# que nos permite negar una condición
es_fin_de_semana = False
if not es_fin_de_semana:
  print("¡midu, venga que hay que streamear!")

# Podemos anidar condicionales, uno dentro del otro
# para determinar múltiples condiciones aunque
# siempre intentaremos evitar esto para simplificar
print("\n Anidar condicionales")
edad = 20
tiene_dinero = True
if edad >= 18:
  if tiene_dinero:
    print("Puedes ir a la discoteca")
  else:
    print("Quédate en casa")
else:
  print("No puedes entrar a la disco")
# Más fácil sería:
# if edad < 18:
#   print("No puedes entrar a la disco")
# elif tiene_dinero:
#   print("Puedes ir a la discoteca")
# else:
#   print("Quédate en casa")

# Ten en cuenta que hay valores que al usarlos como condiciones
# en Python son evaluados como verdaderos o falsos
# por ejemplo, el número 5, es True
numero = 5
if numero: # True
  print("El número no es cero")

# Pero el número 0 se evalúa como False
numero = 0
if numero: # False
  print("Aquí no entrará nunca")

# También el valor vacío "" se evalúa como False
nombre = ""
if nombre:
  print("El nombre no es vacío")

# ¡Ten cuidado con no confundir la asignación = con la comparación ==!
numero = 3 # asignación
es_el_tres = numero == 3 # asignacion de una comparación

if es_el_tres:
  print("El número es 3")

# A veces podemos crear condicionales en una sola línea usando
# las ternarias, es una forma concisa de un if-else en una línea de código
print("\nLa condición ternaria:")
# [código si cumple la condición] if [condicion] else [codigo si no cumple]

edad = 17
mensaje = "Es mayor de edad" if edad >= 18 else "Es menor de edad"
print(mensaje)

edad = 19
print("Es mayor de edad") if edad >= 18 else "Es menor de edad"

##############
##############
##############


# Creación de listas
lista1 = [1, 2, 3, 4, 5] # lista de enteros
lista2 = ["manzanas", "peras", "plátanos"] # lista de cadenas
lista3 = [1, "hola", 3.14, True] # lista de tipos mixtos
lista_vacia = []
lista_de_listas = [[1, 2], ['calcetin', 4]]
matrix = [[1, 2], [2, 3], [4, 5]]
print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

# Acceso a elementos por índice
print(lista2[0])  # manzanas
print(lista2[1])  # peras
print(lista2[-1]) # plátanos (desde el final -1)
print(lista2[-2]) # peras (desde el final -2)
print(lista_de_listas[1][0])

# Slicing (rebanado) de listas
lista1 = [1, 2, 3, 4, 5]
print(lista1[1:4]) # [2, 3, 4]
print(lista1[:3]) # [1, 2, 3]
print(lista1[3:]) # [4, 5]
print(lista1[:]) # [1, 2, 3, 4, 5]

# El tercer parámetro es el PASO (step)
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista1[::2]) # para devolver índices pares
print(lista1[::-1]) # para devolver índices inversos

# Modificar una lista
lista1[0] = 20
print(lista1)

# Añadir elementos a una lista
lista1 = [1, 2, 3]

# forma larga y menos eficiente
lista1 = lista1 + [4, 5, 6]
print(lista1)

# forma corta y más eficiente
lista1 += [7, 8, 9]
print(lista1)

# Recuperar longitud de una lista
print("Longitud de la lista", len(lista1))