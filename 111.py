import numpy as np
x = int(input())
b = np.log((1/np.exp(np.sin(x)+1))/(5/4+1/x**15))/np.log(1+x**2)
print(b)





