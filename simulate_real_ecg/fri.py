import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go

from ECG.ecg import read_ecg
import os
import numpy as np 
from scipy.signal import find_peaks

file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "a01.dat")
ra = read_ecg(file,0,1000)

app = dash.Dash()

app.layout = html.Div([
    html.H1("ECG a01.dat",style={
            'textAlign': 'center',
        }),
    dcc.Graph(id="graph"),
    dcc.RangeSlider(
        id='my-range-slider',
        min=0,
        max=1000,
        step=1,
        value=[50, 150]
    ),
    html.H1(id='output-container-range-slider'),
    html.H1(id='bpm')
])


@app.callback(
    dash.dependencies.Output('output-container-range-slider', 'children'),
    [dash.dependencies.Input('my-range-slider', 'value')])
def update_output(value):
    return f'Time range: [{value[0]/100} , {value[1]/100}] secs'

@app.callback(
    dash.dependencies.Output('bpm', 'children'),
    [dash.dependencies.Input('my-range-slider', 'value')])
def bpm(s):
    global ra
    y=ra[s[0]:s[1]]
    dist = (s[1]-s[0])/100
    peaks, _ = find_peaks(y,height=150 )
    num_peaks = len(peaks)
    if num_peaks ==1:
        return "Nyquist limit violation please select a wider range."
    else:
        return f'bpm : {num_peaks*60/dist}'

@app.callback(
    Output('graph', 'figure'),
    [Input('my-range-slider', 'value')])
def update_fig(s):
    traces = []
    global ra
    traces.append(go.Scatter(
            x=np.arange(s[0],s[1])/100,
            y=ra[s[0]:s[1]],
        ))

    return {
            'data': traces,
            'layout': go.Layout(
                xaxis={'title': 'Time (Sec)'},
                yaxis={'title': 'A/D units', 'range': [-200,350]},
                hovermode='closest'
            )
        }
if __name__ == '__main__':
    app.run_server(debug=True)
