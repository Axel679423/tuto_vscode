#Fechas

from datetime import datetime

fecha = datetime(2024, 3, 16, 4, 3, 34)

print(fecha.second)

now = datetime.now()

print(now)

print(now.minute)

from datetime import time

miTiempo = time(3, 45)

print(miTiempo.minute)

from datetime import date

miDia = date.today()

print(miDia.day)

nuevoAño = datetime(2025, 4, 5)

print(nuevoAño - now)