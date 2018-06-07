import matplotlib.pyplot as plt
import numpy as np
import pandas as pn
x=pn.read_csv('zamowienia.csv',delimiter=';')
print(x)
v=x.groupby(['Sprzedawca']).agg({'Sprzedawca':['count']})
print(v)
wykres=v.plot.bar()
plt.show()