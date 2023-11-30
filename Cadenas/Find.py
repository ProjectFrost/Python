cadena=input("Introduce la cadena: ")
subcadena=input("Introduce la subcadena: ")
start=0;

for i in range(start,len(cadena)):
    for j in subcadena:
        if subcadena[j] == cadena[i]:
            d
print(f"¿Empieza la cadena con la subcadena?: {cadena.startswith(subcadena)}")