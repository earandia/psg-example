# Una tienda ofrece descuentos a sus clientes, 
# si el cliente es mayor de edad y tiene una compra mayor a 1000, 
# se le aplica un descuento del 10%, 
# si es menor de edad y tiene una compra mayor a 500 se le aplica un descuento del 5%, 
# si no cumple ninguna condición se le aplica un descuento del 2%
edad = input("Es mayor de edad?(SI | NO) ")
compra = int(input("Ingrese monto de compra:"))
descuento = 0

if (edad == 'SI' or edad == "si"):
    if compra > 1000:
        descuento = 0.1
elif compra >500:
    descuento = 0.05
else:
    descuento = 0.02

print("descuento del ",descuento*100,"por ciento")