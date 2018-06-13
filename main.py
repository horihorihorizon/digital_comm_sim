import generator as gen
from matplotlib import pyplot 

Fs = 48e3
Flo = 200
SR = 200
Point = 4800

[i, q] = gen.baseband(Fs, SR, Point)
rf = gen.quadmod(Fs, Flo, i, q)

pyplot.plot(i)
pyplot.plot(q)
pyplot.plot(rf)
pyplot.show()
