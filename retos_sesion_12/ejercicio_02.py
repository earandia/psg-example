# Tienes una página web y un usuario quiere acceder a ella,
# verifica si el usuario inició sesión para acceder a la página, 
# caso contrario muestra un mensaje de error

print ("inicia sesion")
print ("accede")
inicia = input("Usuario inicio sesion: ")
print("bienvenido, que desea hacer?" if (inicia) else "Debe iniciar sesion. usuario no registrado")