# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css',
    'http://localhost:5555/styles/frame-styles-template.css',
    'http://localhost:5555/styles/light-theme.css'
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF', 'className': 'test'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                'paper_bgcolor': 'transparent',
                'plot_bgcolor': 'transparent'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)