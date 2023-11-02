#loop for: cumple para iterar una lista de elementos
#ej: listado de usuarios (nombre y apellido) si el campo no se encuentra dentro de los usuarios, el ciclo for se encargará de crear de manera
#virtual este campo, otro uso, buscar elementos, operaciones matematicas, etc..

#funcion range: crea una secuencia de numeros que se utiliza dentro del ciclo for (0,1,2,3,4)

#la variable numero: tomará el valor de cada elemento dentro del range

for numero in range(5):
    print(numero, numero * 'Hola mundo')

#for else
buscar = 10

for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print(" No encontre el numero buscado :( ")

# for usurario in usuarios:
#     usurario.id

for char in "Ultimate python":
    print(char)