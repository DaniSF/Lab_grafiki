import math
import pylab
import numpy as np

t = np.arange(0, 10, 0.01)

pylab.ion()

for n in range (50):
    xlist = [math.sin(t + n) for t in t]
    ylist = [math.cos (2*t) for t in t]
    pylab.clf()
    pylab.plot (xlist, ylist)
    pylab.draw()
    pylab.pause(0.3)


pylab.close()
