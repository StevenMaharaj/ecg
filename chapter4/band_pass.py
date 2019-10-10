# last minute idea
from ECG.ecg import read_ecg
from ECG.ecg_sig import butter_highpass_filter,butter_lowpass_filter,band_pass_filter
import os
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

events = 20000
eventsr = 4*events
file  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"a01.dat")
filer  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"a01r.dat")
y = read_ecg(file,0,events)
yr = read_ecg(filer,0,eventsr)

respN = yr[2::4]

fps = 100


Filteredr = band_pass_filter(respN)


Filterede = band_pass_filter(y)

plt.figure(figsize=(12,8))
plt.subplot(211)
plt.plot(range(len(Filteredr)),Filteredr)
plt.title('filtered respA')
plt.hlines(y=0,xmin = 0,xmax=events)

plt.figure(figsize=(12,8))
plt.subplot(212)
plt.plot(range(len(Filterede)),Filterede)
plt.title('filtered ecg')
plt.hlines(y=0,xmin = 0,xmax=events)
plt.show()
