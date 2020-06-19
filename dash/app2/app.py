# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


# POC - Let's just hard code these for now
platform_port = 5555
dash_port = 8051

app_name = 'Dash App 2'

external_stylesheets = [
    'https://codepen.io/chriddyp/pen/bWLwgP.css'
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.Div(
        id='navbar',
        children=f'Home > {app_name}',
        style={
        'color': 'white',
        'backgroundColor': '#119dff',
        'padding': '2px'
        }
    ),

    html.H1(children=app_name),

    html.Div(children='''
        Dash: This app was written for Browser, OpenFin behaviors Injected!
    '''),

    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': i, 'value': i} for i in ['USA', 'Canada']],
        value='USA'
    ),

    dcc.Graph(
        id='example-graph'
    )
])

@app.callback(
    Output('example-graph', 'figure'),
    [Input('country-dropdown', 'value')])
def update_figure(selected_country):
    data = {
        'USA': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'New York'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'line', 'name': 'Los Angeles'},
        ],
        'Canada': [
                {'x': [1, 2, 3], 'y': [3, 1, 3], 'type': 'line', 'name': u'Montréal'},
                {'x': [1, 2, 3], 'y': [5, 2, 4], 'type': 'line', 'name': 'Toronto'},
        ]
    }
    return {
        'data': data[selected_country],
        'layout': {
            'title': 'Dash Data Visualization',
            'paper_bgcolor': 'transparent',
            'plot_bgcolor': 'transparent'
        }
    }

if __name__ == '__main__':
    app.run_server(debug=True, port=dash_port)