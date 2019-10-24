from ECG.ecg import read_ecg
import os
import matplotlib.pyplot as plt
import numpy as np
# from scipy.signal import find_peaks

plt.style.use('ggplot')

events = 400
file  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"a01.dat")
y = read_ecg(file,0,events)

condition = y>150
a = np.argwhere(condition)
a = a.reshape(len(a),)
groups = np.split(a, np.argwhere(np.diff(a) != 1)[:,0] + 1)
pl = []
for i in range(len(groups)):
    id = np.argmax(y[groups[i]])
    pl = np.append(pl,groups[i][id])
pl = pl.astype(int)
print(pl)
# peak_loc = peak_loc.astype(int)
# print(peak_loc)
# for i in range(1,len(a)):
#     a[i-1]

# peaks, _ = find_peaks(y, height=(100,None))

plt.plot(y,label= "ECG")
plt.plot(pl, y[pl],label="peaks",marker='x', linestyle='dashed')
plt.title(f"ECG for {events} samples or {events/100} secs ")
plt.xlabel('Time (10 ms)')
plt.ylabel("200 A/D units per millivolt")
plt.legend()
plt.show()