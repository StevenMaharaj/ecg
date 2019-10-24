from ECG.ecg import read_ecg
import os
import matplotlib.pyplot as plt
plt.style.use('ggplot')

events = 300
file  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"a01.dat")
y = read_ecg(file,0,events)

plt.plot(y)
plt.title(f"ECG for {events} samples or {events/100} secs ")
plt.xlabel('Time (10 ms)')
plt.ylabel("200 A/D units per millivolt")
plt.savefig("figs/sample_ecg",dpi=250)
plt.show()