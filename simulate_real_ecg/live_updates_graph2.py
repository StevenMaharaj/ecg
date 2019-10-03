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
app = dash.Dash()
wl = np.zeros((500, window_len))
while offset <400:
    window = np.roll(window, -1)
    window[-1] = read_ecg(file, offset, 1)[0]
    wl[offset, :] = window
    time.sleep(0.1)
    
    # print(window)
    offset += 1


# app.layout = html.Div([dcc.Graph(id='line',
#                                  figure={'data': [go.Scatter(x=np.arange(window_len),
#                                                              y=window,
#                                                              mode='lines')],
#                                          'layout':go.Layout(title='my scatter')}
#                                  )])


app.layout = html.Div(
    html.Div([
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1*1000, # in milliseconds
            n_intervals=0
        )
    ])
)

@app.callback(Output('live-update-graph', 'figure'),
              [Input('interval-component', 'n_intervals')])
def update_graph_live(n):
    data = {
        'x':[],
        "y":[]
    }

    file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "a01.dat")
    window_len = 5*100
    window = np.zeros(window_len)
    offset = 0
    wl = np.zeros((500, window_len))
    while offset <400:
        window = np.roll(window, -1)
        window[-1] = read_ecg(file, offset, 1)[0]
        wl[offset, :] = window
        time.sleep(0.1)
        
        # print(window)
        offset += 1
    data['x'] = np.arange(window_len)
    data['y'] = wl[n, :]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['x'], y=data['y'],
                        mode='lines',
                        name='lines'))
    return fig

if __name__ == "__main__":
    app.run_server()