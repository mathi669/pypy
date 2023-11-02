import subprocess

verify = "systemctl is-active snmpd"
reestarsys = "systemctl restart snmpd"

def verify_service():
    try:
        result = subprocess.check_output(verify, shell=True, text=True)
        if result.strip() == "active":
            print("El servicio SNMP está en funcionamiento.")
            return True
        else:
            print("El servicio SNMP no está en funcionamiento.")
            return False
    except subprocess.CalledProcessError:
        print("Error al verificar el estado del servicio SNMP.")
        return False

def reestar_service():
    try:
        subprocess.run(reestarsys, shell=True, check=True)
        print("El servicio SNMP ha sido reiniciado con éxito.")
    except subprocess.CalledProcessError:
        print("Error al reiniciar el servicio SNMP.")

if verify_service():
    reestar_service()
else:
    subprocess.run("systemctl start snmp", shell=True)
    reestar_service()

