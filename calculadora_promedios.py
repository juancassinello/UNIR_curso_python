import math

def ingresar_calificaciones():

    continuar = True
    lista_usuario_materias = []
    lista_usuario_calificaciones = []
    
    while continuar == True:
        
        # 1. Solicitar al usuario que ingrese el nombre de la materia
        lista_usuario_materias.append(input("Por favor, ingrese el nombre de la materia: "))
        
        #2. Solicitar la calificación (validando que sea un número entre 0 y 10)
        try:
            calificacion = float(input("Ingrese la calificación (0-10): "))
            
            while calificacion < 0 or calificacion > 10:
                print("Calificación inválida. Por favor, ingrese un número entre 0 y 10, con decimales.")
                calificacion = float(input("Ingrese la calificación (0-10): "))

            # añadimos la calificación a la lista.
            lista_usuario_calificaciones.append(calificacion)
            
            
            continuar = input("¿Desea meter más asignaturas? (y/n): ").lower().startswith('y')
            if not continuar:
                return lista_usuario_materias, lista_usuario_calificaciones

        except ValueError:
            print("Error: Por favor, ingrese de nuevo la matería y un número válido para la calificación.")
            lista_usuario_materias.pop()

def calcular_promedio(lista_calificaciones):
    return round(math.fsum(lista_calificaciones) / len(lista_calificaciones), 2)

def determinar_estado(lista_calificaciones, umbral = 5.0):

    lista_materias_aprobadas_index = []
    lista_materias_reprobadas_index = []
    
    for index, l in enumerate(lista_calificaciones):
        
        if l >= umbral:
            lista_materias_aprobadas_index.append(index)
        else:
            lista_materias_reprobadas_index.append(index)

    return lista_materias_aprobadas_index, lista_materias_reprobadas_index

def encontrar_extremos(lista_calificaciones):    
    
    calificacion_alta_index = 0
    calificacion_baja_index = 0

    for index, l in enumerate(lista_calificaciones):

        if l > lista_calificaciones[calificacion_alta_index]:
            calificacion_alta_index = index
        
        if l < lista_calificaciones[calificacion_baja_index]:
            calificacion_baja_index = index

    return calificacion_alta_index, calificacion_baja_index

def main():

    # 1. obtenemos materia y calificaciones.
    lista_materias_total, lista_calificaciones_total = ingresar_calificaciones()

    # 2. Calcular Promedio.
    promedio = calcular_promedio(lista_calificaciones_total)

    # 3. determinar materias aprobadas/reprobadas
    lista_materias_aprobadas_index, lista_materias_reprobadas_index = determinar_estado(lista_calificaciones_total)
    lista_materias_aprobadas = []
    lista_materias_reprobadas = []
    
    for l1 in lista_materias_aprobadas_index:
        lista_materias_aprobadas.append(lista_materias_total[l1])

    for l2 in lista_materias_reprobadas_index:
        lista_materias_reprobadas.append(lista_materias_total[l2])


    # 4. encontrar las materias con calificaciones extremas.
    index_extremo_alto, index_extremo_bajo = encontrar_extremos(lista_calificaciones_total)

    '''
    resumen final que incluya:
    - Todas las materias con sus calificaciones
    - El promedio general
    - Las materias aprobadas y reprobadas
    - La materia con mejor calificación y su valor
    - La materia con peor calificación y su valor
    '''
    print(f"El listado de todas las materias introducidas es: {lista_materias_total}")
    print(f"El listado de todas las calificaciones es: {lista_calificaciones_total}")
    print(f"El promedio general de calificaciones es: {promedio}")
    print(f"Las materias aprobadas son: {lista_materias_aprobadas}")
    print(f"Las materias reprobadas son: {lista_materias_reprobadas}")
    print(f"La materia con mejor calificación es {lista_materias_total[index_extremo_alto]}, con una nota de {lista_calificaciones_total[index_extremo_alto]}")
    print(f"La materia con peor calificación es {lista_materias_total[index_extremo_bajo]}, con una nota de {lista_calificaciones_total[index_extremo_bajo]}")

if __name__ == "__main__":
    main()