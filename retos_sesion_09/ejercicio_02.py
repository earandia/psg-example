# De la siguiente lista [1,2,3,4,5,6,7,8,9,10] obtener una sub lista inversa utilizando índices de 3 en 3
lista = [1,2,3,4,5,6,7,8,9,10]

sublista = lista[-10:-1:3]
sublista.sort(reverse=True)

print(sublista)


