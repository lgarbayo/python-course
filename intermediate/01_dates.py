# Importar modulo datetime y timedelta para trabajar con horas y fechas en Python
from datetime import datetime, timedelta

# para formatear idioma:
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

# Obtener la fecha y hora actual
now = datetime.now()
print(f"Fecha y hora actual: {now}") # recordemos que f-string nos permite incluir expresiones de python

# Crear una fecha y hora específica
specific_date = datetime(2025, 2, 12, 15, 30, 0) # año, mes, dia, horas, minutos, segundos, ms
print(f"Fecha y hora específica: {specific_date}")

# Formatear fechas: método strftime(), pasarle el objeto datetime y el formato especificado

format_date = now.strftime("%A %B %Y %H:%M:%S %d/%m") # ver documentacion de python: https://docs.python.org/3/library/datetime.html#format-codes
print(f"Fecha formateada: {format_date}")

# Operaciones con fechas (sumar/restar dias, minutos, horas, meses)
yesterday = datetime.now() - timedelta(days=1)
print(f"Ayer: {yesterday}")

tomorrow = datetime.now() + timedelta(days=0.5) # SE PUEDE HASTA PASAR MEDIO DÍA!
print(f"Mañana: {tomorrow}")

one_hour_after = datetime.now() + timedelta(hours=1)
print(f"Una hora después: {one_hour_after}")

# Obtener componentes individuales de una fecha
year = now.year
print(year)

month = now.month
print(month)

# Calcular la diferencia entre 2 fechas
date1 = datetime.now()
date2 = datetime(2025, 2, 12, 15, 30, 0)
difference = date2 - date1
print(f"Diferencia entre las fechas: {difference}")