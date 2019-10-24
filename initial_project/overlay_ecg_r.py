from ECG.ecg import read_ecg
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import fft
plt.style.use('ggplot')

events = 6000
eventsr = 4*events
file  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"a01.dat")
filer  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"a01r.dat")
y = read_ecg(file,0,events)
yr = read_ecg(filer,0,eventsr)

plt.plot(y)
plt.title(f"ECG for {events} samples or {events/100} secs ")
plt.xlabel('Time (10 ms)')
plt.ylabel("200 A/D units per millivolt")
plt.plot(yr[1::4])
plt.figure()
plt.plot(np.abs(fft(yr)))
plt.show()