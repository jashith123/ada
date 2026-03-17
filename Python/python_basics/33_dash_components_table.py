"""
33_dash_components_table.py

Dash Components:
- HTML Components (dash.html): Div, H1, P, etc.
- Core Components (dash.dcc): Graph, Dropdown, Slider, Input, etc.
- Dash Table (dash.dash_table): Interactive data tables.

Dependencies:
pip install dash pandas
"""

from dash import Dash, html, dcc, dash_table
import pandas as pd
import plotly.express as px

app = Dash(__name__)

# Sample Data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')

# --- Layout ---
app.layout = html.Div([
    html.H1("Dash Core Components & Tables Gallery"),
    
    # 1. Core Components
    html.Div([
        html.Label("Dropdown:"),
        dcc.Dropdown(
            options=['New York City', 'Montreal', 'San Francisco'],
            value='Montreal'
        ),
        
        html.Br(),
        html.Label("Slider:"),
        dcc.Slider(min=0, max=10, step=1, value=5),
        
        html.Br(),
        html.Label("Checklist:"),
        dcc.Checklist(
            options=['New York', 'London', 'Tokyo'],
            value=['New York', 'Tokyo']
        ),
    ], style={'padding': 20, 'border': '1px solid #ddd'}),
    
    html.Br(),
    
    # 2. Dash Table
    html.H3("Interactive Data Table"),
    dash_table.DataTable(
        data=df.head(10).to_dict('records'),
        columns=[{'name': i, 'id': i} for i in df.columns],
        
        # Table Styling & Features
        style_cell={'textAlign': 'left'},
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'
        },
        sort_action='native', # Enable sorting
        filter_action='native', # Enable filtering
        page_size=5           # Pagination
    )
])

if __name__ == '__main__':
    print("Running Components Demo... Open http://127.0.0.1:8050/")
    app.run_server(debug=True)
