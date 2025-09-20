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
# not: que nos permite negar una condición

# Podemos anidar condicionales, uno dentro del otro
# para determinar múltiples condiciones aunque
# siempre intentaremos evitar esto para simplificar
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

########

# Ahora vamos a ver métodos usados a la hora de modificar listas

# Creamos una lista con valores
lista1 = ['a', 'b', 'c', 'd']

# Añadir o insertar elementos a la lista
lista1.append('e') # Añade un elemento al final
print(lista1)

lista1.insert(1, '@') # Inserta un elemento en la posición que le indiquemos como primer argumento
print(lista1) #['a','1','b','c','d','e']

lista1.extend(['2', 'f']) # Añade elementos al final
print(lista1)

# Eliminar elementos de la lista
lista1.remove('@') # Eliminar la PRIMERA aparición de la cadena de texto @
print(lista1)

ultimo = lista1.pop() # Eliminar el último elemento de la lista y además te lo devuelve
print(ultimo)
print(lista1)

lista1.pop(1) # Con pop se puede decidir que elemento eliminar, en este caso, el segundo (índice 1)
print(lista1)

# Eliminar por lo bestia un índice
del lista1[-1] # -1 recordemos que es al revés
print(lista1)

lista1.clear() # Eliminar todos los elementos de la lista
print(lista1)

# Eliminar un rango de elementos
lista1 = ['1', '2', '3', '4', '5']
del lista1[1:3] # eliminamos los elementos del índice 1 al 3 (no incluye el índice 3), es decir, borramos el 2 y el 3
print(lista1)

# Ordenación de listas
print('Ordenar listas modificando la original')
numbers = [3, 10, 2, 8, 99, 101]
numbers.sort() # Modificamos la lista y guardamos en la lista la lista ordenada, NO DEVUELVE UNA COPIA -> MODIFICA LA ORIGINAL
print(numbers)

print('Ordenar listas creando una nueva lista')
numbers = [3, 10, 2, 8, 99, 101]
sorted_numbers = sorted(numbers) # Devuelve una nueva lista
print(sorted_numbers)

print("Ordenar una lista de cadenas de texto (todo minúscula)")
frutas = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print("Ordenar una lista de cadenas de texto (mezclas mayúscula y minúscula)")
frutas = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
frutas.sort(key=str.lower) # Decidimos cómo queremos que compare la cadena de texto
print(frutas)

# upper() -> convertir en mayusculas
# lower() -> convertir en minusculas

# Longitud, contar y comprobar
lista4 = ['1', '2', '4', '4']
print(len(lista4)) # Tamaño de la listas -> 4
print(lista4.count('4')) # Cuantas veces aparece el elemento '4' -> 2
print('2' in lista4) # Comprueba si hay un '2' en la lista -> True
print('6' in lista4) # -> False
