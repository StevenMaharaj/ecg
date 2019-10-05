import numpy as np
from ECG.ecg import read_ecg
import os
import matplotlib.pyplot as plt
plt.style.use('ggplot')

filer  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"a01r.dat")


events = 5000
eventsr = 4*events
path = os.path.dirname(os.path.realpath(__file__))
# file  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"a01.dat")
filer  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"a01r.dat")
# y = read_ecg(file,0,events)
yr = read_ecg(filer,0,eventsr)

RespC = yr[::4]
RespA = yr[1::4]
RespN = yr[2::4]
Sp02 = yr[3::4]

fig, ax = plt.subplots(nrows=4)

x  = np.arange(len(RespC))/100
ax[0].plot(x,RespC)

ax[1].plot(x,RespA)
ax[2].plot(x,RespN)
ax[3].plot(x,Sp02)

ax[0].title.set_text('Chest plethysmography')
ax[1].title.set_text('Abdominal plethysmography')
ax[2].title.set_text('Nasal thermistors')
ax[3].title.set_text('SpO2')

plt.xlabel('Time (sec)')

plt.tight_layout()
plt.savefig(os.path.join(path,"fig/sample_resp"),dpi = 250)

plt.show()




