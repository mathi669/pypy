from datetime import datetime
from pytz import timezone
import pytz

def convert_to_server_timezone(date_str, server_timezone):
    # Convierte la cadena de fecha a un objeto datetime
    transform_date = datetime.strptime(date_str, "%m/%d/%Y %H:%M")

    # Obtén el objeto de la zona horaria del servidor
    server_tz = pytz.timezone(server_timezone)

    # Convierte el objeto datetime a la zona horaria del servidor
    transform_date = server_tz.localize(transform_date)

    current_time = datetime.now(server_tz)

    # Verifica si la fecha de inicio está en el futuro
    if transform_date <= current_time:
        return {"02RESP": "ERROR", "03LOG": "Start time must be in the future"}
    
    # Calcula la diferencia total de segundos
    time_difference_seconds = (transform_date - current_time).total_seconds()

    # Formatea la fecha en el formato deseado
    date_format = transform_date.strftime("%Y;%m;%d;%H;%M")

    return {"02RESP": "SUCCESS", "03LOG": date_format, "Time Difference (seconds)": time_difference_seconds}

# Ejemplo de uso
date_maintenance = "01/09/2024 16:40"
server_timezone = "America/New_York"

result = convert_to_server_timezone(date_maintenance, server_timezone)
print(result)

# Imprimir la fecha y hora actual para referencia
current_time = datetime.now(pytz.timezone(server_timezone))
print("Current Time:", current_time.strftime("%Y;%m;%d;%H;%M"))