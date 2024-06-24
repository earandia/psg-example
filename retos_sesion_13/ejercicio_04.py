# Crea un ciclo infinito que reciba una palabra por teclado y verifique si es palíndrome, 
# termina la ejecución si se ingresa la palabra salir
while True:
    cadena = input("Ingrese una palabra: ")
    palindrome = cadena[::-1]

    if cadena == palindrome:
        print(f"La palabra {cadena.upper()} es palindrome")
    else:
        print(f"La palabra {cadena.upper()} no es palindrome")
