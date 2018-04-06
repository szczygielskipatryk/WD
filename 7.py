lista4 = []
lista5 = []
lista6 = []
import random
random.seed()
for i in range(10):
    z = random.randint(1, 10)
    lista4.append(z)
for i in range(10):
    z = random.randint(1, 10)
    lista5.append(z)
print(lista4+lista5)
print(sorted(lista4),sorted(lista5))
lista6=(set(lista4)&set(lista5))
print (lista6)
