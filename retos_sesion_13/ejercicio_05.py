# Imprimir un tablero de ajedrez de 8x8 con los caracteres # y *
fila_list = ""
for columna in range(1,9):
    fila_list =""
    for fila in range(1,9):
        if fila%2==1:
            fila_list +=" * "
        else:
            fila_list +=" # "
    print(fila_list)

