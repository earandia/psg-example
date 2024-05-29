# Crear una lista de personas con 10 nombres de personas
nombres = ['Mario','Alberto','Juan','Antonia','Fernanda','Felipe','Jhon','Ines','Paula','Pedro']

# Obtener una sub lista de 2 a 7
sublista = nombres[2:7]

# Buscar si existe el nombre "Jhon" en la lista original
print("Jhon existe en la lista original" if nombres.index("Jhon") else "Jhon NO existe en la lista original")

# Ordenar la sub lista alfabéticamente
sublista.sort()
print(sublista)

# Ordenar la lista original alfabéticamente de forma descendente
sublista.sort(reverse=True)
print(sublista)