
# Crea una calculadora por consola que realice las operaciones de 
# suma, resta, multiplicación y división, 
# ingresa dos números y la operación a realizar, 
# verifica si la operación es válida y muestra el resultado

# Número 1: 10
# Número 2: 5
# Operación: +
# -------------
# Resultado: 15

numero_1 = int(input("número 1:"))
numero_2 = int(input("número 2:"))
operacion = input("operacion a realizar (+ - * /):")
resultado = 0

if operacion == "/":
    resultado = numero_1 / numero_2
elif operacion == "*":
    resultado = numero_1 * numero_2
elif operacion == "-":
    resultado = numero_1 - numero_2
else:
    resultado = numero_1 + numero_2

print("Número 1:",numero_1)
print("Número 2:",numero_2)
print("Operacion:",operacion)
print("------------")
print("Resultado:",resultado)