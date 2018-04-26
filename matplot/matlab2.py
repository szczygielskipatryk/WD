import matplotlib.pyplot as plt

x = [i for i in range(-10, 11)]
y1 = []
y2 = []
y3 = []
y4 = []
for liczba in x:
     y1+=[liczba/(1+(liczba**2))]
for liczba in x:
     y2+=[(2*liczba)/(1+((2**5)*(liczba**2)))]

for liczba in x:
     y3+=[(3*liczba)/(1+((3**5)*(liczba**2)))]

for liczba in x:
     y4+=[(4*liczba)/(1+((4**5)*(liczba**2)))]
ax=plt.subplot()
ax.plot(x, y1,'b--',label="x/1+x^2")
ax.plot(x, y2,color='orange',label="2x/1+(2^5)(x^2)")
ax.plot(x,y3,color='pink',label="3x/1+(3^5)(x^2)")
ax.plot(x,y4,color='red',marker='x',label="4x/1+(4^5)(x^2)")
legenda=ax.legend(loc="upper left",shadow=True,fontsize="x-small")
legenda.get_frame().set_facecolor("#FFFF00")
plt.xlabel('X')
plt.ylabel('Y')
plt.show()