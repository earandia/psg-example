# Tienes una página web y un usuario quiere acceder a ella,
# verifica si el usuario inició sesión para acceder a la página, 
# caso contrario muestra un mensaje de error

inicia = input("Usuario inicio sesion(SI | NO): ")
print("bienvenido, que desea hacer?" if (inicia == 'SI') else "Debe iniciar sesion. usuario no registrado")