import numpy as np
import matplotlib.pyplot as plt
import math
x=np.arange(-10,11,1)
var1=[]
for liczba in x:
    if(liczba>0):
        var1.append(1/math.sqrt(liczba))
    else:
        var1.append(0)
plt.plot(x,var1,'o')
plt.show()