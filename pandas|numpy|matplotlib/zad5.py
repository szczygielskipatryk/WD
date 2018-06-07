import numpy as np
import math as mt
x=np.arange(1,21,1)
print(x)
c=x.copy()
np.random.shuffle(c)
print("wektor po random: "+str(c))
b=c.reshape((5,4))
print(b)
f=b.astype('float')
print("suma kolum macierzy b to: " +str(b.sum(axis=0)))
for i in range(5):
    for j in range(4):
        f[i][j]=mt.pow(f[i][j],1/3)
print("Macierz b z elementami do potęgi 1/3:\n"+str(f))
var1=b.flatten()
var1.sort()
print(var1)

