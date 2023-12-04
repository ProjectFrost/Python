cadena=input("Introduce la cadena: ")
caracter=(input("Introduce el caracter a encontrar: "))[:1] #Coje el primer caracter
contador=0

for i in cadena:
    if caracter == cadena[i]:
        contador+=1
        print(f"Posicion en la cadena --> {i}")
            

print(f"El caracter {caracter} aparece {contador} veces")