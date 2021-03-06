# module: signal
# coding: UTF-8

import numpy as np
import math

class fir:

    def __init__(self, coef):
        self.coef = coef
        self.buff = np.zeros(coef.shape[0])

    def filter(self, indata):
        self.buff = np.roll(self.buff, 1)
        self.buff[0] = indata
        outdata = np.sum(self.buff * self.coef)
        return outdata

    def filter_array(self, indata):
        outdata = np.zeros(indata.shape[0])
        for j in range(indata.shape[0]):
            outdata[j] = self.filter(indata[j])
        return outdata