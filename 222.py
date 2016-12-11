import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-5, 5.01, 0.01)
plt.plot(x,  x*x - x - 6, x, x*0)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'$f_1(x)=\sin(x),\ f_2(x)=\cos(x),\ f_3(x)=-x$')
plt.grid(True)
plt.show()
