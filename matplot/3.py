import matplotlib.pyplot as plt
import numpy as np
x=np.random.normal(size=100)
n,bind,patches=plt.hist(x)
plt.title("Histogram")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
