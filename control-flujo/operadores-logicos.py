# and, or, not

gas = False
encendido = True
edad = 18

#ambos deben ser True para que pase la condicion
if not gas and (encendido or edad > 17):
    print("Puedes avanzar")
else:
    print("No puedes avanzar")

if gas or encendido:
    print("Puedes avanzar con or")

#Operadores de corto circuito ( si es que la condicion del lado izq da falso la condicion siguiente no se ejecutará)
if not gas and (encendido or edad > 17):
    print("Puedes avanzar")