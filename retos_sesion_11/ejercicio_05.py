# Eres NOE y tienes que guardar dos animales de cada especie en un arca, crea un diccionario con las especies
arca = {"perro" : 2, "gato" : 2, "tigre" : 2, "mono" : 2, "unicornio" : 0, "jirafa" : 1}

#    Añade al arca 2 especies más usando update()
arca.update({"conejo":2,"escarabajo":2})

#     Toma lista de los animales en el arca iterando el diccionario
print("animales en el arca")
for animal in arca:
    print(animal)

#     Existe en el arca la especie 'dragon'?
dragon = arca.get('dragon')
print(f"Existe en el arca la especie 'dragon'?",'SI' if dragon else 'NO')

#     Elimina la especie 'unicornio' del arca
del arca["unicornio"]
print("Elimina la especie 'unicornio' del arca")
print(arca)

#     Modifica el valor de la especie 'jirafa' por 2
arca["jirafa"] = 2
print("Modificado el valor de la especie 'jirafa'")
print(arca)

#     Vacía el arca después del diluvio
arca.clear()
print("Vacía el arca después del diluvio")
print(arca)
