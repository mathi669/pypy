# permite tomar decisiones en cuanto que camino tome el codigo dependiendo de los valores que se esten trabajando

edad = 15

# Para que los codigos o los resultados que se entreguen dentro de if - else 
# funcionen estos deben estar una tabulacion mas dentro del if
# para que sea ejecutado con exito
if edad > 54:
    print("Puede ver la pelicula ccon descuento")
elif edad > 17:
    print("Puede ver la pelicula")
else:
    print("Nope")

# la evaluacion es de arriba hacia abajo (muy importante el orden)

print("Listo")