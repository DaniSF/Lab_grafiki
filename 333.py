import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 5.01, 0.01)
plt.plot(x, np.log((x*x+1)*np.exp(-abs(x)/10))/np.log(1+np.tan(1/(1+np.sin(x)*np.sin(x)))))
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.title(r'$f_1(x)=\sin(x),\ f_2(x)=\cos(x),\ f_3(x)=-x$')
plt.grid(True)
plt.show()
