import os
from ECG.ecg import read_ecg
file  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"a01.dat")
filer  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"a01r.dat")
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np
from scipy.fftpack import fft

events = 700000
eventsr =4*events

T = 1/100

yr = read_ecg(filer,0,eventsr)

RespN = yr[2::4]
x = np.arange(len(RespN))/100
# print(len(x),len(RespN))
# plt.plot(x,RespN)
# xf = np.sort(1/x)
# yf = np.sort(np.abs(fft(RespN)))


yf = np.abs(fft(RespN))

plt.plot(yf)





plt.show()