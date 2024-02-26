from datetime import datetime
import pytz

class TuClase:
    # Resto de tu clase...

    def nagios_maintenance_v1(self, armor_p, armor_r):
        # Resto del código...

        # Get Parameters
        svh.route = armor_p.json_body["route"] if "route" in armor_p.json_body else ""
        svh.server = armor_p.json_body["server"]
        host_name = armor_p.json_body["host"]
        date_maintenance = armor_p.json_body["date"]
        duration = armor_p.json_body["duration"]
        comment = armor_p.json_body["comment"]
        showstderr = armor_p.json_body["showmessages"].upper() if "showmessages" in armor_p.json_body else "SI"
        OUT_TYPE = armor_p.json_body["out_type"] if "out_type" in armor_p.json_body else "json"

        if int(duration) > 100:
            sal.update({"02RESP": "ERROR"})
            sal.update({"03LOG": "El tiempo de duracion no debe pasar las 100 horas"})
            return sal

        date_to_str = date_maintenance

        if 'AM' in date_to_str.upper() or 'PM' in date_to_str.upper():
            date_format = "%m/%d/%Y %I:%M %p"
        else:
            # If not, assume 24-hour format
            date_format = "%m/%d/%Y %H:%M"

        transform_date = datetime.strptime(date_to_str, date_format)

        # Verifica si el año es bisiesto y ajusta la fecha si es necesario
        year = transform_date.year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            transform_date = transform_date.replace(year=year, day=min(transform_date.day, 29))

        server_timezone = "Chile/Continental"

        server_tz = pytz.timezone(server_timezone)

        transform_date = server_tz.localize(transform_date)

        current_time = datetime.now(server_tz)

        date_format = transform_date.strftime("%Y;%m;%d;%H;%M")

        if transform_date <= current_time:
            sal.update({"02RESP": "ERROR"})
            sal.update({"03LOG": "El tiempo de inicio debe ser en el futuro"})
            return sal

        # Resto del código...

        return sal
