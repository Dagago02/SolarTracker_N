archivo= open("Potenciometros.txt","w") 
archivo.write(f"{pot1},{pot2}")

archivo = open("Potenciometros.txt", "r")
for linea in archivo.readlines():
    columna= str(linea).split(",")
    Npot1=int(columna[0])
    Npot2=int(columna[1])
    print(columna[0])
    print(columna[1])

print(type(Npot1))

