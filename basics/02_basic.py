my_name = "lucho"
print(my_name)

age=23
print(age)
age=22
print(age)

#tipado dinamico: el tipo de dato se determina en tiempo de ejecucion
#que no tienes que declararlo explicitamente
name="lucho"
print(type(name))

name=22
print(type(name))

#tipado fuerte: no realiza conversiones de tipo automaticas

#f-string (literal de cadena de formato)
print(f"Hola {my_name}, tengo {age -1 +1} años")

mi_nombre_de_variable="lolo" #snake_case

#NO TIENE CONSTANTES (UPPER_CASE)

# Palabras reservadas en Python (no se pueden usar como nombres de variables)

# ['False', 'None', 'True', 'and', 'as', 'assert',
# 'async', 'await', 'break', 'class', 'continue',
# 'def', 'del', 'elif', 'else', 'except', 'finally',
# 'for', 'from', 'global', 'if', 'import', 'in', 'is',
# 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']

#Anotaciones de tipo (opcional, para mayor claridad en el código)
is_user_logged_in: bool = True #Indica que la variable es un booleano
print(is_user_logged_in)

#is_user_logged_in=42 CON TYPECHECK ACTIVADO DA ERROR
#print(is_user_logged_in)