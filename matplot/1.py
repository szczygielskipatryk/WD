import matplotlib.pyplot as plt

x = [i for i in range(1, 11)]
y1 = []
y2 = []
y3 = []
y4 = []
for liczba in x:
    y1 += [1/liczba ** 1]
for liczba in x:
    y2 += [1 / liczba ** 2]
for liczba in x:
    y3 += [1/liczba ** 3]
for liczba in x:
    y4 += [1/liczba ** 4]
plt.plot(x, y1,'b--',label="1/x")
plt.plot(x,y2,'yo-',label="1/(x^2)")
plt.plot(x,y3,'g-',label="1/(x^3)")
plt.plot(x,y4,color='orange',label="1/(x^4)")
legenda=plt.legend(loc="upper right",fontsize="x-small")
legenda.get_frame().set_facecolor("#66FF00")
plt.xlabel('X')
plt.ylabel('Y')
plt.show()