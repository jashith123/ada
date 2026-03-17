"""
34_dash_callbacks_basic.py

Dash Callbacks:
- Functions that become automatically called by Dash whenever an input component's property changes.
- Decorator: @app.callback
- Concepts: Input, Output, State.
"""

from dash import Dash, html, dcc, Input, Output, State, ctx

app = Dash(__name__)

app.layout = html.Div([
    html.H2("Callback Demonstrations"),
    
    # --- Example 1: Basic Input/Output ---
    html.Div([
        html.H4("1. Basic Callback (Live Update)"),
        dcc.Input(id='my-input', value='initial value', type='text'),
        html.Div(id='my-output')
    ], style={'border': '1px solid black', 'padding': '10px'}),
    
    html.Br(),

    # --- Example 2: Button & State ---
    html.Div([
        html.H4("2. Callback with State (Button Trigger)"),
        dcc.Input(id='input-state', type='text', value='Type here...'),
        html.Button('Submit', id='submit-button', n_clicks=0),
        html.Div(id='output-state')
    ], style={'border': '1px solid black', 'padding': '10px'}),

    html.Br(),

    # --- Example 3: Multiple Inputs ---
    html.Div([
        html.H4("3. Multiple Inputs"),
        html.Label("X:"),
        dcc.Input(id='input-x', type='number', value=5),
        html.Label("Y:"),
        dcc.Input(id='input-y', type='number', value=2),
        html.Div(id='output-math')
    ], style={'border': '1px solid black', 'padding': '10px'}),
])


# Callback 1: Updates immediately when input changes
@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return f'You entered: {input_value}'


# Callback 2: Updates ONLY when button is clicked
# 'State' allows reading the value without triggering the callback
@app.callback(
    Output('output-state', 'children'),
    Input('submit-button', 'n_clicks'),
    State('input-state', 'value')
)
def update_output(n_clicks, input_value):
    if n_clicks > 0:
        return f'The button has been clicked {n_clicks} times, Input was: "{input_value}"'
    return 'Click the button to submit.'


# Callback 3: Multiple Inputs
@app.callback(
    Output('output-math', 'children'),
    Input('input-x', 'value'),
    Input('input-y', 'value')
)
def add_numbers(x, y):
    if x is None or y is None:
        return "Enter values"
    return f"Sum: {x} + {y} = {x + y}"


if __name__ == '__main__':
    print("Running Basic Callbacks... Open http://127.0.0.1:8050/")
    app.run_server(debug=True)
