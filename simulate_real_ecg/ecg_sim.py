from ECG.ecg import read_ecg
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


file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "a01.dat")
window_len = 5*100
window = np.zeros(window_len)
offset = 0

wl = np.zeros((500, window_len))
while offset < 100:
    window = np.roll(window, -1)
    window[-1] = read_ecg(file, offset, 1)[0]
    wl[offset, :] = window
    time.sleep(0.01)
    print(window)
    offset += 1


data = [go.Scatter(x=np.arange(window_len),
                   y=wl[50, :],
                   mode='lines')]

layout = go.Layout(title="Hello",
                   xaxis={'title': "my x"},
                   hovermode='closest')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='scatter.html')


app = dash.Dash()

app.layout = html.Div([dcc.Graph(id='line',
                                 figure={'data': [go.Scatter(x=np.arange(window_len),
                                                             y=wl[50, :],
                                                             mode='lines')],
                                         'layout':go.Layout(title='my scatter')}
                                 )])


if __name__ == "__main__":
    app.run_server()
