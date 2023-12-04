cadena=input("Introduce la cadena: ")
subcadena=(input("Introduce el caracter a encontrar: "))[:1] #Coje el primer caracter
contador=0

for i in cadena:
    if subcadena == cadena[i]:
        contador+=1
        print(f"Posicion en la cadena --> {i}")
            

print(f"El caracter {subcadena} aparece {contador} veces")