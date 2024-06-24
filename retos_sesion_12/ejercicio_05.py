
# Un usuario ingresa su nombre y gustos musicales por teclado separados por coma, 
# verifica si el usuario ingresó un nombre válido usando truthiness, 
# convertir los gustos musicales en una lista y verifica si tiene el gusto rock en su lista de gustos musicales

# Nombre: Jhon Doe
# Gustos musicales: rock,pop,jazz

nombre = input("Ingresa tu nombre:")
gustos = input("Ingresa tu gusto musical:")
print("para terminar de ingresar gusto musical presiona enter")

gustos_list = []
continuar = True

if nombre:
    print("Nombre Valido")
else:
    print("no es un nombre valido")
if gustos:
    gustos_list.append(gustos)
else:
    continuar = False
if continuar:
    gusto_2 = input("Ingresa tu gusto musical:")
    if gusto_2:
        continuar = True
        gustos_list.append(gusto_2)
    else:
        continuar = False
if continuar:
    gusto_3 = input("Ingresa tu gusto musical:")
    if gusto_3: 
        continuar = True
        gustos_list.append(gusto_3)
    else:
        continuar = False
if continuar:
    gusto_4 = input("Ingresa tu gusto musical:")
    if gusto_4:
        continuar = True
        gustos_list.append(gusto_4)
    else:
        continuar = False
if continuar:
    gusto_5 = input("Ingresa tu gusto musical:")
    if gusto_5:
        continuar = True
        gustos_list.append(gusto_5)
    else:
        continuar = False


if gustos_list.index("rock"):
    print("Te gusta el rock")
else:
    print("No te gusta el rock")
