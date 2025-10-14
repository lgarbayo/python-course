# Las funciones de orden superior son funciones que pueden recibir otras funciones como argumentos o devolver funciones como resultado.
# Son muy útiles para abstraer lógica, reutilizar código y trabajar con programación funcional.
# En Python, las funciones son objetos de primera clase, lo que significa que pueden ser pasadas como argumentos, retornadas y asignadas a variables.
# Ejemplo clásico: map, filter, reduce usan funciones de orden superior.
# En este archivo, sum_two_values_and_value recibe una función (f_sum) como argumento y la aplica al resultado de sumar dos valores.
# Esto permite modificar el comportamiento de la función fácilmente pasando diferentes funciones.

def sum_one(value):
    return value + 1

def sum_two_values_and_value(first_value, second_value,f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_value(4, 5, sum_one))

# --- Closures ---
# Un closure es una función que recuerda el entorno en el que fue creada, incluso después de que ese entorno haya terminado.
# Permite que una función interna acceda a variables locales de la función externa, aunque la función externa ya haya finalizado.
# Los closures son útiles para crear funciones personalizadas con estado propio.

# Ejemplo de closure:
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

por_dos = make_multiplier(2)
por_tres = make_multiplier(3)
print('Closure por_dos:', por_dos(5))  # 10
print('Closure por_tres:', por_tres(5))  # 15
# En este ejemplo, las funciones por_dos y por_tres recuerdan el valor de factor con el que fueron creadas.

# --- Funciones de orden superior integradas (built-in) ---
# Python incluye varias funciones de orden superior muy útiles:
# - map: aplica una función a cada elemento de una colección.
# - filter: filtra elementos de una colección según una condición.
# - reduce: reduce una colección a un solo valor aplicando una función acumulativa.

numbers = [1, 2, 3, 4, 5]

# map: eleva al cuadrado cada elemento
squared = list(map(lambda x: x**2, numbers))
print('map (cuadrados):', squared)

# filter: selecciona los números pares
even = list(filter(lambda x: x % 2 == 0, numbers))
print('filter (pares):', even)

# reduce: multiplica todos los elementos
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print('reduce (producto):', product)

# Estas funciones permiten escribir código más conciso y expresivo, aprovechando la programación funcional en Python.

# --- Ejercicios para practicar funciones de orden superior y closures ---
# 1. Escribe una función de orden superior que reciba una lista y una función, y aplique esa función a cada elemento de la lista.
# 2. Crea un closure que permita sumar un número fijo a cualquier número que se le pase.
# 3. Usando map y lambda, multiplica cada elemento de la lista [2, 4, 6, 8] por 3.
# 4. Usando filter y lambda, filtra los nombres que empiezan por la letra 'A' en una lista de nombres.
# 5. Usando reduce y lambda, encuentra el máximo valor en la lista [5, 9, 2, 8, 1].
# Escribe las soluciones en intermediate_solutions/higher_order_func_solutions.py