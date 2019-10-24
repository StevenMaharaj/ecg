from ECG.ecg import read_ecg
import os
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

plt.style.use('ggplot')

events = 800
file  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"a01.dat")
y = read_ecg(file,0,events)

peaks, _ = find_peaks(y, height=(100,None))

plt.plot(y,label= "ECG")
plt.plot(peaks, y[peaks],label="peaks",marker='x', linestyle='dashed')
plt.title(f"ECG for {events} samples or {events/100} secs ")
plt.xlabel('Time (10 ms)')
plt.ylabel("200 A/D units per millivolt")
plt.legend()
plt.show()