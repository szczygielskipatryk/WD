import matplotlib.pyplot as plt
import numpy as np
import pandas as pn
import xlrd
import openpyxl
import datetime
now=datetime.datetime.now()
var=pn.ExcelFile('1.xlsx')
x=pn.read_excel(var)
wer=now.year
print(wer)
var2=x[x['Rok']>=wer-5]
var1=var2.groupby(['Płeć']).agg({'Liczba':['sum']})
print(var1)
wykres=var1.plot.pie(subplots=True, autopct='%.2f % %',figsize=(5,5))
plt.title("Procent urodzeń dzieci w latach 2013-2018 według płci")
#wykres.set_xlabel("Płeć")
#wykres.set_ylabel("Liczba urodzeń")
plt.show()