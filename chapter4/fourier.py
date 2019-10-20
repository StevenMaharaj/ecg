import os
from ECG.ecg import read_ecg
file  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"a01.dat")
filer  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"a01r.dat")
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import numpy as np
import scipy.fftpack
from ECG.ecg_sig import band_pass_filter


events = 4*10000
eventsr =4*events

N = events 
T = 1/100

yr = read_ecg(filer,0,eventsr)

RespN = yr[2::4]
RespNf = band_pass_filter(RespN)
x = np.linspace(0.0, N*T, N)

yf = scipy.fftpack.fft(RespN)
yf_filtered = scipy.fftpack.fft(RespNf)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

fig, ax = plt.subplots(ncols=2)
plt.subplot(ax[0])
plt.plot(xf, 2.0/N * np.abs(yf[:N//2]))
plt.xlim(0,0.8)
plt.xlabel("frequency (Hz)")
plt.title("fft of RespN")

plt.subplot(ax[1])
plt.plot(xf, 2.0/N * np.abs(yf_filtered[:N//2]))
plt.xlim(0,0.8)
plt.xlabel("frequency (Hz)")
plt.title("fft of filtered RespN")

plt.tight_layout()
plt.savefig('fig/fft',dpi = 250)
plt.show()