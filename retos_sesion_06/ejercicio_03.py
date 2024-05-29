# Imprime una tabla de verdad para la siguiente afirmación: 
# "Una puerta tiene dos interruptores que controlan dos luces 
# la puerta sólo debe abrirse cuando las dos luces están apagadas o las dos están encendidas, 
# caso contrario la puerta no se abre, ¿qué operador lógico se puede utilizar?"

print("---------------Utilizando los operadores and y or---------------")
interruptor_1 = False #luz apagada
interruptor_2 = False #luz apagada
print("Abrir puerta" if (interruptor_1==False and interruptor_2==False) or (interruptor_1 == True and interruptor_2 == True) else "Cerrar puerta")

interruptor_1 = True #luz encendida
interruptor_2 = True #luz encendida
print("Abrir puerta" if (interruptor_1==False and interruptor_2==False) or (interruptor_1 == True and interruptor_2 == True) else "Cerrar puerta")

interruptor_1 = True #luz encendida
interruptor_2 = False #luz apagada
print("Abrir puerta" if (interruptor_1==False and interruptor_2==False) or (interruptor_1 == True and interruptor_2 == True) else "Cerrar puerta")

interruptor_2 = True #luz encendida
interruptor_1 = False #luz apagada
print("Abrir puerta" if (interruptor_1==False and interruptor_2==False) or (interruptor_1 == True and interruptor_2 == True) else "Cerrar puerta")


print("---------------Utilizando los operadores and, or y not---------------")
interruptor_1 = False #luz apagada
interruptor_2 = False #luz apagada
print("Abrir puerta" if (interruptor_1 and interruptor_2) or (not interruptor_1 and not interruptor_2) else "Cerrar puerta")

interruptor_1 = True #luz apagada
interruptor_2 = True #luz apagada
print("Abrir puerta" if (interruptor_1 and interruptor_2) or (not interruptor_1 and not interruptor_2) else "Cerrar puerta")

interruptor_1 = True #luz encendida
interruptor_2 = False #luz apagada
print("Abrir puerta" if (interruptor_1 and interruptor_2) or (not interruptor_1 and not interruptor_2) else "Cerrar puerta")

interruptor_2 = True #luz encendida
interruptor_1 = False #luz apagada
print("Abrir puerta" if (interruptor_1 and interruptor_2) or (not interruptor_1 and not interruptor_2) else "Cerrar puerta")

