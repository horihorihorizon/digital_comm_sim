# module: receiver
# coding: UTF-8

import numpy as np
from numpy import sin, cos, pi
import math
from matplotlib import pyplot
import signal as usrsig
import scipy.signal as scpsig

def quaddet(Fs, Flo, indata):
    size = indata.shape[0]
    t = np.arange(0, 1/Fs*size, 1/Fs)
    lo_i =  cos(2*pi*Flo*t + pi/4)
    lo_q = -sin(2*pi*Flo*t + pi/4)
    out_i = indata * lo_i
    out_q = indata * lo_q
    return [out_i, out_q]

def detlpf(Fs, Flo, in_i, in_q):
    b = scpsig.firls(501 ,[0.0, (0.5*Flo)/(Fs/2), (Flo)/(Fs/2), 1.0], [10**(0/20), 10**(0/20), 10**(-60/20), 10**(-60/20)], [1, 1])
    a = 1
    out_i = scpsig.lfilter(b,a,in_i)
    out_q = scpsig.lfilter(b,a,in_q)
    return [out_i, out_q]