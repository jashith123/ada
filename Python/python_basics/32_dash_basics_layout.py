"""
32_dash_basics_layout.py

Dash Overview:
- Dash is a Python framework for building analytical web applications.
- Built on top of Flask, Plotly.js, and React.js.

Key Concepts:
- Layout: Describes what the app looks like (using Dash HTML/Core Components).
- Callbacks: Describes the interactivity (logic).

Dependencies:
pip install dash dash-bootstrap-components pandas
"""

try:
    from dash import Dash, html, dcc
    import dash_bootstrap_components as dbc
    import plotly.express as px
    import pandas as pd
except ImportError:
    print("Dash libraries not found. Install: pip install dash dash-bootstrap-components pandas")
    exit()

# Initialize the App
# Using a Bootstrap theme for easy styling
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Sample Data for visualization
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# --- Layout ---
# The layout is a tree of components.

# 1. Navigation Bar (using Bootstrap components)
navbar = dbc.NavbarSimple(
    brand="My Dashboard",
    brand_href="#",
    color="primary",
    dark=True,
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="#")),
        dbc.NavItem(dbc.NavLink("Reports", href="#")),
    ]
)

# 2. Data Cards (using Bootstrap Cards)
card_content = [
    dbc.CardHeader("Total Sales"),
    dbc.CardBody(
        [
            html.H5("15,000 Units", class_name="card-title"),
            html.P("Increased by 5% since last month.", class_name="card-text"),
        ]
    ),
]

row_cards = dbc.Row(
    [
        dbc.Col(dbc.Card(card_content, color="info", inverse=True)),
        dbc.Col(dbc.Card(card_content, color="success", inverse=True)),
        dbc.Col(dbc.Card(card_content, color="warning", inverse=True)),
    ],
    className="mb-4", # Margin bottom
)

# 3. Main Layout Assembly
app.layout = dbc.Container(
    [
        navbar,
        html.Br(),
        html.H1("Sales Overview", className="text-center"),
        html.Hr(),
        
        # Insert Cards
        row_cards,
        
        # Insert Graph
        dbc.Row(
            [
                dbc.Col(dcc.Graph(id='example-graph', figure=fig), width=12)
            ]
        )
    ],
    fluid=True # Use full width
)

if __name__ == '__main__':
    print("Running Dash App... Open http://127.0.0.1:8050/ in your browser.")
    app.run_server(debug=True)
