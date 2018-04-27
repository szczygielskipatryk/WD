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
pyl.figure(1)
pyl.subplot(221)
pyl.plot(x,y1,'r',label="y=sin(x)")
legend=pyl.legend(loc='lower center',shadow=True,fontsize='x-small')
legend.get_frame().set_facecolor('#55FF55')
pyl.subplot(222)
pyl.plot(x,y2,'b',label="y=sin(2x)")
legend=pyl.legend(loc='lower center',shadow=True,fontsize='x-small')
legend.get_frame().set_facecolor('#55FF55')
pyl.subplot(223)
pyl.plot(x,y3,color='pink',label="y=sin(3x)")
legend=pyl.legend(loc='lower center',shadow=True,fontsize='x-small')
legend.get_frame().set_facecolor('#55FF55')
pyl.subplot(224)
pyl.plot(x,y4,color='orange',label="y=sin(4x)")
legend=pyl.legend(loc='lower center',shadow=True,fontsize='x-small')
legend.get_frame().set_facecolor('#55FF55')
pyl.show()