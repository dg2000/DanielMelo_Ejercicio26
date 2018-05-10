import numpy as np

import matplotlib.pyplot as plt




v0 = np.random.uniform(35.0, 45.0, 100000000)

ang = np.random.uniform(0.0, np.pi/2.0, 100000000)


def fun(v, teta):

    return v*v*np.sin(2.0*teta)/9.8

d = fun(v0, ang)


#Primera iteracion
d1 = np.logical_and(d>=56, d<=66)

pv1 = v0[d1]



#Segunda iteracion
d2 = np.logical_and(d>=110, d<=120)
pv2 = v0[d2]

#Tercera iteracion

d3 = np.logical_and(d>=26, d<=36)
pv3 = v0[d3]

#Cuarta iteracion

d4 = np.logical_and(d>=172, d<=182)
pv4 = v0[d4]

plt.hist(v0, bins=100, normed = True, label="Inicial")
plt.hist(pv1, bins=100, normed = True, label="Primera iteracion")
plt.hist(pv2, bins=100, normed = True, label="Segunda iteracion")
plt.hist(pv3, bins=100, normed = True, label="Tercera iteracion")
plt.hist(pv4, bins=100, normed = True, label="Cuarta iteracion")
plt.xlabel("Velocidad")
plt.ylabel("Densidad de probabilidad")
plt.legend(loc=0)

plt.savefig("Densidades de probabilidad")
