#print("Hola, como te llamas")
name=input("Hola, como te llamas\n")

print(f"Hola {name}, encantado de conocerte")

#toda la info que introduzca el usuario en el input va a ser STRING, siempre
age = input("¿Cuántos años tienes?\n")
age = int(age)
print(f"Tienes {age} años")

print("Obtener múltiples valores a la vez")
country, city = input("¿En qué país y ciudad vives?\n").split()

print(f"Vives en {country}, {city}")

# Ejercicios propuestos:
#
# Pide al usuario su nombre y edad, y calcula la edad que tendrá el próximo año.
#
# Pide al usuario dos números, los suma y muestra el resultado.
# Se usa float() para permitir números con decimales.
#
# Pide al usuario su nombre y apellido en una sola línea y le da la bienvenida.