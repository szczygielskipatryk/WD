import numpy as np
n=input("1:")
b=int(n)
empty=np.empty((b,b))
x=1
for i in range(b):
    for j in range(b):
        empty[i,j]=x
        x=x+1
k=empty.astype('int64')
print(k)