from datetime import datetime

# Fecha original en formato string
fecha_original_str = "12/6/2023 6:00 PM"

# Convertir la fecha string a un objeto datetime
fecha_original = datetime.strptime(fecha_original_str, "%m/%d/%Y %I:%M %p")

# Formatear la fecha en el nuevo formato
fecha_formateada = fecha_original.strftime("%Y;%m;%d;%H;%M")

print(fecha_formateada)