
#! Trabajando con fechas y horas en Python

from datetime import datetime, timedelta
from os import system
import locale

if system("clear") != 0: system("cls")

#? 1. Obtener la fecha y hora actual
now = datetime.now()

print(f"Obtener Fecha y hora actual: {now}")

#? 2. Crear una fecha y hora específica
specific_date = datetime(2025, 2, 12, 15, 30, 0)
print(f"\nFecha y hora especificas: {specific_date}")

#? 3. Formatear fechas
#? método strftime() para formatear fechas
#? pasarle el objeto datetime y el formato especificado
#? formato:

locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

format_date = now.strftime("%A %B %Y %H:%M:%S")
print(f"\nFecha formateada: {format_date}")


#? 4. Operaciones con fechas (sumar/restar dias, minutos, horas, meses)
yesterday = datetime.now() - timedelta(days=1)
print(f"\nAyer: {yesterday}")

tomorrow = datetime.now() + timedelta(days=1)
print(f"\nMañana: {tomorrow}")

one_hour_after = datetime.now() + timedelta(hours=1)
print(f"\nUna hora despues: {one_hour_after}")


#? 5. Obtener componentes individuales de una fecha
year = now.year
print(f"\nYear: {year}")

month = now.month
print(f"\nMonth: {month}")

#? 6. Calcular la diferencia entre 2 fechas
date1 = datetime.now()
date2 = datetime(2025, 2, 12, 15, 30, 0)

difference = date2 - date1
print(f"\nDiferencia entre las fechas: {difference}")