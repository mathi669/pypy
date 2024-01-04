from datetime import datetime
import re

class TuClase:
    def ssh_nagios(self, armor_p, armor_r):
        # ... (código existente)

        # Validaciones
        required_fields = ["server", "host", "date", "duration", "comment", "showmessages", "out_type"]
        for field in required_fields:
            if field not in armor_p.json_body:
                sal.update({"02RESP": "ERROR"})
                sal.update({"03LOG": f"Missing required field: {field}"})
                return sal

        # Validar formato del servidor
        server_format = re.compile(r'@falabella\.(com|cl)$')
        if not server_format.match(svh.server):
            sal.update({"02RESP": "ERROR"})
            sal.update({"03LOG": "Invalid server format"})
            return sal

        # Validar si el host está siendo monitoreado por Nagios (debe adaptarse a tu lógica)
        if not self.host_monitored(armor_p.json_body["host"]):
            sal.update({"02RESP": "ERROR"})
            sal.update({"03LOG": "Host is not monitored by Nagios"})
            return sal

        # Validar que la duración no sea mayor a 100 horas
        if int(armor_p.json_body["duration"]) > 100:
            sal.update({"02RESP": "ERROR"})
            sal.update({"03LOG": "Duration cannot be greater than 100 hours"})
            return sal

        # Validar que la hora de inicio sea una hora futura
        now = datetime.now()
        start_time = datetime.strptime(armor_p.json_body["date"], "%m/%d/%Y %I:%M %p")
        if start_time <= now:
            sal.update({"02RESP": "ERROR"})
            sal.update({"03LOG": "Start time must be in the future"})
            return sal

        # Resto del código...
