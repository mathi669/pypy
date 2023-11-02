#!/usr/bin/perl -w

use Getopt::Long;
use strict;
use warnings;

my $o_help;
my $dir;
my $host;

my $o_host_pe;
my $o_host_272;
my $o_host_co;
my $o_host_ar;
my $o_host_bf;


##### OPTIONS ####

sub print_usage {
    print "Usage: $0 -A [<orquestador local ARG>]| -B [<orquestador local BF>] |-P [<orquestador local PE>]| -C [<orquestador local CO>]  \n Example: ./change_name_host.pl -A or -P or -C\n";
}
sub help {
   print "\nScript para enviar la carpeta objects_CO,ARG,BF o PE al orquestador correspondiente.\n";
   print "(c)2016 dParadig\n";
   print "e-mail: administradoresmonitoreo\@dparadig.com\n\n";
   print_usage();
   print <<EOT;
-h, --help
   print this help message
-A, --ORQ-ARG
-P, --ORQ-PE
-C, --ORQ-CO
-B, --ORQ-BF
-p, --ORQ-272
EOT
}

sub check_options {
    Getopt::Long::Configure ("bundling");
        GetOptions(
        'h'     => \$o_help,          'help'          => \$o_help,
        'A'     => \$o_host_ar,        'host_ar'        => \$o_host_ar,
        'C'     => \$o_host_co,        'host_co'        => \$o_host_co,
        'P'     => \$o_host_pe,        'host_pe'        => \$o_host_pe,
        'p'     => \$o_host_272,        'host_272'        => \$o_host_272,
	'B'     => \$o_host_bf,        'host_bf'        => \$o_host_bf,
        );
        ##### CHECK SCRIPT INVOCATION ##################

        if (defined ($o_help) ) { help(); exit};
        if (!defined ($o_host_ar) &&  !defined($o_host_272) && !defined($o_host_pe) && !defined($o_host_co) && !defined($o_host_bf) ) { print "ingrese opcion del orquestador a cargar sus archivos\n"; exit};
}

##################################### MAIN-ROUTINE #################################################

sub envio_data(){
	my $cmd = `tar -czf /u01/home/app/nagios/etc/homologation_$dir.tar.gz --directory='/u01/home/app/nagios/etc/' ./$dir/`;
	print "###         Enviando archivos del directorio $dir         ###\n";
	$cmd = `scp -r /u01/home/app/nagios/etc/homologation_$dir.tar.gz $host:/u01/home/app/nagios/admin/homologation2019`;

	$cmd = `ssh $host -o ServerAliveInterval=30 'rm -rf /u01/home/app/nagios/etc/objects/ /u01/home/app/nagios/etc/cgi.cfg /u01/home/app/nagios/etc/htpasswd.users;tar -xzpf /u01/home/app/nagios/admin/homologation2019/homologation_$dir.tar.gz --directory='/u01/home/app/nagios/admin/homologation2019/';  mv /u01/home/app/nagios/admin/homologation2019/$dir/cgi.cfg /u01/home/app/nagios/etc/ ; mv /u01/home/app/nagios/admin/homologation2019/$dir/htpasswd.users /u01/home/app/nagios/etc/ ; mv /u01/home/app/nagios/admin/homologation2019/$dir/objects /u01/home/app/nagios/etc/objects; rm -rf /u01/home/app/nagios/admin/homologation2019/*'`;
	if(defined($o_host_272)){
		$cmd = `ssh $host -o ServerAliveInterval=30 'execas nagios configtest'`;
	}else{
		$cmd = `ssh $host -o ServerAliveInterval=30 'sudo service nagios configtest'`;
	}

if($cmd =~ "Total Errors:   0"){
        print "### No se han encontrado Errores, Procediendo a recargar nagios ###\n";
	if(defined($o_host_272)){
		$cmd=`ssh $host 'execas nagios reload'`;
	}else{
        	$cmd=`ssh $host 'sudo service nagios reload'`;
	}
	$cmd =~ s/\r\n//;
        print "###  $cmd  ###\n";
	print "###                                                             ###\n";
	print "###################################################################\n\n";
}else{
        print "###           Revisar errores indicados en configtest           ###\n";
        print $cmd;
	print "###                                                             ###\n";
	print "###################################################################\n\n";
}

$cmd = `rm -f /u01/home/app/nagios/etc/homologation_$dir.tar.gz`;
}

##################################### MAIN #################################################


check_options();

#if(defined($o_host_ar)){
##        print "\n###################################################################\n";
##        print "###                                                             ###\n";
##        print "###       Bienvenidos al centralizador de archivos nagios       ###\n";
##        print "###                                                             ###\n";
##        print "###               Escojiste opcion orquestador AR               ###\n";
##        $host="nagios\@68.183.101.105";
##        $dir = "objects_AR";
##	  envio_data();
##}
##if(defined($o_host_co)){
##        print "\n###################################################################\n";
##        print "###                                                             ###\n";
##        print "###       Bienvenidos al centralizador de archivos nagios       ###\n";
##        print "###                                                             ###\n";
##        print "###               Escojiste opcion orquestador CO               ###\n";
##        $host="nagios\@68.183.101.105";
##        $dir = "objects_CO";
##        envio_data();
##}
if(defined($o_host_pe)){
        print "\n###################################################################\n";
        print "###                                                             ###\n";
        print "###       Bienvenidos al centralizador de archivos nagios       ###\n";
        print "###                                                             ###\n";
        print "###                Escojiste opcion orquestador PE              ###\n";
        $host="nagios\@172.22.175.114";
        $dir = "PE_objects";
        envio_data();
}

if(defined($o_host_272)){
        print "\n###################################################################\n";
        print "###                                                             ###\n";
        print "###       Bienvenidos al centralizador de archivos nagios       ###\n";
        print "###                                                             ###\n";
        print "###                Escojiste opcion orquestador PE              ###\n";
        $host="nagios\@10.1.34.62";
        $dir = "272_objects";
        envio_data();
}


if(defined($o_host_bf)){
        print "\n###################################################################\n";
        print "###                                                             ###\n";
        print "###       Bienvenidos al centralizador de archivos nagios       ###\n";
        print "###                                                             ###\n";
        print "###                Escojiste opcion orquestador BF              ###\n";
        $host="nagios\@172.20.242.227";
        $dir = "BF_objects";
        envio_data();
}

