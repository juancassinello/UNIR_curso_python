
def ingresar_calificaciones():

    # 1. Solicitar al usuario que ingrese el nombre de la materia
    materia = input("Ingrese el nombre de la materia: ")
    
    #2. Solicitar la calificación (validando que sea un número entre 0 y 10)
    calificacion = float(input("Ingrese la calificación (0-10): "))
    
    continuar = bool(input("¿Desea meter más asignaturas?"))
    if continuar == False:
        return
    

