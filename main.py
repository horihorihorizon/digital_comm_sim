import generator as gen
import receiver as rx
import numpy as np
import signal as usrsig
import scipy.signal as scpsig 
from matplotlib import pyplot 

Fs = 48e3
Flo = 1000
SR = 200
Point = 19200

[i, q] = gen.baseband(Fs, SR, Point)
rf = gen.quadmod(Fs, Flo, i, q)

[mixout_i, mixout_q] = rx.quaddet(Fs, Flo, rf)
[lpfout_i, lpfput_q] = rx.detlpf(Fs, Flo, mixout_i, mixout_q)

pyplot.plot(lpfout_i)
pyplot.plot(lpfput_q)
#pyplot.plot(rf)
pyplot.grid()
pyplot.show()
