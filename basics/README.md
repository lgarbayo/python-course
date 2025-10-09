# 📋 README - Carpeta BASICS

## 🎯 Objetivos de este nivel

En esta sección aprenderás los **fundamentos esenciales** de Python:

- ✅ Concepto de variables y tipos de datos
- ✅ Operadores y expresiones
- ✅ Booleanos y lógica
- ✅ Control de flujo (if/else, bucles)
- ✅ Funciones básicas
- ✅ Trabajar con input del usuario

## 📚 Contenido

### Módulo 1: Introducción y Variables
**Archivo:** `01_basic.py`

Aprenderás:
- Uso de `print()` para mostrar información
- Tipos de datos: int, float, str, bool, etc.
- Casting de tipos (conversiones)
- Operaciones básicas

```python
# Ejemplo: mostrar información
print("Hola Mundo")

# Ejemplo: tipos de datos
edad = 25
altura = 1.75
nombre = "Luis"

print(f"{nombre} tiene {edad} años")
```

---

### Módulo 2: Booleanos y Operadores Lógicos
**Archivo:** `01_booleans.py`

Aprenderás:
- Valores booleanos (True/False)
- Operadores de comparación: `>`, `<`, `==`, `!=`, etc.
- Operadores lógicos: `and`, `or`, `not`
- Tablas de verdad

```python
# Ejemplo: comparaciones
print(5 > 3)           # True
print("manzana" < "pera")  # True

# Ejemplo: lógica
edad = 20
tiene_dinero = True

if edad >= 18 and tiene_dinero:
    print("Puedes ir de compras")
```

---

### Módulo 3: Control de Flujo
**Archivo:** `01_flow_control.py`

Aprenderás:
- Condicionales: `if`, `elif`, `else`
- Listas y acceso a elementos
- Bucles: `for` y `while`
- Break y continue
- Slicing de listas
- List comprehension

```python
# Ejemplo: if/elif/else
nota = 7
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
else:
    print("Aprobado")

# Ejemplo: bucle for
frutas = ["manzana", "pera", "plátano"]
for fruta in frutas:
    print(f"Me gusta la {fruta}")

# Ejemplo: list comprehension
pares = [n for n in range(10) if n % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]
```

---

### Módulo 4: Funciones Básicas
**Archivo:** `01_functions.py`

Aprenderás:
- Definición de funciones
- Parámetros y retorno de valores
- Valores por defecto
- Argumentos posicionales y nombrados
- `*args` y `**kwargs`
- Docstrings

```python
# Ejemplo: función simple
def saludar(nombre):
    """Saluda a una persona"""
    print(f"¡Hola {nombre}!")

saludar("Luis")

# Ejemplo: función con retorno
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)
print(resultado)  # 8

# Ejemplo: parámetros por defecto
def multiplicar(a, b=2):
    return a * b

print(multiplicar(5))      # 10
print(multiplicar(5, 3))   # 15
```

---

### Módulo 5: Variables y Tipado
**Archivo:** `02_basic.py`

Aprenderás:
- Tipado dinámico en Python
- Tipado fuerte (no hace conversiones automáticas)
- F-strings para formateo
- Snake_case (convención de nombres)
- Palabras reservadas de Python
- Type hints (anotaciones de tipo)

```python
# Ejemplo: tipado dinámico
nombre = "Luis"
print(type(nombre))  # <class 'str'>

nombre = 22
print(type(nombre))  # <class 'int'>

# Ejemplo: f-strings
edad = 25
print(f"Tengo {edad} años")

# Ejemplo: type hints
edad: int = 25
nombre: str = "Luis"
```

---

### Módulo 6: Bucles Avanzados
**Archivo:** `02_flow_control.py`

Aprenderás:
- Bucles `while` con condiciones
- Break y continue en bucles
- Else en bucles
- Bucles `for` sobre iterables
- `enumerate()` para obtener índice y valor
- `range()` y sus parámetros

```python
# Ejemplo: while
contador = 0
while contador < 5:
    print(contador)
    contador += 1

# Ejemplo: for con enumerate
frutas = ["manzana", "pera", "plátano"]
for idx, fruta in enumerate(frutas):
    print(f"{idx}: {fruta}")

# Ejemplo: range
for num in range(0, 10, 2):
    print(num)  # 0, 2, 4, 6, 8
```

---

### Módulo 7: Input del Usuario
**Archivo:** `03_basic.py`

Aprenderás:
- Función `input()` para leer del usuario
- Conversión de tipos desde input
- Múltiples valores con `split()`

```python
# Ejemplo: input básico
nombre = input("¿Cómo te llamas?\n")
print(f"Hola {nombre}")

# Ejemplo: convertir a número
edad = int(input("¿Cuántos años tienes?\n"))
print(f"Tienes {edad} años")

# Ejemplo: múltiples valores
pais, ciudad = input("País y ciudad:\n").split()
print(f"Vives en {pais}, {ciudad}")
```

---

## 🏋️ Cómo trabajar con este nivel

1. **Lee** el archivo `README.md` (este documento)
2. **Ejecuta** los archivos `.py` en orden (01_basic.py, 01_booleans.py, etc.)
3. **Estudia** los comentarios dentro del código
4. **Prueba** modificando los ejemplos
5. **Completa** los ejercicios propuestos

## ⚡ Ejercicios Propuestos

### Ejercicio 1: Calculadora Simple
Crea un programa que pida dos números y muestre suma, resta, multiplicación y división.

```python
# Tu código aquí
```

**Solución esperada:**
```
Número 1: 10
Número 2: 5
Suma: 15
Resta: 5
Multiplicación: 50
División: 2.0
```

### Ejercicio 2: Adivina el Número
Crea un juego donde el usuario tenga que adivinar un número entre 1 y 100.

**Pistas:**
- Usa `import random` y `random.randint(1, 100)`
- Usa un bucle `while`
- Dale pistas si es mayor o menor

### Ejercicio 3: Tabla de Multiplicar
Crea una función que reciba un número y muestre su tabla de multiplicar.

```python
def tabla_multiplicar(numero):
    # Tu código aquí
    pass
```

---

## 📖 Conceptos Clave Resumidos

| Concepto | Explicación | Ejemplo |
|----------|-------------|---------|
| **Variable** | Contenedor de un valor | `nombre = "Luis"` |
| **Tipo de dato** | Categoría del valor | `int`, `str`, `float`, `bool` |
| **Casting** | Conversión entre tipos | `int("5")` → `5` |
| **Operador** | Símbolo para operaciones | `+`, `-`, `==`, `and` |
| **Función** | Bloque reutilizable de código | `def saludar():` |
| **Bucle** | Repetición de código | `for`, `while` |
| **Condicional** | Decisión en el código | `if`, `elif`, `else` |

---

## 🔗 Recursos Útiles

- [Documentación oficial de Python](https://docs.python.org/3/)
- [Python Cheat Sheet](https://www.pythoncheatsheet.org/)
- [W3Schools Python Tutorial](https://www.w3schools.com/python/)

---

## ✅ Checklist de Finalización

- [ ] Entiendo qué son variables y tipos de datos
- [ ] Puedo usar operadores lógicos correctamente
- [ ] Sé cómo usar if/elif/else
- [ ] Puedo crear y usar listas
- [ ] Puedo escribir funciones básicas
- [ ] Entiendo bucles for y while
- [ ] Puedo trabajar con input del usuario
- [ ] He completado los 3 ejercicios propuestos

---

**Siguiente paso:** Cuando domines estos conceptos, continúa con la carpeta `intermediate/`

---
