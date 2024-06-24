# Dar las felicitaciones a los estudiantes que 
# aprobaron el curso de la siguiente tupla de estudiantes
estudiantes = [('Juan', 51), ('Pedro', 80), ('Maria', 90), ('Ana', 40), ('Luis', 30)]

for estudiante in estudiantes:    
    if estudiante[1]>50:
        print(f"Felicidades {estudiante[0]}, aprobastes el curso con {estudiante[1]}")

