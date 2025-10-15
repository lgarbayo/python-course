# 📋 README - Carpeta INTERMEDIATE

## 🎯 Objetivos de este nivel

En esta sección aprenderás conceptos **más avanzados** de Python:

- ✅ Trabajar con fechas y horas
- ✅ Diccionarios y estructuras de datos complejas
- ✅ Expresiones regulares (regex)
- ✅ Búsqueda y manipulación de datos
- ✅ Algoritmos y resolución de problemas
- ✅ Mejores prácticas de código

## 📚 Contenido

### Módulo 1: Fechas y Horas
**Archivo:** `01_dates.py`

Aprenderás:
- Módulo `datetime` para trabajar con fechas
- Obtener fecha y hora actual
- Crear fechas específicas
- Formatear fechas con `strftime()`
- Operaciones con fechas (suma/resta)
- Calcular diferencias entre fechas
- Trabajar con zonas horarias

```python
from datetime import datetime, timedelta

# Ejemplo: fecha actual
ahora = datetime.now()
print(ahora)  # 2025-02-12 15:30:45.123456

# Ejemplo: crear fecha específica
fecha = datetime(2025, 2, 12, 15, 30, 0)

# Ejemplo: formatear fecha
fecha_formateada = ahora.strftime("%d/%m/%Y %H:%M")
print(fecha_formateada)  # 12/02/2025 15:30

# Ejemplo: sumar días
mañana = datetime.now() + timedelta(days=1)
print(mañana)

# Ejemplo: diferencia entre fechas
fecha1 = datetime.now()
fecha2 = datetime(2025, 12, 31)
diferencia = fecha2 - fecha1
print(f"Faltan {diferencia.days} días")
```

---

### Módulo 2: Diccionarios Básicos
**Archivo:** `01_dictionaries.py`

Aprenderás:
- Creación y estructura de diccionarios
- Acceso a valores por clave
- Modificación de diccionarios
- Métodos: `keys()`, `values()`, `items()`
- Eliminar elementos
- Diccionarios anidados

```python
# Ejemplo: crear diccionario
persona = {
    "nombre": "Luis",
    "edad": 22,
    "ciudad": "Madrid"
}

# Ejemplo: acceso
print(persona["nombre"])  # Luis

# Ejemplo: modificar
persona["edad"] = 23

# Ejemplo: agregar clave
persona["profesion"] = "Ingeniero"

# Ejemplo: eliminar
del persona["ciudad"]

# Ejemplo: iterar
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Ejemplo: diccionario anidado
usuario = {
    "nombre": "Luis",
    "redes": {
        "github": "lgarbayo",
        "twitter": "@luiisgaarbayo"
    }
}

print(usuario["redes"]["github"])  # lgarbayo
```

---

### Módulo 3: Expresiones Regulares (Regex) - Parte 1
**Archivo:** `01_regex.py`

Aprenderás:
- Módulo `re` para expresiones regulares
- `re.search()` para buscar patrones
- `re.findall()` para encontrar todas las coincidencias
- `re.finditer()` para iterar resultados
- Métodos: `group()`, `start()`, `end()`
- Modificadores: `re.IGNORECASE`
- `re.sub()` para reemplazar texto
- Cuantificadores: `*`, `+`, `?`, `{n}`, `{n,m}`
- Clases de caracteres: `[]`, `[^]`

```python
import re

# Ejemplo: búsqueda básica
texto = "Hola mundo"
if re.search("Hola", texto):
    print("Encontrado")

# Ejemplo: encontrar todas las coincidencias
texto = "Python es genial. Python es fácil."
matches = re.findall("Python", texto)
print(f"Encontradas {len(matches)} coincidencias")

# Ejemplo: reemplazar
texto = "Hola, mundo! Hola de nuevo."
nuevo_texto = re.sub("Hola", "Adiós", texto)
print(nuevo_texto)

# Ejemplo: cuantificadores
# * : 0 o más veces
# + : 1 o más veces
# ? : 0 o 1 vez
matches = re.findall(r"a+", "aaabacaa")  # ['aaa', 'a', 'aa']

# Ejemplo: clases de caracteres
# [aeiou] : cualquier vocal
# [0-9] : cualquier dígito
# \d : dígito, \w : alfanumérico, \s : espacio
matches = re.findall(r"\d", "Tengo 25 años")  # ['2', '5']
```

