# module: receiver
# coding: UTF-8

import numpy as np
from numpy import sin, cos, pi
import math
from matplotlib import pyplot

def quaddet(Fs, Flo, indata):
    size = indata.shape(0)
    t = np.arange(0, 1/Fs*size, 1/Fs)
    lo_i =  cos(2*pi*Flo*t + pi/4)
    lo_q = -sin(2*pi*Flo*t + pi/4)
    out_i = indata * lo_i
    out_q = indata * lo_q
    return [out_i, out_q]

