import os
from ECG.ecg import make_df_summary
import pandas as pd
import numpy as np

file  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"a01.dat")
df = make_df_summary(file,0,500)

# print(df)

dfpretty = pd.DataFrame({
    "R-peak location (sec)":df["T (sec)"],
    "R-peak height (A/D units)":df["Amplitude"].astype(int),
    "R-R intveral":df["DT"],
    "R-peak height change (A/D units)":df["DAmplitude"],

})


print(dfpretty)
path = os.path.dirname(os.path.realpath(__file__))

dfpretty.to_csv(os.path.join(path,"table/features.csv"),index=False)