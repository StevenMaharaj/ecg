from ECG.ecg import read_ecg
import matplotlib.pyplot as plt
from scipy.signal import medfilt
# plt.style.use('ggplot')
events = 800
# file  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"a01.dat")
file = "a01.dat"
y = read_ecg(file,0,events)
    
fig, axs = plt.subplots(5, 2)
count = 41
for j in range(2):
    for i in range(5):
        fil = medfilt(y,kernel_size=count)
        # fil = medfilt(fil,kernel_size=41)
        fil = [fil[i:i+20].mean() for i in range(len(fil))]
        ax = axs[i,j]
        ax.plot(fil)
        ax.set_title(f'kernel_size={count}')
        count += 2
plt.tight_layout()
# plt.savefig("figs/group_means_by_id")
plt.show(fig)
events = 800
# file  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"a01.dat")
file = "a01.dat"
y = read_ecg(file,0,events)
    
fig, axs = plt.subplots(5, 2)
count = 41
for j in range(2):
    for i in range(5):
        fil = medfilt(y,kernel_size=count)
        ax = axs[i,j]
        ax.plot(fil)
        ax.set_title(f'kernel_size={count}')
        count += 2
plt.tight_layout()
# plt.savefig("figs/group_means_by_id")
plt.show(fig)