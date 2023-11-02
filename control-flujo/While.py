#Lo que hace, es evaluar la variable con el valor de la der, si la evaluacion es verdadera se ejecuta la iteracion
#ej: si numero es menor que 100, este ejecutará dando numero hasta que llegue el punto de pasar el 100

numero = 1

while numero < 100:
    print(numero)
    numero *= 2


while comando != "salir":
    comando = input("$ ")
    print(comando)

#loop infinito, si cuando no tenemos una condicion de salida dentro de un loop. este se ejecutará infinitamente