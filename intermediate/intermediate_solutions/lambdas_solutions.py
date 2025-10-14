# Soluciones a los ejercicios de lambdas

# 1. Números impares
impares = list(filter(lambda x: x % 2 != 0, [1, 2, 3, 4, 5, 6, 7]))

# 2. Celsius a Fahrenheit
celsius = [0, 20, 30, 40]
fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))

# 3. Ordenar tuplas por edad
personas = [('Ana', 23), ('Luis', 19), ('Marta', 31)]
ordenadas = sorted(personas, key=lambda x: x[1])

# 4. Suma con reduce
from functools import reduce
suma = reduce(lambda x, y: x + y, [10, 20, 30, 40])

# 5. Par o impar
par_impar = lambda x: 'par' if x % 2 == 0 else 'impar'
