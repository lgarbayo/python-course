## Bucles WHILE

# Bucle con una simple condición
contador = 0
while contador <= 5:
  print(contador)
  contador += 1 # importante para evitar un bucle infinito para una condición de salida

# utilizando la palabra break, para romper el bucle
contador = 0
while True:
  print(contador)
  contador += 1

  if contador == 5:
    break # sale del bucle

# continue lo hace es saltar esa iteración en concreto
contador = 0
while contador < 10:
  contador += 1

  if contador % 2 == 0:
    continue # solo mostrara los numeros impares, salta la iteracion de los pares

  print(contador)

# else, esta condición se ejecuta cuando termina el bucle
contador = 0
while contador < 5:
  print(contador)
  contador += 1
  # en el unico caso en el que no se ejecuta el else seria si en el while hay break, dado que no encontrara nunca la condicion
else:
  print("El bucle ha terminado")

contador = 0
while contador < 5:
  print(contador)
  contador += 1
  break
else:
  print("El bucle ha terminado")

# pedirle al usuario un número positivo
numero = -1
while numero < 0:
  numero = int(input("Escribe un número positivo: ")) # int para castear
  if numero < 0:
    print("El número debe ser positivo. Intenta otra vez")

print(f"El número que has introducido es {numero}")

numero = -1
while numero < 0:
  try:
    numero = int(input("Escribe un número positivo: "))
    if numero < 0:
      print("El número debe ser positivo. Intenta otra vez")
  except:
    print("Lo que introduces debe ser un número")

# ¿Por qué se usa try...except?
# El bloque `try...except` se utiliza para MANEJAR ERRORES y evitar que el programa se detenga bruscamente si algo sale mal.

print(f"El número que has introducido es {numero}")

############################################################

## Bucles FOR

# Iterar una lista
frutas = ["manzana", "pera", "mandarina"]
for fruta in frutas:
  print(fruta)

# Iterar sobre cualquier cosa que sea iterable
cadena = "lucho"
for caracter in cadena:
  print(caracter)

# enumerate()
frutas = ["manzana", "pera", "mandarina"]
for index, value in enumerate(frutas): # con enumerate() en la 1era posicion tendremos el indice, y en la 2da el valor
  print(f"El índice es {index} y la fruta es {value}")

# bucles anidados
letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras:
  for numero in numeros:
    print(f"{letra}{numero}")

# break
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales):
  print(animal)
  if animal == "loro":
    print(f"El loro está escondido en el índice {idx}")
    break

# continue
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for idx, animal in enumerate(animales):
  if animal == "loro": continue
  
  print(animal)

# Comprensión de listas (list comprehension)
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
animales_mayus = [animal.upper() for animal in animales] # creamos la lista y decimos lo que queremos hacer para cada una de las listas
print(animales_mayus)

# Muestra los números pares de una lista
pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]
print(pares)

# Generar una secuencia de números del 0 al 9
for num in range(10):
  print(num)

# range(inicio, fin)
for num in range(5, 10):
  print(num)

# range(inicio, fin, paso)
for num in range(0, 1000, 5):
  print(num)

for num in range(-5, 0):
  print(num)

for num in range(10, 0, -1):
  print(num)

# transformar el rango en una lista
nums = range(10)
list_of_nums = list(nums)
print(type(list_of_nums))
print(list_of_nums)

# range para hacer un bucle x veces
for _ in range(5): print("hacer cinco veces algo")