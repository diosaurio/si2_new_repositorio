# connect to the database, read the first 1000 entries
# then perform 1000 queries retrieving each one of the entries
# one by one. Measure the time requiered for the 1000 queries


# Configurar Django
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "visaSite.settings")
django.setup()
import psycopg2
import time
from visaAppRPCBackend.models import Tarjeta

try:
    # Conexion a la base de datos
    tarjetas = Tarjeta.objects.all()[:1000]

    # Medir el tiempo de inicio
    start_time = time.time()

    # Realizar busquedas una a una
    for tarjeta in tarjetas:
        id_value = tarjeta.numero  # Suponiendo que la primera columna es el ID
        tarjeta_encontrada = Tarjeta.objects.get(pk=id_value)

    # Medir el tiempo de finalizacion
    end_time = time.time()

    # Mostrar los resultados
    print(f"Tiempo invertido en buscar las 1000 entradas una a una: {end_time - start_time:.6f} segundos")

except Exception as e:
    print(f"Error: {e}")

