import math,sys
num=int(input("Introduce el numero: "))
esPrimo=True;

if num==1:
    esPrimo=False
    print("Es el numero primo: "+ str(esPrimo))
    sys.exit(0)

for divisor in range(2,int(math.sqrt(num)+1)):
   if (num%divisor==0):
        esPrimo=False
        break
print("Es el numero primo: "+ str(esPrimo))