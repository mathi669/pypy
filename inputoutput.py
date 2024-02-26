import subprocess
import pexpect

def elimination_monitoring_points(self, armor_p, armor_r):
    # Tu código existente...

    # Obtener la dirección IP del host de la solicitud
    host_ip = armor_p.json_body["host_ip"] if "host_ip" in armor_p.json_body else None
    
    if host_ip is None:
        # Manejar el caso en que no se proporciona la dirección IP del host
        sal.update({"02RESP": "ERROR"})
        sal.update({"03LOG": "Host IP is required"})
        return sal

    # Construir el comando para ejecutar el script Nagios
    command_exec_elimination_point = "./u01/home/app/nagios/admin/ServicesRemover/ServiceRemover_V2.py"

    try:
        # Iniciar el proceso y esperar la entrada
        process = pexpect.spawn(command_exec_elimination_point)
        process.expect("Ingrese la IP del dispositivo:")
        process.sendline(host_ip)
        process.expect("¿Es este el archivo correcto? (s/n)")
        process.sendline("s")

        # Continuar enviando respuestas según sea necesario...
        # Aquí puedes agregar más líneas de código para enviar respuestas adicionales
        # dependiendo de las preguntas que haga el script Nagios

        # Capturar la salida del script Nagios
        output = process.read().decode("utf-8")

        # Manejar la salida y actualizar la respuesta
        # (este código puede variar dependiendo de cómo se estructura la salida del script Nagios)
        if "NAGIOS HOST REMOVED" in output:
            sal.update({"01INFO": "NAGIOS HOST REMOVED"})
            sal.update({"02RESP": "OK"})
            sal.update({"03LOG": output})
        else:
            sal.update({"01INFO": "ERROR TO CONNECT"})
            sal.update({"02RESP": "ERROR"})
            sal.update({"03LOG": output})

        logger.info(sal)
        return sal

    except pexpect.exceptions.EOF:
        # Manejar cualquier error que ocurra durante la ejecución del proceso
        sal.update({"02RESP": "ERROR"})
        sal.update({"03LOG": "Error executing the Nagios script"})
        logger.error("Error executing the Nagios script")
        return sal
