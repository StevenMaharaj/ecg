import matplotlib.pyplot as plt
plt.style.use('ggplot')
from ECG.ecg import read_ecg
import os
import numpy as np
from scipy import fft

events = 700000
file  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"a01.dat")
# file = "a01.dat"
y = read_ecg(file,0,events)

plt.plot(np.abs(fft(y)))
plt.title(f"FFT of ECG for {events} samples or {events*100} Hz ")
plt.xlabel('Freq (100 Hz)')
plt.ylabel("|Y(freq)|")
plt.show()