from ECG.ecg import read_ecg
import os
import matplotlib.pyplot as plt
plt.style.use('ggplot')

events = 800
file  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"a01r.dat")
yr = read_ecg(file,0,events)


fig,ax = plt.subplots(nrows=4,ncols = 1)
for i in range(3):
    ax[i].plot(yr[i::4],"x")

plt.tight_layout()
plt.show()

# plt.plot(y)
# plt.title(f"ECG for {events} samples or {events/100} secs ")
# plt.xlabel('Time (10 ms)')
# plt.ylabel("200 A/D units per millivolt")
# plt.show()