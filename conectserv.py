import paramiko

hostname = "192.168.1.133"
port = 22
username = 'mati'
password = 'matia$"6'

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(hostname, port, username, password)
    
    stdin, stdout, stderr = ssh.exec_command('Get-Service -Name SNMP')

    print(stdout.read().decode())
except Exception as e:
    print(f"Error al conectar al servidor: {e}")

finally:
    ssh.close()