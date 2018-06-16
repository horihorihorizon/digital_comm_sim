# module: generator
# coding: UTF-8

import numpy as np
from numpy import sin, cos, pi
import math
from matplotlib import pyplot

def quadmod(Fs, Flo, in_i, in_q):
    size = min(in_i.shape[0], in_q.shape[0])
    t = np.arange(0, 1/Fs*size, 1/Fs)
    lo_i =  cos(2*pi*Flo*t + pi/4)
    lo_q = -sin(2*pi*Flo*t + pi/4)
    out = in_i * lo_i + in_q * lo_q
    return out

def baseband(Fs, SymbolRate, Point, Type='BPSK'):
    SamplePerBit, rem = divmod(Fs, SymbolRate)
    SamplePerBit = int(SamplePerBit)
    if(Type=='BPSK'):
        SYMBOLE_WIDTH = 1
    elif(Type=='QPSK'):
        SYMBOLE_WIDTH = 2
    REQUIRED_BIT = math.ceil(Point/Fs*SymbolRate*SYMBOLE_WIDTH)  
    out_i = np.zeros(Point)
    out_q = np.zeros(Point)
    npz_stream = pn9(REQUIRED_BIT) * 2 - 1
    if(rem != 0):
        print('GENERATE: illegal symbolrate for sample frequency')    
        return [0, 0]
    if(Type=='BPSK'):
        for j in range(int(Point/SamplePerBit)):
            for k in range(SamplePerBit):
                out_i[j*SamplePerBit+k] = 1/np.sqrt(2)*npz_stream[j]
                out_q[j*SamplePerBit+k] = 1/np.sqrt(2)*npz_stream[j]
    elif(Type=='QPSK'):
        for j in range(int(Point/SamplePerBit)):
            for k in range(SamplePerBit):
                out_i[j*SamplePerBit+k] = 1/np.sqrt(2)*npz_stream[2*j]
                out_q[j*SamplePerBit+k] = 1/np.sqrt(2)*npz_stream[2*j+1]
    return [out_i, out_q]

def pn9(Point):
    reg = 0xFFFF
    out = np.zeros(Point)
    for j in range(Point):
        out[j] = (reg >> 8) & 0x0001
        reg = reg << 1
        if(((reg >> 5) & 0x0001) ^ ((reg >> 9) & 0x0001)):    
            reg = reg |  0x0001
        else:
            reg = reg & ~0x0001
    return out
