#print("Hola, como te llamas")
nombre=input("Hola, como te llamas\n")

print(f"Hola {nombre}, encantado de conocerte")

#toda la info que introduzca el usuario en el input va a ser STRING, siempre
age = input("¿Cuántos años tienes?\n")
age = int(age)
print(f"Tienes {age} años")

print("Obtener múltiples valores a la vez")
country, city = input("¿En qué país y ciudad vives?\n").split()

print(f"Vives en {country}, {city}")