import dash
from dash.dependencies import Output, Input, State
import dash_core_components as dcc
import dash_html_components as html

import plotly
import plotly.offline as pyo
import plotly.graph_objects as go

from collections import deque
import random

X = deque(maxlen=5*100)
Y = deque(maxlen=5*100)

X.append(1)
Y.append(1)

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id="live-graph", animate=True),
    dcc.Interval(
        id='graph-update',
        interval=100,
        n_intervals=0
    )
])


@app.callback(Output('live-graph', 'figure'),
              [Input('graph-update', 'n_intervals')])
def update_graph(n):
    global X
    global Y
    X.append(X[-1]+1)
    Y.append(Y[-1]+Y[-1]*random.uniform(-0.1, 0.1))

    data = go.Scatter(
        x=list(X),
        y=list(Y),
        name="scatter",
        mode='lines'
    )
    return {'data': [data], "layout": go.Layout(xaxis=dict(range=[min(X), max(X)]),
                                                yaxis=dict(range=[min(Y), max(Y)]))}



if __name__ == '__main__':
    app.run_server(debug=True)