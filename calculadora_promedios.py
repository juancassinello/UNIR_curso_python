
def ingresar_calificaciones():

    continuar = True
    ingresar_list_materias = []
    ingresar_list_calificaciones = []
    
    while continuar == True:
        
        # 1. Solicitar al usuario que ingrese el nombre de la materia
        # materia = input("Por favor, ingrese el nombre de la materia: ")
        ingresar_list_materias.append(input("Por favor, ingrese el nombre de la materia: "))
        
        #2. Solicitar la calificación (validando que sea un número entre 0 y 10)
        try:
            calificacion = float(input("Ingrese la calificación (0-10): "))
            
            while calificacion < 0 or calificacion > 10:
                print("Calificación inválida. Por favor, ingrese un número entre 0 y 10, con decimales.")
                calificacion = float(input("Ingrese la calificación (0-10): "))

            # añadimos la calificación a la lista.
            ingresar_list_calificaciones.append(calificacion)
            
            
            continuar = input("¿Desea meter más asignaturas? (y/n): ").lower().startswith('y')
            if continuar:
                return ingresar_list_materias, ingresar_list_calificaciones

        except TypeError:
            print("Error: Por favor, ingrese un número válido para la calificación.")
            

def determinar_estado(calificaciones, umbral = 5.0):
    # devuelva dos listas: una con los índices de las materias aprobadas y otra con los índices de las reprobadas.
    pass

def encontrar_extremos(calificaciones):    
    # identifique el índice de la calificación más alta y el índice de la más baja en la lista de calificaciones.
    pass


def main():
    list_materia, list_calificaciones = ingresar_list_calificaciones()
    