# Imprimir los 20 primeros números primos
nro_primo = 2
primo_list = []

contador = 1

while contador <= 20:
    if (nro_primo % (nro_primo/2) == 0) :
        primo_list.append(nro_primo)
        contador += 1
    nro_primo += 1

print("Los 20 primeros números primos son: ",primo_list)