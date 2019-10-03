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


app = dash.Dash()
crash_free = 0
app.layout = html.Div([
    html.H1(id="live-update-text"),
    dcc.Interval(id="interval-component",
                 interval=2*1000,
                 n_intervals = 0)
])

@app.callback(Output('live-update-text', 'children'),
              [Input('interval-component', 'n_intervals')])

def update_layout(n):
    return f"Crash free for {n}"

if __name__ == "__main__":
    app.run_server()