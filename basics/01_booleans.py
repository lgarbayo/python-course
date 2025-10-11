print("\nValores booleanos básicos:")
print(True)
print(False)

# Operadores de comparación: devuelven un valor booleano.
print("\nOperadores de comparación:")
print("5 > 3:", 5 > 3)        # True
print("5 < 3:", 5 < 3)        # False
print("5 == 5:", 5 == 5)      # True (igualdad)
print("5 != 3:", 5 != 3)      # True (desigualdad)
print("5 >= 5:", 5 >= 5)      # True (mayor o igual que)
print("5 <= 3:", 5 <= 3)      # False (menor o igual que)

print("\nComparación de cadenas:")
print("'manzana' < 'pera':", "manzana" < "pera") # True: la m < la p
print("'Hola' == 'hola'", "Hola" == "hola") # False (sensible a mayúsculas): case-sensitive

# Ejercicio propuesto:
#
# Escribe una expresión que determine si una persona puede entrar a un club.
# La condición es que debe ser mayor o igual de 18 años.

# Operadores lógicos: and, or, not
print("\nOperadores lógicos:")
print("True and True:", True and True)   # True
print("True and False:", True and False)  # False
print("True or False:", True or False)    # True
print("False or False:", False or False)  # False
print("not True:", not True)             # False
print("not False:", not False)            # True

# Ejercicio propuesto:
#
# Tienes un nombre de usuario y una contraseña. El sistema solo debe permitir
# el acceso si el nombre de usuario es "admin" Y la contraseña es "provisional".
# Escribe una expresión que sea True solo si el usuario y contraseña son correctos.
#
# Una tienda tiene una promoción especial los sábados o los domingos.
# Escribe una expresión que determine si hoy aplica la promoción.

# Tablas de verdad (para referencia):
print("\nTablas de verdad:")
print("\nand:")
print("A     B     A and B")
print("True  True ", True and True)
print("True  False", True and False)
print("False True ", False and True)
print("False False", False and False)

print("\n or:")
print("A     B     A or B")
print("True  True ", True or True)
print("True  False", True or False)
print("False True ", False or True)
print("False False", False or False)

print("\n not:") 
print("A     not A")
print("True ", not True)
print("False", not False)

# Ejercicio propuesto:
#
# Para ver contenido premium, un usuario debe estar logueado Y NO debe tener la cuenta suspendida.
# Escribe una expresión que sea True si el usuario puede ver el contenido.