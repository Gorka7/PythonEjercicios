# Clase en vídeo: https://youtu.be/TbcEqkabAWU

#Dates

#Date time

#from datetime import timedelta
#from datetime import date
#from datetime import time
from datetime import datetime

ahora = datetime.now()


print(ahora.year)
print(ahora.month)
print(ahora.day)
print(ahora.hour)
print(ahora.minute)
print(ahora.second)

timestamp = ahora.timestamp()
print(timestamp)



year_2023 = datetime(2023, 1, 1)

#Prueba

