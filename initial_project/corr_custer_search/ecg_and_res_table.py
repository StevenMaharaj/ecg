from ECG.ecg import read_ecg,make_df_summary,make_ecg_res_summary
from ECG.ecg_sig import butter_highpass_filter,butter_lowpass_filter
import os
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

events = 6000
eventsr = 4*events
file  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"../a01.dat")
filer  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"../a01r.dat")
y = read_ecg(file,0,events)
yr = read_ecg(filer,0,eventsr)

respA = yr[1::4]

fps = 100

Filtered = butter_highpass_filter(respA,0.1,fps)
Filtered = butter_lowpass_filter(Filtered,0.2,fps)



plt.figure(figsize=(12,8))
plt.subplot(211)
plt.plot(range(len(respA)),respA)
plt.title('respA')
plt.subplot(212)
plt.plot(range(len(Filtered)),Filtered)
plt.title('filtered respA')
plt.hlines(y=0,xmin = 0,xmax=events)
plt.show()




df = make_df_summary(file,0,events)
print(df.head())

offset = df["Offset"].values
df["respA"] = respA[offset]
df["respA_filtered"] = Filtered[offset]
print(df.head())



#############

# Test function in ECG package make_ecg_res_summary

df1 = make_ecg_res_summary(file,filer,0,events)
print(df1.head())