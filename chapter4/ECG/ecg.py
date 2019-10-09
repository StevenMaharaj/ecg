from scipy.signal import find_peaks
from ECG.ecg_sig import butter_highpass_filter,butter_lowpass_filter
import numpy as np
import pandas as pd

def read_ecg(file_name,offset, events):   # extract the ECG data
    """Reads a .dat ecg file

    Parameters:
    file_name (str): file name to be read
    offest (int): number of sample to the right we begin to read the data
    events (int): window of samples

    Returns:
    numpy.ndarray : array of ECG data

   """
    A=open(file_name,'rb')                # returns data in A/D units
    A.seek(offset*2)
    y=[]
    i = events
    while (i):
        D=A.read(2)
        N=int.from_bytes(D,byteorder='little',signed=True)
        y.append(N)
        i -=1
    return np.array(y)


def make_df_summary(file_name,offset, events):
    """
    Creates a summary of of and EGC

    Parameters:
    file_name (str): file name to be read
    offest (int): number of sample to the right we begin to read the data
    events (int): window of samples

    Returns:
    pandas.DataFrame : dataframe of features 
    [Offset  Amplitude  T (sec)    DT DAmplitude]
    

    
    """

    Offset, dict_heights = find_peaks(read_ecg(file_name,0,events), height=(100,None))
    Amplitude = dict_heights['peak_heights'] 
    T = Offset/100
    DT = np.append(0,np.diff(T))
    DAmplitude = np.append(0,np.diff(Amplitude))
    return(pd.DataFrame({"Offset":Offset,
                "Amplitude":Amplitude,
                "T (sec)":T,
                "DT":DT,
                "DAmplitude":DAmplitude}))
    
def make_ecg_res_summary(file_name_ecg,file_name_resp,offset, events):
    """
    Creates a summary of of and EGC

    Parameters:
    file_name_ecg (str): file name of ecg data to be read
    file_name_resp (str): file name of ecg data to be read
    offest (int): number of sample to the right we begin to read the data
    events (int): window of samples

    Returns:
    pandas.DataFrame : dataframe of features 
    [Offset  Amplitude  T (sec)    DT DAmplitude respA  respA_filtered]
    
    
    
    """
    eventsr = 4*events
    
    yr = read_ecg(file_name_resp,offset,eventsr)

    respA = yr[1::4]
    fps =100 # sampling frequency
    Filtered = butter_highpass_filter(respA,0.1,fps)
    Filtered = butter_lowpass_filter(Filtered,0.2,fps)

    df = make_df_summary(file_name_ecg,0,events)
    offset = df["Offset"].values
    df["respA"] = respA[offset]
    df["respA_filtered"] = Filtered[offset]

    return df