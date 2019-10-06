import os
from ECG.ecg import read_ecg
file  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"a01.dat")
filer  =  os.path.join(os.path.dirname(os.path.realpath(__file__)),"a01r.dat")

A=open(file,'rb')
# y = []
with open(file,'rb') as f:
    y = f.read(10)

print(y)
# N = [int.from_bytes(y[2*i:2*(i+2)],byteorder='little',signed=True) for i in range(len(y)/2)]

print(read_ecg(file,0,5))