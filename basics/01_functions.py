## Definición de una función

# def nombre_de_la_funcion(parametro1, parametro2, ...):
#   """docstring"""
#   cuerpo de la función
# return valor_de_retorno # opcional

# Ejemplo de una función para imprimir algo en consola
def saludar(): print("¡Hola!")
saludar()

# Ejemplo de una función con parámetro
def saludar_a(nombre): print(f"¡Hola {nombre}!")
saludar_a("lolo")

# Funciones con más parámetros
def sumar(a, b):
   suma = a + b
   return suma
result = sumar(2, 3)
print(result)

# Documentar las funciones con docstring
def restar(a, b): 
  """Resta dos numeros y devuelve el resultado""" # descripcion de la funcion en cadena de texto multilinea
  return a - b
print(restar.__doc__) # Acceder a la docstring (atributo especial __doc__ para documentacion)
help(restar) # help genera una ayuda formateada y mas completa (generalmente incluye tambien la firma de la funcion ( nombre y parametros ))

# Parámetros por defecto
def multiplicar(a, b = 2): return a * b # b es un parametro opcional con valor por defecto 2
print(multiplicar(2)) # a = 2
print(multiplicar(2, 3)) # el valor por defecto es opcional -> a * b = 2 * 3 = 6 

# Argumentos por posición
def describir_persona(nombre: str, edad: int, sexo: str):
  print(f"Soy {nombre}, tengo {edad} años y soy {sexo}")

# parámetros posicionales
describir_persona(1, 22, "helicoptero de combate")
describir_persona("lucho", 22, "muuuuuuy bueeeno")
describir_persona("hombre", "edad", 23)

# Argumentos por clave
# parámetros nombrados
describir_persona(sexo="muuuuy bueeno", nombre="luis", edad=22)
describir_persona(sexo="hombre", nombre="andy", edad=21) 

# Argumentos de longitud de variable (*args): # * significa que la funcion puede recibir cualquier numero de argumentos posicionales
def sumar_numeros(*args):
  suma = 0
  for numero in args:
    suma += numero
  return suma
print(sumar_numeros(1, 2, 3, 4, 5))
print(sumar_numeros(1, 2))
# util cuando no sabes cuantos argumentos necesitaras procesar

# Argumentos de clave-valor variable (**kwargs): # ** significa que la funcion puede recibir cualquier numero de argumentos nombrados
def mostrar_informacion_de(**kwargs):
  for clave, valor in kwargs.items():
    print(f"{clave}: {valor}")
mostrar_informacion_de(nombre="luis", edad=22, sexo="home", es="muy bueeeeeno", is_rich=False)

def count_carnivore_dinosaur_eggs(egg_list) -> int:
  """
  Esta función recibe una lista de numeros enteros que representan la cantidad de huevos que han puesto diferentes dinosaurios en el parque jurásico y los de número par son de carnívoros. Devuelve un número con la suma de todos los huevos de carnívoros.
  """
  total_carnivore_eggs = 0

  for eggs in egg_list:
    if eggs % 2 == 0:
      total_carnivore_eggs += eggs
  return total_carnivore_eggs

egg_list = [3, 4, 7, 5, 8]
print(count_carnivore_dinosaur_eggs(egg_list)) # 12

# --- Ejercicio 1: Calculadora de Área ---
#
# Crea una función llamada `calculate_rectangle_area` que acepte dos argumentos: `width` y `height`. 
# La función debe devolver el área del rectángulo (width * height).
# Añade un docstring que explique lo que hace la función.
#
# --- Ejercicio 2: Saludo Personalizado ---
#
# Crea una función llamada `create_greeting` que acepte un argumento `name` y un argumento opcional `greeting` con el valor por defecto "Hello".
# La función debe devolver un saludo en formato "Greeting, Name!".
# Ejemplo: create_greeting("Luis") -> "Hello, Luis!"
#
# --- Ejercicio 3: Promedio de Calificaciones ---
#
# Crea una función llamada `calculate_average` que acepte un número variable de argumentos numéricos (`*args`).
# La función debe devolver el promedio de todos los números pasados.
# Si no se pasan argumentos, debe devolver 0.
#
# --- Ejercicio 4: Constructor de Perfiles ---
#
# Crea una función llamada `build_user_profile` que acepte un número variable de argumentos de palabra clave (`**kwargs`).
# La función debe imprimir cada par clave-valor en una nueva línea.
#
# --- Ejercicio 5: Validador de Contraseña ---
#
# Crea una función `is_password_valid(password: str) -> bool` que verifique
# si una contraseña es segura.
#
# Criterios de validez:
# 1. Debe tener al menos 8 caracteres.
# 2. Debe contener al menos un número. (Pista: puedes usar `any(c.isdigit() for c in password)`)
#
# La función debe devolver `True` si es válida, y `False` en caso contrario.