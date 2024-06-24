# Crea un diccionario con las siguientes tuplas de animales
tupla = (('perro', '🐶') , ('gato','🐱') , ('aves',['🐦','🦅']))
diccionario = dict(tupla)
print("Diccionario creado desde una tupla")
print(diccionario)
#  Del diccionario obtén y elimina el valor de la clave 'aves'
del diccionario['aves']
print("eliminada la clave ave del diccionario")
print(diccionario)
#  Modifica el valor de la clave 'gato' por '🐈'
diccionario['gato'] = '🐈'
print("modificacion de la  clave gato del diccionario")
print(diccionario)
#  Cambia la clave perro por perros y su valor por ['🐶','🐕']
diccionario['perros'] = diccionario['perro']
del diccionario['perro']
diccionario['perros'] = ['🐶','🐕']
print("cambio la clave  de perro por perros")
print(diccionario)


