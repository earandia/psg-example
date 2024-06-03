# El usuario Jhon Doe esta en una red social sus amigos son:
#   {Alice, Bob, Charlie, David, Eve}
# La usuaria Jess Doe tiene los siguientes amigos
#    {Alice, Bob,  Frank, Grace}


jhon = {"Alice", "Bob", "Charlie", "David", "Eve"}
jess = {"Alice", "Bob", "Frank", "Grace"}


# ¿Tienen Jhon y Jess amigos en común?,
print("¿Tienen Jhon y Jess amigos en común?","SI" if len(jhon.intersection(jess)) > 0 else "NO")

# ¿Cuáles son?
print ("¿Cuáles son?",jhon.intersection(jess))