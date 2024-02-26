# Add User

El script nagiosmaintenancemvp.py esta diseñado como un mvp en un escenario en particular a modo de pruebas para obtener feedback para la V1 del mismo.

# Despliegue

.- Entorno: Este script es compatible con una versión de Python 2.x
.- Configuración: Los directorios necesarios para el funcionamiento del script deben existir y ser accesibles para que el script funcione correctamente.

# Funciones

.- Verificación de Usuario Existente: Antes de crear un usuario, el script verifica si ya existe en el archivo correspondiente.
.- Creación de Usuario: Si el usuario no existe, se procede a su creación y a la modificación de los archivos de configuración pertinentes.
.- Sincronización y Reinicio de Servicios: Después de la creación y configuración del usuario, se ejecutan scripts para sincronizar cambios y reiniciar servicios, asegurando que los cambios tengan efecto.
.- Gestión de Errores: El script maneja errores básicos, como problemas al leer archivos o ejecutar comandos.

# Uso

El usuario se debe posicionar en el directorio del script, esto es, dentro de `/u01/home/app/nagios/admin/AddUser`.  

Se ejecuta desde la línea de comandos. Al iniciar, el script pide al usuario que elija una ubicación (Paises, Corporativo, Peru/Tiendas) para crear un nuevo usuario. El usuario debe ingresar el nombre del nuevo usuario y su contraseña.

## Funcionamiento interno

El funcionamiento interno del script se puede describir de la siguiente manera:

.- Establecimiento de Directorios: Al inicio, el script define una serie de variables que representan los directorios en los que operará. Estos incluyen directorios para diferentes workers (países, corporativo, Perú), directorios para contactos y sincronización.

.- Verificación de Existencia de Usuario: Cuando se ejecuta una acción para una ubicación específica (países, corporativo, Perú), el primer paso es verificar si el usuario ya existe. 
Para cada ubicación, hay una función específica que abre el archivo htpasswd.users correspondiente y busca una coincidencia con el nombre de usuario proporcionado.
Si el usuario ya existe, el script notifica al usuario y detiene el proceso para esa ubicación.
.- Solicitud de Información del Usuario: El script solicita al usuario que ejecute el script para introducir el nombre del nuevo usuario a través de la función raw_input.
.- Creación de Usuario: Si el usuario no existe, el script procede a crearlo. Este proceso implica la ejecución de comandos específicos para cada ubicación que incluyen la adición del usuario a los archivos correspondientes y la configuración de permisos basicos de solo lectura.
.- Reinicio de Servicios y Sincronización: Para cada ubicación, después de agregar un usuario y modificar la configuración, el script ejecuta un proceso de sincronización y reinicio de servicios. Esto se hace para asegurar que los cambios realizados se apliquen efectivamente en el sistema.
.- Notificación al Usuario: Finalmente, el script informa al usuario sobre el resultado del proceso, ya sea un éxito o un fallo debido a varios motivos, como un error al leer un archivo o al ejecutar un comando.

# Pruebas

# Servidores en los que el script ha sido desplegado
- f1cloud2019