import matplotlib.pyplot as pyl
import numpy as np
x=np.linspace(-np.pi,np.pi,201)
y1=[]
y2=[]
y3=[]
y4=[]
for rzecz in x:
    y1 += [np.sin(rzecz * 1)]
    y2 += [np.sin(rzecz * 2)]
    y3 += [np.sin(rzecz * 3)]
    y4 += [np.sin(rzecz * 4)]
pyl.xlabel('X')
pyl.ylabel('Y')
ax=pyl.subplot()
ax.plot(x,y1,'r',label="y=sin(x)")
ax.plot(x,y2,'b',label="y=sin(2x)")
ax.plot(x,y3,color='pink',label="y=sin(3x)")
ax.plot(x,y4,color='orange',label="y=sin(4x)")
legend=ax.legend(loc='lower center',shadow=True,fontsize='x-small')
legend.get_frame().set_facecolor('#55FF55')
pyl.show()