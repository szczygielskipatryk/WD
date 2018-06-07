import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt
plik=pd.read_csv('wig.csv')
plik.Data=pd.to_datetime(plik.Data)
print(plik)
seria=plik.set_index('Data')['Zamkniecie']
print(seria)
print(seria.index)
plt.subplot(211)
plt.plot(seria)
plt.title('Wartość WIG')
plt.xlabel('Rok')
plt.ylabel('Wartość')
plt.subplot(212)
plik=plik.set_index('Data')
var3=seria.tail(100)
var4=var3.cumsum()
var5=pd.DataFrame(var4)
var5['MA100']=var5.rolling(window=20).mean()
print("xXXXXXXXXXXXXXXXXXXXx")
print(var5)
plt.plot(var5,var3)
plt.legend()
plt.show()