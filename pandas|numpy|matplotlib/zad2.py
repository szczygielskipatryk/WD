import numpy as np
import matplotlib.pyplot as plt
x=np.arange(-5,6,1)
var1=[]
for liczba in x:
    var1.append(pow(liczba,3)+3)
#plt.plot(x,var1,'X--y')
#plt.show()
#zad3
b=np.zeros((5,5))
#print(b)
for x in range(5):
    for j in range(5):
        if(x==j):
            b[x][j]=(x+1)**2
#print(b)
g=np.eye(5)
g=np.hstack((g, np.ones((5,1))))
#print(g)
#zad4
import pandas as pd
zamowienia=pd.read_csv('zamowienia.csv',delimiter=';')
#print(zamowienia)
var2=zamowienia.groupby(['Kraj']).agg({'Kraj':['count']})
plt.figure(1)
var2.plot.pie(subplots=True, autopct='%.2f % %',figsize=(5,5))
plt.show()
var5={'Sprzedawca':zamowienia['Sprzedawca']}
print(var5)
var6=pd.value_counts(var5['Sprzedawca'], sort=True)
print(var6)
var7=var6[0:3]
plt.figure(2)

var7.plot.bar()
plt.show()
