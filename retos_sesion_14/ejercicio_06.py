# Crear una función que reciba una lista de números y
#  devuelva solo los números pares

def get_numero_par(numeros_pares_list):
    numeros_pares = list()  
    for numero in numeros_pares_list:
        if numero%2 == 0:
            numeros_pares.append(numero)
    return numeros_pares


numeros_list = [21,24,61,33,50]

print(get_numero_par(numeros_list))