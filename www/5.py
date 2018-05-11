import numpy as np
m=input("Podaj długosc wektora: ")
wektor=np.arange(int(m),0,-1)
var2=int(m)
print(wektor)
k=wektor.astype('int64')
wer=np.diag(wektor)
print(wer)