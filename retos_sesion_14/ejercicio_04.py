# Crear una función anónima para obtener el área de un círculo con radio 5
import math


area = lambda radio:math.pi*radio**2
resultado = area(5)
print(f"El area del circulo es: {resultado}")