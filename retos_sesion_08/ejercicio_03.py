# Ingresa una cadena por teclado y almacena el valor en una tupla
# Concatena la tupla ('¡', ) + tupla almacenada + la tupla ('!', )
# Imprime el resultado concatenado
# Repite la tupla final 3 veces e imprime el nuevo resultado

cadena = input("Ingresa un texto: ")
cadena_tupla = tuple(cadena)
# print(cadena_tupla)
resultado = ('¡', "") + cadena_tupla + ('!', "")
print(resultado)

nuevo_resultado = resultado*3
print(nuevo_resultado)

