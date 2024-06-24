# Imprimir los 20 primeros números de la serie de Fibonacci
serie = []
primer_nro = 0
actual_nro = 1
siguiente_nro = primer_nro + actual_nro

contador = 1

while contador < 21:
    serie.append(actual_nro)
    contador += 1
    primer_nro = actual_nro
    actual_nro = siguiente_nro
    siguiente_nro = primer_nro + actual_nro

print(serie)
    
