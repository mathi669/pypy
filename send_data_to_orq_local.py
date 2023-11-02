#!/usr/bin/env python

import argparse
import subprocess

dir = None
host = None

o_host_pe = None
o_host_272 = None

##### OPTIONS ####

def print_usage():
    print "Usage: {0} -P [<orquestador local PE>] | -p [<orquestador local 272>]".format(__file__)
    print "Example: ./change_name_host.py -P or -p"

def help():
    print "\nScript para enviar la carpeta objects_PE o objects_272 al orquestador correspondiente."
    print "(c)2016 dParadig"
    print "e-mail: administradoresmonitoreo@dparadig.com\n"
    print_usage()
    print "-P, --ORQ-PE\n-p, --ORQ-272"

def check_options():
    global o_host_pe, o_host_272

    parser = argparse.ArgumentParser(description="Script to send objects_PE or objects_272 folder to the corresponding orchestrator.")
    parser.add_argument('-P', '--ORQ-PE', action='store_true', help='Orquestador local PE')
    parser.add_argument('-p', '--ORQ-272', action='store_true', help='Orquestador local 272')

    args = parser.parse_args()

    o_host_pe = args.ORQ_PE
    o_host_272 = args.ORQ_272

    ##### CHECK SCRIPT INVOCATION ##################

    if not o_host_pe and not o_host_272:
        help()  # Imprimir la ayuda cuando no se proporcionan opciones
        exit()

##################################### MAIN-ROUTINE #################################################

def envio_data():
    global dir, host
    cmd = subprocess.call(["tar", "-czf", "/u01/home/app/nagios/etc/homologation_{0}.tar.gz".format(dir), "--directory='/u01/home/app/nagios/etc/'", "./{0}/".format(dir)])
    print "###         Enviando archivos del directorio {0}         ###".format(dir)
    cmd = subprocess.call(["scp", "-r", "/u01/home/app/nagios/etc/homologation_{0}.tar.gz".format(dir), "{0}:/u01/home/app/nagios/admin/homologation2019".format(host)])

    cmd = subprocess.call(["ssh", host, "-o", "ServerAliveInterval=30", 'rm -rf /u01/home/app/nagios/etc/objects/ /u01/home/app/nagios/etc/cgi.cfg /u01/home/app/nagios/etc/htpasswd.users;tar -xzpf /u01/home/app/nagios/admin/homologation2019/homologation_{}.tar.gz --directory=\'/u01/home/app/nagios/admin/homologation2019/\';  mv /u01/home/app/nagios/admin/homologation2019/{}/cgi.cfg /u01/home/app/nagios/etc/ ; mv /u01/home/app/nagios/admin/homologation2019/{}/htpasswd.users /u01/home/app/nagios/etc/ ; mv /u01/home/app/nagios/admin/homologation2019/{}/objects /u01/home/app/nagios/etc/objects; rm -rf /u01/home/app/nagios/admin/homologation2019/*'.format(dir, dir, dir, dir)])
    cmd = subprocess.call(["ssh", host, "-o", "ServerAliveInterval=30", 'execas nagios configtest'])

    if "Total Errors:   0" in cmd:
        print("### No se han encontrado Errores, Procediendo a recargar nagios ###")
        cmd = subprocess.call(["ssh", host, 'execas nagios reload'])
        cmd = cmd.replace('\r\n', '')
        print "###  {0}  ###".format(cmd)
        print "###                                                             ###"
        print "###################################################################\n"
    else:
        print "###           Revisar errores indicados en configtest           ###"
        print cmd
        print "###                                                             ###"
        print "###################################################################\n"

    cmd = subprocess.call(["rm", "-f", "/u01/home/app/nagios/etc/homologation_{0}.tar.gz".format(dir)])

##################################### MAIN #################################################

check_options()

if o_host_pe:
    print "\n###################################################################"
    print "###                                                             ###"
    print "###       Bienvenidos al centralizador de archivos nagios       ###"
    print "###                                                             ###"
    print "###               Escojiste opción orquestador PE               ###"
    host = "nagios@172.22.175.114"
    dir = "PE_objects"
    envio_data()
if o_host_272:
    print "\n###################################################################"
    print "###                                                             ###"
    print "###       Bienvenidos al centralizador de archivos nagios       ###"
    print "###                                                             ###"
    print "###               Escojiste opción orquestador 272              ###"
    host = "nagios@10.1.34.62"
    dir = "272_objects"
    envio_data()
