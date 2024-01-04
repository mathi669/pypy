import subprocess
import sys

def detener_servicio_snmp():
    comando_ps = 'Stop-Service -Name "SNMP"'
    try:
        subprocess.run(['powershell', '-Command', comando_ps], check=True)
        print("El servicio SNMP se detuvo correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al detener el servicio SNMP: {e}")
        print("Es posible que necesites ejecutar el script con privilegios de administrador.")

def iniciar_servicio_snmp():
    comando_ps = 'Start-Service -Name "SNMP"'
    try:
        subprocess.run(['powershell', '-Command', comando_ps], check=True)
        print("El servicio SNMP se inició correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"Error al iniciar el servicio SNMP: {e}")
        print("Es posible que necesites ejecutar el script con privilegios de administrador.")

def estado_servicio_snmp():
    comando_ps = 'Get-Service -Name "SNMP" | Select-Object Status'
    try:
        subprocess.run(['powershell', '-Command', comando_ps], check=True)
        print("Estado actual")
    except subprocess.CalledProcessError as e:
        print(f"Error al Comprobar estado: {e}")
        print("Es posible que necesites ejecutar el script con privilegios de administrador.")

def gestionar_servicio_snmp(accion):
    acciones_validas = ["detener", "iniciar", "estado", "reiniciar"]
    
    if accion not in acciones_validas:
        print("Acción no válida. Las acciones válidas son: detener, iniciar, estado, reiniciar")
        return
    
    if accion == "detener":
        detener_servicio_snmp()
    elif accion == "iniciar":
        iniciar_servicio_snmp()
    elif accion == "estado":
        estado_servicio_snmp()
    elif accion == "reiniciar":
        detener_servicio_snmp()
        iniciar_servicio_snmp()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <accion>")
        print("Acciones válidas: detener, iniciar, estado, reiniciar")
    else:
        accion = sys.argv[1].lower()
        gestionar_servicio_snmp(accion)
