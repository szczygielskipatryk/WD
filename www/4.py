import numpy as np
k=input("podaj podstawe potęgi: ")
m=input("Podaj ile ( do której potegi) chcesz potęgowac: ")
p=int(k)
f=int(m)
w=np.logspace(1,f,f,base=p)
potega=w.astype('int64')
print(potega)
