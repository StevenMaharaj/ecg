from ECG.ecg import read_ecg,find_peaks
import numpy as np
import time
import os
import numpy as np

import plotly.offline as pyo
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from collections import deque

file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "a01.dat")
Y = deque(maxlen=500)
offest = 0
# read first window
window = 500
Y.append(read_ecg(file,offest,window))
# p = find_peaks(Y)
print(find_peaks(list(Y)[0],height=150))
# print(list(Y)[0][-1])
# print(p.values)