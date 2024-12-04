acceso = 0  #la "llave" de todo el sistema, hasta que este valor no sea 1, el vehiculo no podra ser arrancado

while acceso != 1:

    codigo = input("Introduzca el codigo de arranque: ")

    if codigo == '2701':  # Ese valor es la contraseña, la cual vendria predeterminada junto al programa

        acceso += 1  # Incrementar el valor de "acceso", lo cual permite que se arranque el vehiculo

    else: 
        
        print("El codigo es incorrecto, por favor, intentelo de nuevo")


print("Puede arrancar el vehiculo")