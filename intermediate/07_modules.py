# ============================================
# GUÍA COMPLETA DE MÓDULOS EN PYTHON
# ============================================

# Un módulo es un archivo .py que contiene código (funciones, variables, clases)
# que puedes reutilizar en otros programas. Python tiene módulos built-in
# (como math, os, sys) y puedes crear los tuyos propios.

# ============================================
# 1. IMPORTAR UN MÓDULO COMPLETO
# ============================================

# SINTAXIS:
# import math
#
# EXPLICACIÓN:
# Importa todo el módulo "math" (módulo built-in para operaciones matemáticas)
# Para usar algo del módulo, debes escribir: math.funcion()
#
# EJEMPLO:

import math

# Acceder a la constante pi del módulo math
print(math.pi)  # Output: 3.141592653589793

# Usar la función pow() del módulo math
print(math.pow(2, 8))  # Output: 256.0 (2 elevado a 8)

# VENTAJA: Claridad. Sabes que pi viene del módulo math
# DESVENTAJA: Escribir "math." cada vez es más largo


# ============================================
# 2. IMPORTAR ALGO ESPECÍFICO DE UN MÓDULO
# ============================================

# SINTAXIS:
# from math import pi
#
# EXPLICACIÓN:
# Importa SOLO la constante "pi" del módulo math
# Ahora puedes usar "pi" directamente sin escribir "math."
#
# EJEMPLO:
from math import pi
print(pi)  # Output: 3.141592653589793

# VENTAJA: Código más corto y directo
# DESVENTAJA: Menos claro de dónde viene "pi"


# ============================================
# 3. IMPORTAR CON ALIAS (RENOMBRAR)
# ============================================

# SINTAXIS:
# from math import pi as PI_VALUE
#
# EXPLICACIÓN:
# Importa "pi" pero lo renombras como "PI_VALUE"
# Útil para evitar conflictos de nombres o hacer código más legible
#
# EJEMPLO:
from math import pi as PI_VALUE
print(PI_VALUE)  # Output: 3.141592653589793

# VENTAJA: Puedes usar nombres más descriptivos
# EJEMPLO: Si tuvieras varias constantes "pi", las podrías diferenciar


# ============================================
# 4. IMPORTAR TODO DE UN MÓDULO (NO RECOMENDADO)
# ============================================

# SINTAXIS:
# from math import *
#
# EXPLICACIÓN:
# Importa TODAS las funciones y constantes del módulo
# Luego puedes usar sin prefijo: sin(), cos(), pi, etc.
#
# EJEMPLO:
# from math import *
# print(pi)
# print(sin(0))
#
# ⚠️ NO RECOMENDADO porque:
# - No sabes exactamente qué se importó
# - Puede causar conflictos si hay nombres duplicados
# - Es difícil de mantener y debuggear


# ============================================
# 5. CREAR Y USAR TUS PROPIOS MÓDULOS
# ============================================

# SUPONGAMOS QUE TIENES UN ARCHIVO LLAMADO "my_module.py"
# CON ESTE CONTENIDO:
#
# def sumValue(a, b, c):
#     """Suma tres números"""
#     return a + b + c
#
# def printValue(text):
#     """Imprime un texto"""
#     print(f"Texto: {text}")


# ============================================
# 6. IMPORTAR TU MÓDULO COMPLETO
# ============================================

# SINTAXIS:
# import my_module
#
# EXPLICACIÓN:
# Importa todo tu módulo personalizado
# Para usar las funciones, debes escribir: my_module.funcion()

import my_module

# Llamar a la función sumValue del módulo my_module
my_module.sumValue(5, 3, 1)  # Output: 9

# Llamar a la función printValue del módulo my_module
my_module.printValue("Hola Python!")  # Output: Texto: Hola Python!

# VENTAJA: Claro dónde vienen las funciones
# DESVENTAJA: Más código al escribir "my_module."


# ============================================
# 7. IMPORTAR FUNCIONES ESPECÍFICAS DE TU MÓDULO
# ============================================

# SINTAXIS:
# from my_module import sumValue, printValue
#
# EXPLICACIÓN:
# Importa SOLO las funciones que necesitas de tu módulo
# Ahora puedes usarlas directamente sin "my_module."

from my_module import sumValue, printValue

# Llamar directamente a sumValue
sumValue(5, 3, 1)  # Output: 9

# Llamar directamente a printValue
printValue("Hola python")  # Output: Texto: Hola python

# VENTAJA: Código más corto
# Puedes importar múltiples cosas separadas por comas


# ============================================
# 8. IMPORTAR CON ALIAS (TUS MÓDULOS)
# ============================================

# SINTAXIS:
# from my_module import sumValue as sum_three
# from my_module import printValue as print_text
#
# EXPLICACIÓN:
# Renombras las funciones de tu módulo
# Útil si quieres nombres más cortos o descriptivos
#
# EJEMPLO:
# from my_module import sumValue as sum_three
# sum_three(5, 3, 1)


