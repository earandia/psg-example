# Calculadora flexible: Crea una calculadora que acepte diferentes operaciones matemáticas 
# como argumentos de palabras clave.
# realice los cálculos correspondientes, 
# las operaciones son suma, resta, multiplicación y división

def datos_persona(**datos):
    resultado = ""
    if datos['op'] == 'suma':
        resultado = f"{datos['numero_1']} + {datos['numero_2']} = {datos['numero_1'] + datos['numero_2']}"
    elif datos['op'] == 'resta':
        resultado = f"{datos['numero_1']} - {datos['numero_2']} = {datos['numero_1'] - datos['numero_2']}"
    elif datos['op'] == 'multiplicacion':
        resultado = f"{datos['numero_1']} * {datos['numero_2']} = {datos['numero_1'] * datos['numero_2']}"
    elif datos['op'] == 'division':
        resultado = f"{datos['numero_1']} / {datos['numero_2']} = {datos['numero_1'] / datos['numero_2']}"
    else:
        resultado = "Operacion invalida"
    return resultado   


numero_1 = int(input("Ingrese un numero: "))
numero_2 = int(input("Ingrese otro numero: "))
operador = input("Ingrese operacion: ")
resultado = datos_persona(op = operador, numero_1 = numero_1, numero_2 = numero_2)
print (resultado)