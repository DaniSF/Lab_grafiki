import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-10, 10, 0.01)
a = 'plt.plot(x, ' + input() + ')'
eval(a)
plt.xkcd()
plt.show()
