lista3 = []
import random

random.seed
for i in range(10):
    z = random.randint(0, 15)
    lista3.append(z)
lista3.sort()
lista3.reverse()
print (lista3)
plik=open("pliki.txt","r+")
plik.writelines(str(lista3))
plik.close()