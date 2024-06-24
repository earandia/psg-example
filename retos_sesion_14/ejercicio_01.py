# Un estudiante desea saber cuál es su promedio de calificaciones en la materia de matemáticas, 
# cree una función que reciba las calificaciones como lista y 
# devuelva el promedio las calificaciones son 20,40,60,51,13

def promedio(calificaciones):
    total = sum(calificaciones)
    cantidad = len(calificaciones)

    return total / cantidad


print("calificaciones de matemáticas")
calificacion_list = []
while True:
    calificacion = int(input("calificacion: "))
    if(0<calificacion<=100):
        calificacion_list.append(calificacion)
    else:
        break

print(f"El promedio de las calificaciones es ",promedio(calificacion_list))