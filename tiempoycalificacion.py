#declarar las variables
minutos=0; segundos=0; horas=0;
nombre=0; curso=0; parcial1=0; parcial2=0; parcial3=0;
promedio_parciales=0; examen_final=0; trabajo_final=0; calificacion_final=0;

#realizar conversiones de tiempo y calcular calificaciones
# Mostrar el menú de opciones
print("***** MENU DE OPCIONES *****")
print("1. Convertir segundos a horas")
print("2. Convertir segundos a minutos")
print("3. Convertir segundos a horas, minutos y segundos")
print("4. Calcular calificación final del alumno")
print("5. Salir del programa")

# Solicitar la opción del usuario
opcion = int(input("Escoja una opción del menú: "))

# Opción 1: Conversión de segundos a horas
if opcion == 1:
    segundos = int(input("Ingrese la cantidad de segundos: "))
    horas = segundos/3600
    print("{} segundos equivalen a {} horas".format(segundos , horas))

# Opción 2: Conversión de segundos a minutos
elif opcion == 2:
    segundos = int(input("Ingrese la cantidad de segundos: "))
    minutos = segundos/60
    print("{} segundos equivalen a {} minutos".format(segundos , minutos))

# Opción 3: Conversión de segundos a horas, minutos y segundos
elif opcion == 3:
    segundos = int(input("Ingrese la cantidad de segundos: "))
    horas = segundos/3600
    segundos %= 3600
    minutos = segundos/60
    segundos %= 60
    print("Las conversiones serian: Horas: {}, Minutos: {}, Segundos: {}".format(horas , minutos , segundos))

# Opción 4: Cálculo de calificación final del alumno
elif opcion == 4:
    nombre=input("Ingrese el nombre del alumno: ")
    curso=input("Ingrese el curso del alumno: ")
    parcial1=int(input("Ingrese la primera calificación: "))
    parcial2=int(input("Ingrese la segunda calificación: "))
    parcial3=int(input("Ingrese la tercera calificación: "))

    promedio_parciales = parcial1+parcial2+parcial3/3
    examen_final = int(input("Ingrese la calificación del examen final: "))
    trabajo_final = int(input("Ingrese la calificación del trabajo final: "))

    calificacion_final = (promedio_parciales * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)

    print("***** RESULTADOS *****")
    print("Alumno: " , nombre)
    print("Curso: " , curso)
    print("Calificación final: " , calificacion_final)

# Opción 5: Salir del programa
elif opcion == 5:
    print("Fin del programa")

# Validación en caso de que el usuario ingrese una opción inválida
else:
    print("Opción no válida, por favor seleccione una opción correcta.")
