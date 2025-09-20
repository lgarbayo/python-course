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
print(restar.__doc__)
help(restar)

# Parámetros por defecto
def multiplicar(a, b = 2): return a * b
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

# Argumentos de longitud de variable (*args):
def sumar_numeros(*args):
  suma = 0
  for numero in args:
    suma += numero
  return suma
print(sumar_numeros(1, 2, 3, 4, 5))
print(sumar_numeros(1, 2))

# Argumentos de clave-valor variable (**kwargs):
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