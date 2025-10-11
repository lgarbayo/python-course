from datetime import datetime, timedelta
import locale

# Configurar el idioma a español para los nombres de días y meses
try:
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
except locale.Error:
    print("Locale 'es_ES.UTF-8' no soportado. Usando el locale por defecto.")


# --- Solución Ejercicio 1: Formato de Fecha Personalizado ---
print("--- Ejercicio 1 ---")
now = datetime.now()
# %A: Día de la semana completo, %d: día del mes, %B: mes completo, %Y: año, %H:%M: hora y minutos
formatted_string = now.strftime("Hoy es %A, %d de %B de %Y, y son las %H:%M.")
print(formatted_string)


# --- Solución Ejercicio 2: Calculadora de Fechas Futuras ---
print("\n--- Ejercicio 2 ---")
current_time = datetime.now()
future_date = current_time + timedelta(weeks=5, days=3, hours=10)
print(f"La fecha en el futuro será: {future_date.strftime('%d/%m/%Y a las %H:%M')}")


# --- Solución Ejercicio 3: Cuenta Atrás para Año Nuevo ---
print("\n--- Ejercicio 3 ---")
now = datetime.now()
next_year = now.year + 1
new_year_date = datetime(next_year, 1, 1, 0, 0, 0)
time_left = new_year_date - now
# .total_seconds() es útil, pero para un formato más legible, el objeto timedelta es directo.
print(f"Faltan para Año Nuevo: {time_left}")


# --- Solución Ejercicio 4: Convertir String a Fecha (Parsing) ---
print("\n--- Ejercicio 4 ---")
date_string = "25/12/2024"
# %d: día, %m: mes, %Y: año
parsed_date = datetime.strptime(date_string, "%d/%m/%Y")
# Usamos strftime para obtener el nombre del día de la semana
day_of_week = parsed_date.strftime("%A")
print(f"La fecha {date_string} fue un {day_of_week}.")


# --- Solución Ejercicio 5: ¿Es fin de semana? ---
print("\n--- Ejercicio 5 ---")
def is_weekend(date_obj: datetime) -> bool:
    """Devuelve True si la fecha es sábado (5) o domingo (6)."""
    # .weekday() -> Lunes=0, Martes=1, ..., Sábado=5, Domingo=6
    return date_obj.weekday() >= 5

# Prueba con hoy
today = datetime.now()
print(f"¿Hoy ({today.strftime('%A')}) es fin de semana? {is_weekend(today)}")

# Prueba con una fecha conocida (un sábado)
a_saturday = datetime(2025, 10, 11)
print(f"¿El {a_saturday.strftime('%d/%m/%Y')} ({a_saturday.strftime('%A')}) es fin de semana? {is_weekend(a_saturday)}")
