# Anita y Pepito llevan saliendo juntos por 4 semanas, cada vez que salen van a comer a una plaza de comidas. 
# Ambos quieren saber que tan compatibles son viendo cuantos platos de comida tienen en común. 
# A continuación tienes los platos de comida que ambos han ido pidiendo a los largo de sus citas:

#Anita: Sushi, Pizza, Tacos, Hamburguesa, Pasta, Alitas
#Pepito: Pizza, Tacos, Ensalada, Pasta, Helado, Milanesa

#Si la cantidad platos de comida que tienen en comunes mayor a 50% entonces ambos seguirán saliendo

anita = {"Sushi", "Pizza", "Tacos", "Hamburguesa", "Pasta", "Alitas"}
pepito = {"Pizza", "Tacos", "Ensalada", "Pasta", "Helado", "Milanesa"}

comida_comun = anita.intersection(pepito)
comida_promedio = len(anita)
cantidad_comida_comun = len(comida_comun)
promedio = (cantidad_comida_comun*100)/comida_promedio

print("seguiran saliendo" if promedio > 50 else "no seguiran saliendo")