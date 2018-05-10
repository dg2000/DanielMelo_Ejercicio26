import numpy as np

import matplotlib as plt

from matplotlib.pylab import hist, show


vel = np.random.random(1000000)*10.0 + 35.0

ang = np.random.random(1000000)*np.pi/2.0


def fun(v, teta):

    return v*v*np.sin(2.0*teta)/9.8

d = fun(vel, ang)




hist(d, bins=80)
show()

a1 = d >= 56 
a2 = d >= 110 
a3 = d >= 26 
a4 = d >= 172 

b1 = d <= 66
b2 = d <= 120
b3 = d <= 36
b4 = d <= 182

d1 = np.concatenate((a1, b1), axis=0)
d2 = np.concatenate((a2, b2), axis=0)
d3 = np.concatenate((a3, b3), axis=0)
d4 = np.concatenate((a4, b4), axis=0)
