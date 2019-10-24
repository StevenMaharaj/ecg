import numpy as np
import pandas as pd
from scipy import signal, fft
from scipy.signal import find_peaks
import matplotlib.pyplot as plt


def sine_generator(fs, sinefreq, duration):
    T = duration
    nsamples = fs * T
    w = 2. * np.pi * sinefreq
    t_sine = np.linspace(0, T, nsamples, endpoint=False)
    y_sine = np.sin(w * t_sine)
    result = pd.DataFrame({'data' : y_sine} ,index=t_sine)
    return result

def rand_generator(fs, duration):
    T = duration
    nsamples = fs * T
    t_val = np.linspace(0, T, nsamples, endpoint=False)
    y_val = np.random.uniform(size=nsamples)
    result = pd.DataFrame({'data' : y_val} ,index=t_val)
    return result

def butter_highpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = signal.filtfilt(b, a, data)
    return y

def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = signal.filtfilt(b, a, data)
    return y

def band_pass_filter(y,low=0.1,high=0.2,fps = 100):
    """
    Applies a butterworth band pass filter.

    Parameters:
    y (numpy array): input to be filtered
    low (float): lower cut off frequency
    high (float): higher cut off frequency
    fps (int) : sampling rate

    Returns:
    numpy array: filtered data
    """
    y = butter_highpass_filter(y,low,fps)
    y = butter_lowpass_filter(y,high,fps)
    return y