---

### Módulo 4: Diccionarios Avanzados
**Archivo:** `02_dictionaries.py`

Aprenderás:
- Algoritmos usando diccionarios
- Búsqueda eficiente de pares
- Técnicas de optimización
- Casos de uso reales

```python
# Ejemplo: encontrar dos números que sumen un objetivo
def encontrar_pares(numeros, objetivo):
    """
    Encuentra dos números que sumen el objetivo.
    Retorna [índice1, índice2] o None
    """
    vistos = {}
    
    for idx, num in enumerate(numeros):
        faltante = objetivo - num
        
        if faltante in vistos:
            return [vistos[faltante], idx]
        
        vistos[num] = idx
    
    return None

resultado = encontrar_pares([4, 5, 6, 2], 8)
print(resultado)  # [2, 3] porque 6 + 2 = 8
```

---

### Módulo 5: Expresiones Regulares (Regex) - Parte 2
**Archivo:** `02_regex.py`

Aprenderás:
- El punto (`.`) para cualquier carácter
- Escape de metacaracteres (`\.`)
- Caracteres especiales: `\d`, `\w`, `\s`
- Anclas: `^` (inicio), `$` (final)
- Límites de palabra: `\b`
- Alternancia: `|`

```python
import re

# Ejemplo: punto (.)
# Coincide con cualquier carácter excepto salto de línea
matches = re.findall(r"H.la", "Hola H0la H$la")  # ['Hola', 'H0la', 'H$la']

# Ejemplo: escape de metacaracteres
matches = re.findall(r"\.", "Casa. Coche. Bicicleta.")  # ['.', '.', '.']

# Ejemplo: dígitos
matches = re.findall(r"\d", "Tengo 25 años")  # ['2', '5']

# Ejemplo: alfanuméricos
matches = re.findall(r"\w", "Hola_25")  # ['H','o','l','a','_','2','5']

# Ejemplo: espacios
matches = re.findall(r"\s", "Hola mundo")  # [' ']

# Ejemplo: anclas
matches = re.findall(r"^Hola", "Hola mundo")  # ['Hola']
matches = re.findall(r"mundo$", "Hola mundo")  # ['mundo']

# Ejemplo: validar email simple
email = "usuario@ejemplo.com"
patron = r"^[\w._%+-]+@[\w.-]+\.[a-z]{2,}$"
if re.search(patron, email, re.IGNORECASE):
    print("Email válido")
```

---

## 🏋️ Cómo trabajar con este nivel

1. **Revisa** si completaste todos los ejercicios de `basics/`
2. **Ejecuta** los archivos en orden
3. **Estudia** los patrones y algoritmos
4. **Practica** escribiendo tus propias soluciones
5. **Completa** los ejercicios propuestos

## ⚡ Ejercicios Propuestos

### Ejercicio 1: Gestor de Tareas
Crea un programa que gestione una lista de tareas con diccionarios:

```python
# Estructura sugerida
tareas = {
    1: {"titulo": "Comprar leche", "completada": False},
    2: {"titulo": "Estudiar Python", "completada": True},
}

# Funciones a implementar:
# - agregar_tarea(id, titulo)
# - marcar_completada(id)
# - eliminar_tarea(id)
# - listar_tareas()
# - listar_pendientes()
```

**Bonus:** Guarda las tareas en un archivo usando JSON

---

### Ejercicio 2: Validador de Contraseñas
Crea una función que valide contraseñas usando regex:

```python
def validar_contraseña(password):
    """
    Una contraseña válida debe tener:
    - Mínimo 8 caracteres
    - Al menos una mayúscula
    - Al menos una minúscula
    - Al menos un dígito
    - Al menos un carácter especial (@, #, $, %)
    """
    pass
```

