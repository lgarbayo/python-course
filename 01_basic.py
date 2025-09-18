#mostrar informacion en consola
print("Hola Mundo")
print('hola amigos')
print("py", "th", "on", end= " ")
print("py", "th", "on", sep="")

#tipos de datos
print(5)
#int, float, complex, str, bool, NoneType, list, tuple, dict, range, set...
print(type(-5))
print(type(3.14))
print(type(1.0))
print(type(1e3))
print(type(1 + 2j))
print(type("str:"))
print(type("""
      """))
print(type(True))
print(type(False))
print(type(1 < 2))
print(type(None))

"""
    cadena de texto usada para documentar
"""

#casting de tipos
print("Conversion de tipos")
print(type(100)) #tipado fuerte, no realiza conversiones de tipos automaticas
#print("100" + 2) :error porque el primero es str, entonces + actua como concat cadenas
    #al reves el + seria de suma
print(2 + int("100"))
print("100" + str(2))
print(float(3.16))
print(int(3.1416)) #convierte en entero pierdes decimales
print(bool(3))
print(bool(0)) #unico q se convierte a false
print(bool(1))
print(bool("")) #unico str q se convierte a false porq es cadena vacia, con un espacio ya tiene algo
print(bool(" "))
print(bool("False"))

print(round(3.5))
print(round(2.5))
#round justo en .5 en python redondea al PAR más cercano
