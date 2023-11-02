import subprocess

# Nombre del servicio SNMP en Windows 10
nombre_servicio = "SNMP"

def verificar_servicio():
    try:
        resultado = subprocess.check_output(["sc", "query", nombre_servicio], text=True)
        if "RUNNING" in resultado:
            print(f"El servicio {nombre_servicio} está en funcionamiento.")
            return True
        else:
            print(f"El servicio {nombre_servicio} no está en funcionamiento.")
            return False
    except subprocess.CalledProcessError:
        print(f"Error al verificar el estado del servicio {nombre_servicio}.")
        return False

def reiniciar_servicio():
    try:
        subprocess.run(["sc", "stop", nombre_servicio], check=True)
        subprocess.run(["sc", "start", nombre_servicio], check=True)
        print(f"El servicio {nombre_servicio} ha sido reiniciado con éxito.")
    except subprocess.CalledProcessError:
        print(f"Error al reiniciar el servicio {nombre_servicio}.")

if verificar_servicio():
    # Si el servicio está en funcionamiento, reiniciar
    reiniciar_servicio()
else:
    # Si el servicio no está en funcionamiento, iniciarlo y luego reiniciar
    subprocess.run(["sc", "start", nombre_servicio], check=True)
    reiniciar_servicio()
