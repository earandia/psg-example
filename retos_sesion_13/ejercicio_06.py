# Crea un ciclo infinito que reciba un número por teclado y 
# verifique si es un número primo, 
# termina la ejecución si se ingresa el número 0 
while True:
    numero = int(input("ingresa un numero:"))

    if (numero != 0):
        for i in range(2,int(numero/2)):
            if (numero%i) == 0:
                es_primo = False
                if es_primo:
                    print("es primo")
                else:
                    print("no es primo")
                break
    else:
        break


