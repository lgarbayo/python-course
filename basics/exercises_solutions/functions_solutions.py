# --- Solución Ejercicio 1: Calculadora de Área ---
def calculate_rectangle_area(width, height):
    """Calcula el área de un rectángulo a partir de su ancho y alto."""
    return width * height
# Prueba
area = calculate_rectangle_area(10, 5)
print(f"Ejercicio 1: El área es {area}")
# help(calculate_rectangle_area) # Para ver el docstring


# --- Solución Ejercicio 2: Saludo Personalizado ---
def create_greeting(name, greeting="Hello"):
    """Crea un saludo personalizado."""
    return f"{greeting}, {name}!"
# Prueba
print(f"Ejercicio 2: {create_greeting('Luis')}")


# --- Solución Ejercicio 3: Promedio de Calificaciones ---
def calculate_average(*args):
    """Calcula el promedio de una serie de números."""
    if not args:  # Si la tupla de argumentos está vacía
        return 0
    total = sum(args)
    return total / len(args)
# Prueba
print(f"Ejercicio 3: El promedio de (10, 8, 9) es {calculate_average(10, 8, 9)}")
print(f"Ejercicio 3: El promedio de () es {calculate_average()}")


# --- Solución Ejercicio 4: Constructor de Perfiles ---
def build_user_profile(**kwargs):
    """Muestra la información de un perfil de usuario."""
    print("Ejercicio 4: Perfil de usuario:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")
# Prueba
build_user_profile(name="William Dafoe", age=40, city="New York", status="Active")


# --- Solución Ejercicio 5: Validador de Contraseña ---
def is_password_valid(password: str) -> bool:
    """
    Verifica si una contraseña es segura.
    - Al menos 8 caracteres.
    - Al menos un número.
    """
    has_min_length = len(password) >= 8
    has_digit = any(char.isdigit() for char in password)
    return has_min_length and has_digit
# Prueba
print(f"Ejercicio 5: ¿'password123' es válida? {is_password_valid('password123')}")
print(f"Ejercicio 5: ¿'pass' es válida? {is_password_valid('pass')}")
print(f"Ejercicio 5: ¿'password' es válida? {is_password_valid('password')}")