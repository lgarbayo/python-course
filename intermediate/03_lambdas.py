# Las funciones lambda en Python son funciones anónimas, es decir, no tienen un nombre asociado.
# Se utilizan para crear funciones pequeñas y rápidas, generalmente en una sola línea.
# Su sintaxis básica es: lambda argumentos: expresión
# Son útiles cuando necesitas una función simple y temporal, por ejemplo, como argumento de otras funciones (map, filter, sorted, etc).
# Las lambdas pueden tener cualquier número de argumentos, pero solo una expresión, cuyo resultado es el valor de retorno.
# Ejemplo básico:
# lambda x, y: x + y
# Esta lambda toma dos argumentos y devuelve su suma.

lambda first_value, second_value: first_value + second_value
sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(4, 5))

# También puedes usar lambdas dentro de funciones para crear funciones personalizadas:
def sum_three_values(value):
    # Esta función devuelve una lambda que suma tres valores: los dos argumentos y el valor fijo
    return lambda first_value, second_value: first_value + second_value + value
print(sum_three_values(10)(4, 5))
# En este ejemplo, sum_three_values(10) devuelve una función que suma 10 al resultado de sumar los dos argumentos.

# Las lambdas se usan mucho en programación funcional y para operaciones rápidas sobre colecciones.
# Ejemplo: filtrar, transformar, ordenar, reducir listas, etc.

# --- Ejercicios para practicar lambdas (apoyarse en la leccion 04)---
# 1. Usando lambda y filter, obtén los números impares de la lista [1, 2, 3, 4, 5, 6, 7].
# 2. Usando lambda y map, convierte una lista de temperaturas en Celsius a Fahrenheit.
# 3. Ordena una lista de tuplas (nombre, edad) por edad usando sorted y lambda.
# 4. Usando reduce y lambda, suma todos los elementos de la lista [10, 20, 30, 40].
# 5. Escribe una lambda que reciba un número y devuelva 'par' si es par y 'impar' si es impar.
# Escribe las soluciones en intermediate_solutions/lambdas_solutions.py