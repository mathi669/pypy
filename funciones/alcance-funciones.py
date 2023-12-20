saludo = "Hola global" #alcance global

def saludar():
    saludo = "Hola mundo" #alcance en la funcion saludar
    print(saludo)

def saludoChanchito():
    saludo = "Hola chanchito" # alcance en la funcion saludoChanchito
    print(saludo)

saludar()