**Test:**
```python
print(validar_contraseña("Abc123!"))        # False (7 caracteres)
print(validar_contraseña("Abc123!@"))       # True
print(validar_contraseña("abc123!@"))       # False (sin mayúscula)
```

---

### Ejercicio 3: Analizador de Logs
Crea un programa que analice un archivo de log (o simula uno):

```python
log = """
2025-02-12 10:30:45 ERROR: Connection timeout
2025-02-12 10:31:20 INFO: Server started
2025-02-12 10:32:15 WARNING: High memory usage
2025-02-12 10:33:00 ERROR: Database connection failed
2025-02-12 10:34:10 INFO: Request processed
"""

# Funciones a implementar:
# - extraer_errores(): devuelve solo los errores
# - extraer_por_hora(hora): devuelve logs de una hora específica
# - contar_por_tipo(): devuelve cuántos hay de cada tipo
# - extraer_timestamps(): devuelve todas las fechas/horas
```

---

### Ejercicio 4: Planificador de Eventos
Crea un programa que trabajar con fechas:

```python
# Dado una lista de eventos con fechas
eventos = [
    {"nombre": "Cumpleaños", "fecha": "2025-02-20"},
    {"nombre": "Examen", "fecha": "2025-03-15"},
    {"nombre": "Viaje", "fecha": "2025-04-10"},
]

# Funciones a implementar:
# - eventos_proximos(dias): eventos en los próximos N días
# - dias_hasta(evento): cuántos días faltan
# - evento_mas_cercano(): cuál es el próximo
# - ordenar_cronologicamente(): ordena por fecha
```

---

## 📖 Conceptos Clave Resumidos

| Concepto | Explicación | Ejemplo |
|----------|-------------|---------|
| **Diccionario** | Estructura clave-valor | `{"nombre": "Luis"}` |
| **Datetime** | Trabajo con fechas y horas | `datetime.now()` |
| **Regex** | Búsqueda de patrones en texto | `r"\d+"` |
| **Módulo** | Librería de Python | `import re`, `import datetime` |
| **Patrón** | Expresión que describe texto | `[a-z]+`, `\d{3}` |
| **Algoritmo** | Proceso paso a paso | Búsqueda de pares en lista |

---

## 🔗 Recursos Útiles

- [Documentación datetime](https://docs.python.org/3/library/datetime.html)
- [Documentación regex](https://docs.python.org/3/library/re.html)
- [Regex101.com](https://regex101.com/) - Prueba regex interactivamente
- [RegexCheatsheet.com](https://www.regular-expressions.info/tutorial.html)
- [Real Python - Dictionaries](https://realpython.com/python-dicts/)

---

## 🧠 Diferencias con Basics

| Aspecto | Basics | Intermediate |
|--------|--------|-------------|
| **Enfoque** | Conceptos fundamentales | Estructura de datos y algoritmos |
| **Complejidad** | Principiante | Intermedio |
| **Uso de módulos** | Mínimo | Extensivo (re, datetime) |
| **Algoritmos** | Simples | Más eficientes y optimizados |
| **Proyectos** | Ejercicios pequeños | Proyectos integradores |

---

## ✅ Checklist de Finalización

- [ ] Entiendo cómo usar diccionarios
- [ ] Puedo trabajar con fechas y horas
- [ ] Conozco los patrones básicos de regex
- [ ] Puedo buscar y reemplazar texto con regex
- [ ] He implementado algoritmos usando diccionarios
- [ ] Puedo validar datos con regex
- [ ] He completado los 4 ejercicios propuestos
- [ ] Entiendo cuándo usar cada herramienta

---

**🚀 Siguiente Paso:**

Cuando domines estos conceptos, considera:
- **Programación Orientada a Objetos (POO):**
  - Clases y objetos
  - Herencia y polimorfismo
  - Encapsulación

- **Manejo de Archivos:**
  - Leer y escribir archivos
  - JSON y CSV
  - Serialización

- **Bases de Datos:**
  - SQL básico
  - SQLite con Python

- **APIs y Web:**
  - Requests HTTP
  - Web scraping
  - Flask o Django

---
