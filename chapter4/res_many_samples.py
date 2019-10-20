import os
from ECG.ecg import read_ecg
file  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"a01.dat")
filer  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"a01r.dat")
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np


events = 4*10000
eventsr =4*events

T = 1/100

yr = read_ecg(filer,0,eventsr)

RespN = yr[2::4]
x = np.arange(len(RespN))/100



fig, ax = plt.subplots(nrows=4)


for i in range(4):
    ax[i].plot(x[10000*(i):10000*(i+1)],RespN[10000*(i):10000*(i+1)],label = "RespN")
    ax[i].hlines(0,min(x[10000*(i):10000*(i+1)]),max(x[10000*(i):10000*(i+1)]),label = "Zero line")


plt.xlabel("Time (Sec)")
plt.legend(loc="lower left")
plt.tight_layout()
path = os.path.dirname(os.path.realpath(__file__))

plt.savefig(os.path.join(path,"fig/many_sample_resp"),dpi = 250)

plt.show()
