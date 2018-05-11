import numpy as np
a=np.arange(2,42,2)
b=np.arange(1.0,4.5,0.5)
c=b.astype('int64')
print(a)
print(b)
print (c)
wymiar=input("Podaj wymair tablicy(x*x):")
n=int(wymiar)
x=np.arange(0,n,1)
for p in x:
    m=np.array(np.arange(n)+p*n)
    print(m)