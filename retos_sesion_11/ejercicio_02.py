# Crea un diccionario para almacenar información de comidas de animales por ejemplo
# comidas = {"carne" : {"animales": ["león", "tigre"]}, "frutas" : {"animales": ["mono", "elefante"]}}

comidas = {"carne" : {"animales": ["león", "tigre"]}, "frutas" : {"animales": ["mono", "elefante"]}}
print(comidas)
# Añade al diccionario de comidas 4 alimentos más usando update(clave=valor)

comidas.update({"vegetales" : {"animales": ["conejo","cerdo"]}, "seca":{"gato","perro"}, "humeda":{"gato","perro"}, "variada":{"cerdo","raton","rata"}})

print(comidas)
# Existe en el diccionario de comidas la comida 'carne'?
existe_carne = 'carne' in comidas

# Elimina la comida 'frutas' del diccionario de comidas
del comidas['frutas']
print(comidas)