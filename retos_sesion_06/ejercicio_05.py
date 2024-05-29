# Comparar los números 123 y 890, comprobar si tienen la misma paridad ambos pares o ambos impares
numero_1 = 123
numero_2 = 890

pares = (numero_1%2==0) and (numero_2%2==0)
impares = (numero_1%2==1) and (numero_2%2==1)

print("Ambos son pares" if pares else "")
print("Ambos son imppares" if impares else "")