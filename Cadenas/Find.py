cadena=input("Introduce la cadena: ")
subcadena=(input("Introduce el caracter a encontrar: "))[:1]
contador=0

for i in range(0,len(cadena)):
    if subcadena == cadena[i]:
        contador+=1
            

print(f"El caracter {subcadena} aparece {contador} veces")