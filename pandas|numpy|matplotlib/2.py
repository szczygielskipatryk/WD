import matplotlib.pyplot as plt
import numpy as np
import pandas as pn
import xlrd
import openpyxl
var=pn.ExcelFile('1.xlsx')
x=pn.read_excel(var)
var1=x.groupby(['Płeć']).agg({'Liczba':['sum']})
print(var1)
wykres=var1.plot.bar()
wykres.set_xlabel("Płeć")
wykres.set_ylabel("Liczba urodzeń")
plt.show()