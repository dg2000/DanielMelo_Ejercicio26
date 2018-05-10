import numpy as np

import matplotlib as plt

vel = np.random.random(1000)*10.0 + 35.0

ang = np.random.random(1000)*np.pi/2.0


def fun(v, teta):

    return v*v*np.sin(2.0*teta)/9.8




