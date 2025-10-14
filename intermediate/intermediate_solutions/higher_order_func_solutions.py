# Soluciones a los ejercicios de funciones de orden superior y closures

# 1. Función de orden superior para aplicar una función a cada elemento
def aplicar_funcion(lista, funcion):
    return [funcion(x) for x in lista]

# 2. Closure para sumar un número fijo
def make_adder(fijo):
    def adder(x):
        return x + fijo
    return adder

# 3. Multiplicar cada elemento por 3
multiplicados = list(map(lambda x: x * 3, [2, 4, 6, 8]))

# 4. Filtrar nombres que empiezan por 'A'
nombres = ['Ana', 'Luis', 'Alberto', 'Marta']
filtrados = list(filter(lambda nombre: nombre.startswith('A'), nombres))

# 5. Encontrar el máximo con reduce
from functools import reduce
maximo = reduce(lambda x, y: x if x > y else y, [5, 9, 2, 8, 1])
