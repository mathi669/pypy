import logging
from datetime import datetime
import pytz

# Logging
logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def nagios_maintenance_v1(self, armor_p, armor_r):
    # Defines Service Output
    sal = {"01INFO": "NAGIOS CONNECT SERVER",
           "02RESP": "",
           "03LOG": ""}

    # Instanciate Class
    svh = self.ssh_utils()
    svh.ssh_sep = "\r\n"

    # Validate ldap auth
    aut = svh.auth(armor_r.headers, "nagios")
    if not aut["user_auth"] and not aut["david_auth"]:
        sal.update({"02RESP": "ERROR"})
        sal.update({"03LOG": "authentication failed"})
        return sal

    # # validate group membership
    if not aut["group_member"]:
        sal.update({"02RESP": "ERROR"})
        sal.update({"03LOG": "Not authorized for this task"})
        return sal

    required_fields = ["server", "host", "date", "duration", "comment"]
    for field in required_fields:
        if field not in armor_p.json_body.keys():
            sal.update({"02RESP": "ERROR"})
            sal.update({"03LOG": f"Missing required field: {field}"})
            return sal
        elif armor_p.json_body[field] is None or armor_p.json_body[field] == "":
            sal.update({"02RESP": "ERROR"})
            sal.update(
                {"03LOG": f"""Empty required field: {armor_p.json_body[field]}"""})
            return sal

    # Get Parameters
    svh.route = armor_p.json_body["route"] if "route" in armor_p.json_body else ""
    svh.server = armor_p.json_body["server"]
    host_name = armor_p.json_body["host"]
    date_maintenance = armor_p.json_body["date"]
    duration = armor_p.json_body["duration"]
    comment = armor_p.json_body["comment"]
    showstderr = armor_p.json_body["showmessages"].upper(
    ) if "showmessages" in armor_p.json_body else "SI"
    OUT_TYPE = armor_p.json_body["out_type"] if "out_type" in armor_p.json_body else "json"

    if int(duration) > 100:
        sal.update({"02RESP": "ERROR"})
        sal.update(
            {"03LOG": "El tiempo de duracion no debe pasar las 100 horas"})
        return sal

    date_to_str = date_maintenance

    if 'AM' in date_to_str.upper() or 'PM' in date_to_str.upper():
        date_format = "%m/%d/%Y %I:%M %p"
    else:
        # If not, assume 24-hour format
        date_format = "%m/%d/%Y %H:%M"

    transform_date = datetime.strptime(date_to_str, date_format)

    server_timezone = "Chile/Continental"

    server_tz = pytz.timezone(server_timezone)

    transform_date = server_tz.localize(transform_date)

    current_time = datetime.now(server_tz)

    date_format = transform_date.strftime("%Y;%m;%d;%H;%M")

    if transform_date <= current_time:
        sal.update({"02RESP": "ERROR"})
        sal.update({"03LOG": "El tiempo de inicio debe ser en el futuro"})
        return sal

    user = aut['user']
    logger.debug(user)
    # add user to comments
    comment_with_user = f'{comment} (User:{aut["user"]})'

    user_input = host_name + ";" + date_format + \
        ";" + duration + ";" + comment_with_user + ";"

    # Open Server Conection
    if svh.ssh_open() == "error":
        sal.update({"02RESP": "ERROR"})
        sal.update({"03LOG": svh.ssh_err_con})
        logger.info(sal)
        return sal

    # Rescatar usuario desde template
    svh.ssh_service_account = "root"

    input_validate = f"echo '{host_name}' > /u01/home/app/nagios/admin/DeviceValidator/entrada.txt"

    if showstderr == "NO":
        input_validate += " 2>/dev/null"

    # Execute command
    logger.debug(input_validate)
    ret = svh.ssh_cmd_exec(input_validate)
    logger.debug(ret)

    logger.debug('Datos cargados al archivo entrada.txt')

    # ####### Ejecucion script para realizar validacion #######
    command_validate = "python /u01/home/app/nagios/admin/DeviceValidator/DeviceValidator.py"
    # Execute command
    logger.debug(command_validate)
    ret = svh.ssh_cmd_exec(command_validate)
    logger.debug(ret)

    if 'stdout' in ret and "No se encontraron coincidencias" in ret["stdout"][0]:
        error_message = f"Error: Host '{host_name}' no encontrado"
        sal.update({"02RESP": "ERROR"})
        sal.update({"03LOG": error_message})
        return sal

    # logger.debug(svh.get_out_type(ret["stdout"], "text"))
    # logger.debug(str(len(ret["stdout"])))
    if 'stdout' in ret and len(ret["stdout"]) > 1:
        # logger.debug("entrando a if coincidencias multiples")
        opciones_coincidencias = f"Se han encontrado las siguientes coincidencias para el host: '{host_name}' " + svh.get_out_type(
            ret["stdout"], "text") + " Indique el nombre especifico."  # Las opciones son las líneas restantes en stdout
        sal.update({"02RESP": "MULTIPLE_COINCIDENCIA"})
        sal.update({"03LOG": opciones_coincidencias})
        return sal

    command_to_maintenance = f"echo '{user_input}' > /u01/home/app/nagios/admin/ham_in.txt"

    if showstderr == "NO":
        command_to_maintenance += " 2>/dev/null"

    # Execute command
    logger.debug(command_to_maintenance)
    ret = svh.ssh_cmd_exec(command_to_maintenance)
    logger.debug(ret)

    logger.debug('Datos cargados al archivo ham_in.txt')

    ###### Ejecucion script para realizar mantencion #######
    command_exec = "/u01/home/app/nagios/admin/ham_solo_V3.pl -M ham_in.txt"
    # Execute command
    logger.debug(command_exec)
    ret = svh.ssh_cmd_exec(command_exec)
    logger.debug(ret)

    # if rest of case
    if ret["exit_code"] == "0":
        sal.update({"01INFO": "NAGIOS IN MAINTENANCE"})
        sal.update({"02RESP": "OK"})
        sal.update({"03LOG": svh.get_out_type(ret["stdout"], "text")})
    else:
        sal.update({"01INFO": "ERROR TO CONNECT"})
        sal.update({"02RESP": "ERROR"})
        sal.update({"03LOG": svh.get_out_type(ret["ERROR"], "text")})

    logger.info(sal)
    return sal
