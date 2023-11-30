num=int(input("Introduce el número del que quieres su factorial: ")) 
aux=1

for i in range(num,0,-1):
    aux*=i
print(aux) 