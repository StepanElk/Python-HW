import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


x = np.arange(0,4*np.pi,0.1)   # start,stop,step
y = np.log10(x) + np.cos(x)
plt.plot(x, y)
plt.show()