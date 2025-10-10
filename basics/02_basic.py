# Variables y asignación
my_name = "lucho"
print(my_name)

age=23
print(age)
age=22
print(age)

# tipado dinamico: el tipo de dato se determina en tiempo de ejecucion, no tienes que declararlo explicitamente
name="lucho"
print(type(name))

name=22
print(type(name))

# tipado fuerte: no realiza conversiones de tipo automaticas 
# Como vimos antes, no puedes hacer 2 + "hola". Debes convertir los tipos explícitamente.

#f-string (literal de cadena de formato)
print(f"Hola {my_name}, tengo {age -1 +1} años")

# Ejercicios propuestos:
#
# Tienes 3 productos para comprar en un supermercado. Tu objetivo es imprimir: "huevos, bacon y morcilla"
# Ejemplo: Huevos, Bacon, Morcilla

mi_nombre_de_variable="lolo" # en python para denominar variables se usan minúsculas separadas con guiones bajos: snake_case

# PYTHON NO TIENE CONSTANTES (UPPER_CASE)
# Por convención, si nombras una variable en mayúsculas, estás indicando a otros programadores que no deberían modificar su valor.

# Palabras reservadas en Python (no se pueden usar como nombres de variables)
# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']

# Anotaciones de tipo (opcional, para mayor claridad en el código)
is_user_logged_in: bool = True # Indica que la variable es un booleano: pista o anotación sobre el tipo de dato que deberia tener la variable
# Python en sí mismo no fuerza que la variable sea de ese tipo, funciona solo como anotación
# Sin embargo, herramientas externas de analisis de codigo pueden usar estas pistas para detecetar errores antes de que se ejecute el programa (p.ej. mypy)
print(is_user_logged_in)

#is_user_logged_in=42 CON TYPECHECK (mypy) ACTIVADO DA ERROR YA QUE DETECTA QUE NO ES BOOL
#print(is_user_logged_in)