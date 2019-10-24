from ECG.ecg import read_ecg,make_df_summary,make_ecg_res_summary
import os
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

events = 100000
eventsr = 4*events
file  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"../a01.dat")
filer  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"../a01r.dat")

df = make_ecg_res_summary(file,filer,0,events)
print(df.head())

plt.figure(figsize=(12,8))
plt.scatter(x=df["DT"],y=df["respA_filtered"],alpha=0.6)
plt.show()


# dfp = df[df["respA_filtered"]>0]
# dfn = df[df["respA_filtered"]<0]

# plt.figure(figsize=(12,8))
# plt.scatter(x=dfp["DT"],y=dfp["respA_filtered"],alpha=0.6)
# plt.scatter(x=dfn["DT"],y=dfn["respA_filtered"],alpha=0.6)
# plt.show()