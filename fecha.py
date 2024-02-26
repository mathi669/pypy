import datetime

def obtener_fecha_archivo(linea):
    partes = linea.split(';')
    return datetime.date(int(partes[1]), int(partes[2]), int(partes[3]))

def restar_un_dia(fecha):
    un_dia = datetime.timedelta(days=1)
    return fecha - un_dia

entrada = 'ham_in.txt'
fecha_limite = datetime.date(2024, 3, 1)
fecha_actual = datetime.date.today()

if fecha_actual < fecha_limite:
    with open(entrada, 'r') as archivo:
        linea = archivo.readline().strip()

    fecha_archivo = obtener_fecha_archivo(linea)
    nueva_fecha = restar_un_dia(fecha_archivo)

    partes = linea.split(';')
    partes[1:4] = [str(nueva_fecha.year), str(nueva_fecha.month).zfill(2), str(nueva_fecha.day).zfill(2)]
    nueva_linea = ';'.join(partes)

    with open(entrada, 'w') as archivo:
        archivo.write(nueva_linea + '\n')