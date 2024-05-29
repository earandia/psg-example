# Tienes una tienda de abarrotes y tienes dos listas una con los productos que tienes y otra con los precios
productos = ["arroz","fideo"]
precios = [4,3]

# Agregar 5 productos nuevos al final de las listas
productos.append("pan")
precios.append(0.5)
productos.append("leche")
precios.append(4)
productos.append("huevo")
precios.append(0.7)
productos.append("azucar")
precios.append(6)
productos.append("harina")
precios.append(3)
# Eliminar el producto con el nombre "Leche" de las listas
productos.remove("leche")
# ¿Cuanto cuesta el producto "Pan" y "Huevo"?
print("Pan cuesta",precio[mi_lista.index("pan")])
print("Huevo cuesta",precio[mi_lista.index("huevo")])

# ¿Cual es el producto más caro y más barato?
max_price_producto = max(precios)
min_price_producto = min(precios)

max_producto = productos[precio.index(max_price_producto)]
min_producto = productos[precio.index(min_price_producto)]

print("producto mas caro:",max_producto)
print("producto mas barato:",min_producto)

# ¿Cuántos productos tienes en total?
total_productos = len(productos)
print("total productos:",total_productos)
# ¿Cuanto cuesta el total de los productos?
costo_total_productos = sum(precios)
print("Total de los productos:",costo_total_productos)
# Ordena los productos alfabéticamente y precios si es posible
productos.sort(reverse=True)
# Eliminar todos los productos de las listas
productos.clear()

# Convertir y ejecutar el archivo de la "sesion09.py" a un archivo en jupyter notebook 
