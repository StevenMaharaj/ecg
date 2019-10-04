import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go

from ECG.ecg import read_ecg
import os
import numpy as np 

file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "a01.dat")
ra = read_ecg(file,0,1000)

app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(id="graph"),
    dcc.RangeSlider(
        id='my-range-slider',
        min=0,
        max=1000,
        step=1,
        value=[50, 150]
    ),
    html.Div(id='output-container-range-slider')
])


@app.callback(
    dash.dependencies.Output('output-container-range-slider', 'children'),
    [dash.dependencies.Input('my-range-slider', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)



@app.callback(
    Output('graph', 'figure'),
    [Input('my-range-slider', 'value')])
def update_fig(s):
    traces = []
    global ra
    traces.append(go.Scatter(
            x=np.arange(s[0],s[1]),
            y=ra[s[0]:s[1]],
        ))

    return {
            'data': traces,
            'layout': go.Layout(
                xaxis={'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy', 'range': [-200,350]},
                hovermode='closest'
            )
        }
if __name__ == '__main__':
    app.run_server(debug=True)
