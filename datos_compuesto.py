#Lista es un tipo de dato compuesto
#Los valores de la lista, pueden ser modificados
nombre_persona=["jose", "pereira", "juan", "carlos",25,7.4, "True"]
print(nombre_persona[2])
nombre_persona[2]="pedro"
print(nombre_persona[2])

#tuplas igual que las listas, almacenan valores, pero no pueden modificarse, sus valores son inmutables
frutas_tropicales =("mango", "naranja", "coco")
frutas_tropicales=("piña", "mango")
#frutas_tropicales[1]="piña"

print(frutas_tropicales)

#los conjuntos en python omite los valores que son duplicados 
apellidos={"juan","carlos","julio","juan"}
print (apellidos)

edades= {12,15,23,12}
print(edades)

#diccionarios en python otro tipo de datos compuesto

datos_personales={
    'nombre':"alice",
    'nombre_2':"nahomy",
    'apellido':"castellon",
    'edad':18,
    'persona':True
}

datos_personales['nombre']="alicee"
print(datos_personales["nombre"])
print(datos_personales["nombre_2"])
print(datos_personales['apellido'])