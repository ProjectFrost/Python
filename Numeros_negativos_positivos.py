rep=int(input("Introduzca el número de numeros a introducir: "))
positivo=0;
neutro=0;
negativo=0;

for i in range(0,rep):
    num=int(input("Introduzca un numero: "))
    if (num>0):
        positivo+=1
    elif (num<0):
        negativo+=1
    else:
        neutro+=1
print("Positivos: "+str(positivo)+"\nNeutros: "+str(neutro)+"\nNegativos: "+str(negativo))