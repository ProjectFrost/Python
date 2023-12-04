parrafo=input("Introduce el parrafo: ")
i=0

for i in range(0,len(parrafo)):
    if (parrafo[i]=="."):
        parrafo = parrafo[:i] + (parrafo[i+1:])

print(parrafo)

