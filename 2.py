import matplotlib.pyplot as plt

x = [i for i in range(-10, 11)]
y1 = []
y2 = []
y3 = []
y4 = []
for i in x:
     a=(1*i)/(1+1**5*i**2)
     y1.append(a)

for i in x:
    a = (2 * i) / (1 + 2 ** 5 * i ** 2)
    y2.append(a)
#for liczba in x:
 #    y3+=[(3*liczba)/(1+((3**5)*(liczba**2)))]

#for liczba in x:
     #y4+=[(4*liczba)/(1+4**5*liczba**2)]
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
ax.plot(y1,'b--',label="x/1+x^2")
ax.plot(y2,color='orange',label="2x/1+(2^5)(x^2)")
#ax.plot(x,y3,color='pink',label="3x/1+(3^5)(x^2)")
#ax.plot(x,y4,color='red',marker='x',label="4x/1+(4^5)(x^2)")
legenda=ax.legend(loc="upper left",shadow=True,fontsize="x-small")
legenda.get_frame().set_facecolor("#FFFF00")
plt.xlabel('oś X')
plt.ylabel('oś Y')
plt.show()