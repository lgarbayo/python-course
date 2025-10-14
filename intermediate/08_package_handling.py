# ============================================
# GUÍA COMPLETA DE ENTORNOS VIRTUALES EN PYTHON
# ============================================

# Un entorno virtual es un directorio aislado donde puedes instalar paquetes
# específicos para tu proyecto sin afectar el Python del sistema.

# ============================================
# 1. CREAR UN ENTORNO VIRTUAL
# ============================================

# COMANDO EN TERMINAL:
# python3 -m venv venv
#
# EXPLICACIÓN:
# - python3 -m venv: Módulo de Python para crear entornos virtuales
# - venv: Nombre del directorio donde se guardará el entorno
#   (puedes ponerle otro nombre como "mi_entorno", "env", etc.)
#
# RESULTADO:
# Se crea una carpeta "venv" con una copia aislada de Python


# ============================================
# 2. ACTIVAR EL ENTORNO VIRTUAL
# ============================================

# COMANDO EN TERMINAL (Linux/Mac):
# source venv/bin/activate
#
# COMANDO EN TERMINAL (Windows):
# venv\Scripts\activate
#
# EXPLICACIÓN:
# Activa el entorno virtual para que uses sus paquetes
#
# INDICADOR:
# Verás (venv) al inicio de tu terminal cuando esté activado


# ============================================
# 3. INSTALAR PAQUETES
# ============================================

# COMANDO EN TERMINAL (Con el entorno ACTIVADO):
# pip install nombre_paquete
#
# EJEMPLOS:
# pip install numpy
# pip install pandas
# pip install requests
# pip install flask
#
# EXPLICACIÓN:
# Instala el paquete en tu entorno virtual, no en el sistema


# ============================================
# 4. INSTALAR MÚLTIPLES PAQUETES
# ============================================

# COMANDO EN TERMINAL:
# pip install numpy pandas requests flask
#
# EXPLICACIÓN:
# Instala varios paquetes de una vez separados por espacios


# ============================================
# 5. VER PAQUETES INSTALADOS
# ============================================

# COMANDO EN TERMINAL:
# pip list
#
# EXPLICACIÓN:
# Muestra todos los paquetes instalados en tu entorno virtual
# con sus versiones


# ============================================
# 6. VER INFORMACIÓN DE UN PAQUETE ESPECÍFICO
# ============================================

# COMANDO EN TERMINAL:
# pip show numpy
#
# EXPLICACIÓN:
# Muestra detalles del paquete: versión, ubicación, dependencias, etc.


# ============================================
# 7. ACTUALIZAR UN PAQUETE
# ============================================

# COMANDO EN TERMINAL:
# pip install --upgrade nombre_paquete
#
# FORMA CORTA:
# pip install -U nombre_paquete
#
# EJEMPLO:
# pip install --upgrade numpy
#
# EXPLICACIÓN:
# Actualiza el paquete a su versión más reciente


# ============================================
# 8. DESINSTALAR UN PAQUETE
# ============================================

# COMANDO EN TERMINAL:
# pip uninstall nombre_paquete
#
# EJEMPLO:
# pip uninstall numpy
#
# EXPLICACIÓN:
# Elimina el paquete del entorno virtual


# ============================================
# 9. CREAR ARCHIVO requirements.txt
# ============================================

# COMANDO EN TERMINAL:
# pip freeze > requirements.txt
#
# EXPLICACIÓN:
# Crea un archivo que lista todos los paquetes instalados con sus versiones
# Ideal para compartir tu proyecto en GitHub
#
# CONTENIDO TÍPICO DE requirements.txt:
# numpy==1.24.3
# pandas==2.0.2
# requests==2.31.0
# flask==2.3.2


# ============================================
# 10. INSTALAR DEPENDENCIAS DESDE requirements.txt
# ============================================

# COMANDO EN TERMINAL:
# pip install -r requirements.txt
#
# EXPLICACIÓN:
# Instala todos los paquetes listados en requirements.txt
# Útil cuando alguien clona tu proyecto desde GitHub


# ============================================
# 11. DESACTIVAR EL ENTORNO VIRTUAL
# ============================================

# COMANDO EN TERMINAL:
# deactivate
#
# EXPLICACIÓN:
# Desactiva el entorno virtual y vuelves a usar el Python del sistema
# El (venv) desaparece de tu terminal


# ============================================
# 12. BUSCAR UN PAQUETE EN PyPI
# ============================================

# COMANDO EN TERMINAL:
# pip search nombre_paquete
#
# NOTA: Este comando ya no funciona. Mejor usa:
# https://pypi.org/ (desde el navegador)
#
# EXPLICACIÓN:
# Busca información sobre paquetes disponibles


# ============================================
# 13. INSTALAR VERSIÓN ESPECÍFICA DE UN PAQUETE
# ============================================

# COMANDO EN TERMINAL:
# pip install numpy==1.24.3
#
# EXPLICACIÓN:
# Instala una versión exacta del paquete
# El == especifica la versión exacta


# ============================================
# 14. INSTALAR CON RANGO DE VERSIONES
# ============================================

# COMANDO EN TERMINAL:
# pip install "numpy>=1.20,<2.0"
#
# EXPLICACIÓN:
# >= Mayor o igual que
# < Menor que
# Instala cualquier versión entre 1.20 y 2.0


# ============================================
# 15. ELIMINAR TODO EL ENTORNO VIRTUAL
# ============================================

# COMANDO EN TERMINAL:
# rm -r venv  (Linux/Mac)
# rmdir /s venv  (Windows)
#
# EXPLICACIÓN:
# Elimina toda la carpeta del entorno virtual
# Útil si quieres empezar de cero


# ============================================
# RESUMEN DE FLUJO DE TRABAJO
# ============================================

# 1. Crear proyecto
# 2. cd tu-proyecto
# 3. python3 -m venv venv
# 4. source venv/bin/activate
# 5. pip install nombre_paquete
# 6. Escribir código
# 7. pip freeze > requirements.txt
# 8. Subir a GitHub
# 9. deactivate (cuando termines)

# ============================================
# ESTRUCTURA DE CARPETAS RECOMENDADA
# ============================================

# mi-proyecto/
# │
# ├── venv/                  # Entorno virtual (NO subir a GitHub)
# ├── main.py               # Archivo principal
# ├── requirements.txt      # Dependencias (SÍ subir a GitHub)
# ├── README.md             # Descripción del proyecto
# └── .gitignore            # Incluir "venv/" para no subirlo

# ============================================
# ARCHIVO .gitignore RECOMENDADO
# ============================================

# venv/
# __pycache__/
# *.pyc
# .DS_Store
# .vscode/
# *.egg-info/
# dist/
# build/