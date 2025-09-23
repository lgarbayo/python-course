persona = {
  "nombre": "luis",
  "edad": 22,
  "es_estudiante": True,
  "calificaciones": [7, 8, 9],
  "socials": {
    "github": "lgarbayo",
    "instagram": "@luiisgaarbayo",
    "linkedin": "luis-garbayo"
  }
}

# para acceder a los valores
print(persona["nombre"])
print(persona["calificaciones"][2])
print(persona["socials"]["linkedin"])

# cambiar valores al acceder
persona["nombre"] = "lgfernandez"
persona["calificaciones"][2] = 10

# eliminar completamente una propiedad
del persona["edad"]
print(persona)
# para acceder al valor, recuperarlo y eliminarlo:
es_estudiante = persona.pop("es_estudiante") 
print(f"es_estudiante: {es_estudiante}")
print(persona)

# sobreescribir un diccionario con otro diccionario
a = { "name": "luis", "age": 22 }
b = { "name": "lolo", "es_estudiante": True }
a.update(b)
print(a)

# comprobar si existe una propiedad
print("nombre" in persona) # True
print("name" in persona) # False

# obtener todas las claves
print(persona.keys())
# obtener todas los valores
print(persona.values())
# obtener tanto clave como valor
print(persona.items())

for key, value in persona.items():
  print(f"{key}: {value}")