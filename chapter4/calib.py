import os
from ECG.ecg import read_ecg
from ECG.ecg_sig import band_pass_filter
file  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"a01.dat")
filer  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"a01r.dat")
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np


events = 4*1000
eventsr =4*events

T = 1/100

y= read_ecg(file,0,events)
yr = read_ecg(filer,0,eventsr)
RespN = yr[2::4]

x = np.arange(len(RespN))/100

yf = band_pass_filter(y,low=0.1,high = 0.5)
RespNf = band_pass_filter(RespN,low=0.1,high = 0.5)

fig, ax = plt.subplots(nrows=2)
ax[0].plot(x,yf)
ax[1].plot(x,RespNf)
plt.show()
