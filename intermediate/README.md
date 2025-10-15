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
- Anclas: `^` (inicio), `# 📋 README - Carpeta INTERMEDIATE

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

 (final)
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

### Módulo 6: Diccionarios Avanzados - Ejercicios
**Archivo:** `03_dictionaries_exercises.py`

Incluye 3 ejercicios progresivos:
1. Mi libro favorito (crear y modificar diccionarios)
2. Contador de frecuencia de palabras (algoritmo con diccionarios)
3. Encontrar números complementarios (búsqueda eficiente)

---

### Módulo 7: Funciones Lambda
**Archivo:** `03_lambdas.py`

Aprenderás:
- Qué son las funciones lambda
- Sintaxis básica: `lambda argumentos: expresión`
- Usos prácticos con `map()`, `filter()`, `reduce()`
- Funciones que devuelven lambdas
- Ejercicios propuestos para practicar

```python
# Ejemplo básico
sumar = lambda x, y: x + y
print(sumar(3, 5))  # 8

# Con map
numeros = [1, 2, 3, 4]
cuadrados = list(map(lambda x: x**2, numeros))  # [1, 4, 9, 16]

# Con filter
pares = list(filter(lambda x: x % 2 == 0, numeros))  # [2, 4]

# Con reduce
from functools import reduce
producto = reduce(lambda x, y: x * y, numeros)  # 24
```

---

### Módulo 8: Funciones de Orden Superior y Closures
**Archivo:** `04_higher_order_func.py`

Aprenderás:
- Funciones que reciben funciones como argumentos
- Funciones que devuelven funciones
- Closures: funciones que recuerdan su entorno
- `map()`, `filter()` y `reduce()`
- Programación funcional en Python

```python
# Closure: función que recuerda su contexto
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

por_dos = make_multiplier(2)
print(por_dos(5))  # 10

# Map, filter, reduce
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
pares = list(filter(lambda x: x % 2 == 0, numeros))
from functools import reduce
producto = reduce(lambda x, y: x * y, numeros)
```

---

### Módulo 9: Manejo de Excepciones
**Archivo:** `05_exceptions.py`

Aprenderás:
- Try/except para capturar errores
- Bloques else y finally
- Tipos comunes de excepciones
- Lanzar excepciones con `raise`
- Buenas prácticas en manejo de errores

```python
# Captura básica
try:
    x = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por cero")

# Con else y finally
try:
    archivo = open("archivo.txt")
except FileNotFoundError:
    print("Archivo no encontrado")
else:
    print("Archivo abierto correctamente")
finally:
    print("Siempre se ejecuta")

# Lanzar excepciones
def dividir(a, b):
    if b == 0:
        raise ValueError("El divisor no puede ser cero")
    return a / b
```

---

### Módulo 10: Manejo de Archivos
**Archivo:** `06_file_handling.py`

Aprenderás:
- Leer y escribir archivos de texto
- Trabajar con archivos JSON
- Trabajar con archivos CSV
- Context manager (`with`)
- Modos de apertura de archivos

```python
# Escribir en archivo
with open("archivo.txt", "w") as f:
    f.write("Contenido del archivo\n")

# Leer de archivo
with open("archivo.txt", "r") as f:
    contenido = f.read()

# JSON
import json
datos = {"nombre": "Luis", "edad": 22}
with open("datos.json", "w") as f:
    json.dump(datos, f, indent=2)

# CSV
import csv
with open("datos.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["nombre", "edad"])
    writer.writerow(["Luis", 22])
```

---

### Módulo 11: Módulos e Importaciones
**Archivo:** `07_modules.py`

Aprenderás:
- Importar módulos completos
- Importar funciones específicas
- Usar alias para módulos
- Crear tus propios módulos
- Módulos built-in comunes
- Estructura de paquetes

```python
# Importar módulo completo
import math
print(math.pi)

# Importar función específica
from math import sqrt
print(sqrt(16))

# Importar con alias
from math import pi as PI_VALUE
print(PI_VALUE)

# Tu propio módulo
from mi_modulo import mi_funcion
mi_funcion()
```

---

### Módulo 12: Entornos Virtuales y Gestión de Paquetes
**Archivo:** `08_package_handling.py`

Aprenderás:
- Crear entornos virtuales
- Instalar paquetes con pip
- Crear archivo requirements.txt
- Activar y desactivar entornos
- Versiones específicas de paquetes

```bash
# Crear entorno virtual
python3 -m venv venv

# Activar (Linux/Mac)
source venv/bin/activate

# Instalar paquete
pip install numpy

# Ver paquetes instalados
pip list

# Guardar dependencias
pip freeze > requirements.txt

# Instalar desde requirements.txt
pip install -r requirements.txt
```

---

### Módulo 13: Ejercicios de Fechas
**Archivo:** `02_dates_exercises.py`

Incluye 5 ejercicios prácticos:
1. Formato de fecha personalizado
2. Calculadora de fechas futuras
3. Cuenta atrás para Año Nuevo
4. Convertir string a fecha (parsing)
5. Verificar si es fin de semana

---

## 🏋️ Cómo trabajar con este nivel

1. **Revisa** si completaste todos los ejercicios de `basics/`
2. **Ejecuta** los archivos en orden
3. **Estudia** los patrones y algoritmos
4. **Practica** escribiendo tus propias soluciones
5. **Completa** los ejercicios propuestos

## 📂 Estructura de Archivos de Soluciones ⚡

En la carpeta `intermediate_solutions/` encontrarás:

- **`dates_solutions.py`**: Soluciones a los 5 ejercicios de fechas
- **`dictionaries_solutions.py`**: Soluciones a los 3 ejercicios de diccionarios
- **`exceptions_solutions.py`**: Soluciones a manejo de excepciones
- **`file_handling_solutions.py`**: Notas sobre archivos XML (auto-aprendizaje)
- **`higher_order_func_solutions.py`**: Soluciones a funciones de orden superior y closures
- **`lambdas_solutions.py`**: Soluciones a ejercicios de funciones lambda
- **`regex_solutions.py`**: Notas para practicar regex (auto-aprendizaje)

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

**🚀 Siguiente Paso:** Cuando domines estos conceptos continúa con la carpeta `backend/`
