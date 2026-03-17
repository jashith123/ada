"""
35_dash_advanced_callbacks.py

Advanced Callbacks:
- Multiple Outputs: Returning multiple values from a single callback.
- Chained Callbacks: One dropdown updates the options of another.
"""

from dash import Dash, html, dcc, Input, Output

app = Dash(__name__)

# Data for Chained Callback
all_options = {
    'America': ['New York City', 'San Francisco', 'Cincinnati'],
    'Canada': ['Montreal', 'Toronto', 'Ottawa']
}

app.layout = html.Div([
    html.H2("Advanced Callbacks"),
    
    # --- Chained Callbacks Section ---
    html.Div([
        html.H4("Chained Callbacks (Dependent Dropdowns)"),
        
        html.Label("Select Country:"),
        dcc.Dropdown(
            id='countries-dropdown',
            options=[{'label': k, 'value': k} for k in all_options.keys()],
            value='America'
        ),
        
        html.Br(),
        
        html.Label("Select City (Updates based on Country):"),
        dcc.Dropdown(id='cities-dropdown'),
        
        html.Br(),
        html.Div(id='display-selected-values')
    ], style={'border': '1px solid blue', 'padding': '15px'}),
    
    html.Br(),
    
    # --- Multiple Outputs Section ---
    html.Div([
        html.H4("Multiple Outputs"),
        dcc.Input(id='num-input', type='number', value=2),
        html.Div([
            html.P(id='square-output'),
            html.P(id='cube-output'),
            html.P(id='log-output')
        ])
    ], style={'border': '1px solid green', 'padding': '15px'})
])


# --- Chained Callbacks Logic ---

# 1. Update City options based on Country selection
@app.callback(
    Output('cities-dropdown', 'options'),
    Input('countries-dropdown', 'value'))
def set_cities_options(selected_country):
    return [{'label': i, 'value': i} for i in all_options[selected_country]]

# 2. Set a default value for City when options change
@app.callback(
    Output('cities-dropdown', 'value'),
    Input('cities-dropdown', 'options'))
def set_cities_value(available_options):
    return available_options[0]['value']

# 3. Display the final selection
@app.callback(
    Output('display-selected-values', 'children'),
    Input('countries-dropdown', 'value'),
    Input('cities-dropdown', 'value'))
def set_display_children(selected_country, selected_city):
    return f'{selected_city} is a city in {selected_country}'


# --- Multiple Outputs Logic ---
@app.callback(
    Output('square-output', 'children'),
    Output('cube-output', 'children'),
    Output('log-output', 'children'),
    Input('num-input', 'value')
)
def math_operations(number):
    if number is None:
        return "N/A", "N/A", "N/A"
    
    sq = number ** 2
    cube = number ** 3
    import math
    try:
        lg = math.log(number)
    except:
        lg = "Err"
        
    return f"Square: {sq}", f"Cube: {cube}", f"Log: {lg:.2f}"


if __name__ == '__main__':
    print("Running Advanced Callbacks... Open http://127.0.0.1:8050/")
    app.run_server(debug=True)
