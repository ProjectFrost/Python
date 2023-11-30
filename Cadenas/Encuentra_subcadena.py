cadena=input("Introduce la cadena: ")
subcadena=input("Introduce la subcadena a buscar: ")
if cadena.find(subcadena)==-1:
    print("La subcadena no esta")
else:
    print(f"La subcadena esta")