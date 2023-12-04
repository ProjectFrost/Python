parrafo=input("Introduce el parrafo: ")

for i in range(0,len(parrafo)):
    if (parrafo[i]==",") and (parrafo[i+1]!=" "):
        parrafo = parrafo[:i] + ", " + parrafo[i+1:]

print(parrafo)

