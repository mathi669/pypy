#kwargs: una forma de empaquetar parametros, en solo un parametro, a diferencia de los xargs
#en vez de pasar un *, con los kwargs son 2 **
def get_product(**datos):
    print(datos["id"], datos["name"]) #-- para mostrar parametros especificos se utiliza [] para acceder a los parametros que se quieran mostrar

#Cuando en una funcion se trabaja con kwargs, hay que indicar el nombre del parametro
#ej: para "id" hay que anteponer el nombre, id="id"
get_product(id="id", name="iphone", desc="esto es un iphone")
