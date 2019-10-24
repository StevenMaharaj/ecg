from ECG.ecg import read_ecg
import os
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from scipy.signal import find_peaks
import numpy as np
import pandas as pd

events = 800
file  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"a01.dat")
# file = "a01.dat"
y = read_ecg(file,0,events)

Offset, dict_heights = find_peaks(y, height=(100,None))
Amplitude = dict_heights['peak_heights'] 
T = Offset/100
DT = np.append(0,np.diff(T))
df_summary = pd.DataFrame({"Offset":Offset,
             "Amplitude":Amplitude,
             "T (sec)":T,
             "DT":DT})
print(df_summary)