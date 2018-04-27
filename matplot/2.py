import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,50)
y1 = []
y2 = []
y3 = []
y4 = []
for liczba in x:
     y1+=[(liczba)/(1+(liczba**2))]
for liczba in x:
     y2+=[(2*liczba)/(1+((2**5)*(liczba**2)))]

for liczba in x:
     y3+=[(3*liczba)/(1+((3**5)*(liczba**2)))]

for liczba in x:
     y4+=[(4*liczba)/(1+4**5*liczba**2)]
fig=plt.figure()
bx=fig.add_subplot(111)
fig.suptitle("Działanie")
fig.subplots_adjust(top=0.85)
bx.set_title("podtytuł")
bx.text(-8,0.2,r' $\frac{n*x}{1+n^5 *x^2}$')
bx.annotate('Strzałka na (0,0)', xy=(0,0), xytext =(0.1,0.1),arrowprops=dict(facecolor='yellow',shrink=0.01))
bx.text(2,-0.4,"Tekst w ramce",bbox={'facecolor':'blue'})
bx.text(-2,0.4,"tekst poza ramką")
ax=plt.subplot()
ax.plot(x, y1,'b--',label=r"$\frac{x}{1+x^2}$")
ax.plot(x, y2,color='orange',label=r"$\frac{2x}{1+(2^5)(x^2)}$")
ax.plot(x,y3,color='pink',label=r'$\frac{3x}{1+(3^5)(x^2)}$')
ax.plot(x,y4,color='red',label=r"$\frac{4x}{1+(4^5)(x^2)}$")
legenda=ax.legend(loc="upper left",shadow=True,fontsize="x-small")
legenda.get_frame().set_facecolor("#FFFF00")
plt.xlabel('oś X')
plt.ylabel('oś Y')
plt.show()