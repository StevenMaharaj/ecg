from ECG.ecg import read_ecg,make_df_summary,make_ecg_res_summary
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')

events = 1000000
eventsr = 4*events
file  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"../a01.dat")
filer  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"../a01r.dat")

df = make_ecg_res_summary(file,filer,0,events)
print(df.head())

# sns.pairplot(df)

corr_matrix = df.corr()
corr_matrix_sq = df.corr()**2
sns.heatmap(corr_matrix,annot=True)
plt.title("R")
plt.figure()
sns.heatmap(corr_matrix_sq,annot=True)
plt.title("R^2")
plt.show()
