
mochilero_a = {"París", "Londres", "Nueva York", "Tokio","Peru", "Chile", "Colombia", "Bolivia"}
mochilero_b = {"Londres", "Roma", "Nueva York", "Sidney","Argentina","Brasil","Panama","Bolivia"}

visitar_b = mochilero_a.difference(mochilero_b)
visitar_a = mochilero_b.difference(mochilero_a)

print(visitar_a)
print(visitar_b)


# Ahora quieren saber en que ciudades han estado ambos mochileros
ambas_ciudades = mochilero_a.intersection(mochilero_b)
print(ambas_ciudades)