# ============================================
# 9. RENOMBRAR UN MÓDULO COMPLETO
# ============================================

# SINTAXIS:
# import my_module as mm
#
# EXPLICACIÓN:
# Importas el módulo pero lo llamas "mm"
# Ahora usas: mm.sumValue(), mm.printValue()
#
# EJEMPLO:
# import my_module as mm
# mm.sumValue(5, 3, 1)
# mm.printValue("Hola!")


# ============================================
# 10. ESTRUCTURA DE CARPETAS CON MÓDULOS
# ============================================

# mi-proyecto/
# │
# ├── main.py              # Archivo principal
# ├── my_module.py         # Tu módulo personalizado
# ├── utils.py             # Otro módulo personalizado
# └── helpers/
#     ├── __init__.py      # Convierte carpeta en paquete
#     └── helper_module.py # Módulo dentro de carpeta


# ============================================
# 11. IMPORTAR DE CARPETAS (PAQUETES)
# ============================================

# Si tienes: helpers/__init__.py y helpers/helper_module.py
#
# SINTAXIS:
# from helpers.helper_module import my_function
# import helpers.helper_module
#
# EXPLICACIÓN:
# Importas módulos que están dentro de carpetas
# El archivo __init__.py convierte la carpeta en paquete


# ============================================
# 12. MÓDULOS BUILT-IN COMUNES
# ============================================

# math      → Operaciones matemáticas (sin, cos, sqrt, pi, etc.)
# os        → Sistema operativo (crear carpetas, listar archivos, etc.)
# sys       → Sistema (argumentos, path, salida, etc.)
# random    → Números aleatorios
# datetime  → Fechas y horas
# json      → Trabajar con archivos JSON
# csv       → Trabajar con archivos CSV
# requests  → Descargar contenido de internet (necesita pip install)
# flask     → Crear aplicaciones web (necesita pip install)

# EJEMPLO DE USO:
import os
import random
from datetime import datetime

# Ver el directorio actual
print(os.getcwd())

# Número aleatorio entre 1 y 100
print(random.randint(1, 100))

# Fecha y hora actual
print(datetime.now())


# ============================================
# 13. CREAR TU PROPIO MÓDULO (PASO A PASO)
# ============================================

# PASO 1: Crea un archivo "calculadora.py" con:
#
# def sumar(a, b):
#     return a + b
#
# def restar(a, b):
#     return a - b
#
# def multiplicar(a, b):
#     return a * b


# PASO 2: En tu archivo principal, importa:
#
# from calculadora import sumar, restar, multiplicar
#
# print(sumar(10, 5))         # Output: 15
# print(restar(10, 5))        # Output: 5
# print(multiplicar(10, 5))   # Output: 50


# ============================================
# 14. VERIFICAR SI UN MÓDULO EXISTE
# ============================================

# Antes de importar, puedes verificar si está disponible:

# try:
#     import numpy
#     print("NumPy está disponible")
# except ImportError:
#     print("NumPy no está instalado")


# ============================================
# 15. VER QUÉ HAY DENTRO DE UN MÓDULO
# ============================================

# FUNCIÓN: dir(módulo)
# EXPLICACIÓN: Muestra todas las funciones y variables del módulo
#
# EJEMPLO:

print("\n--- Contenido del módulo math ---")
print(dir(math))

# FUNCIÓN: help(módulo.funcion)
# EXPLICACIÓN: Muestra la documentación de una función
#
# EJEMPLO:
help(math.sqrt)  # Muestra documentación de sqrt()


# ============================================
# COMPARACIÓN: DIFERENTES FORMAS DE IMPORTAR
# ============================================

# OPCIÓN 1: Importar módulo completo
# import math
# math.pi, math.sqrt()
# ✅ Claro y explícito

# OPCIÓN 2: Importar función específica
# from math import pi, sqrt
# pi, sqrt()
# ✅ Código más corto

# OPCIÓN 3: Importar con alias
# from math import pi as PI
# PI
# ✅ Nombres personalizados

# OPCIÓN 4: Importar todo (NO RECOMENDADO)
# from math import *
# pi, sqrt()
# ❌ Poco claro, puede causar conflictos


# ============================================
# BUENAS PRÁCTICAS
# ============================================

# 1. Imports al inicio del archivo
# 2. Agrupa: primero built-in, luego third-party, luego locales
# 3. Un import por línea (para mayor claridad)
# 4. Usa alias solo si es necesario
# 5. Evita "import *"
# 6. Comenta si el nombre de un módulo no es obvio

# EJEMPLO DE BUEN ORDEN:

# # Built-in modules
# import os
# import sys
# from datetime import datetime
#
# # Third-party modules
# import numpy as np
# import pandas as pd
#
# # Local modules
# import my_module
# from helpers import utility_function