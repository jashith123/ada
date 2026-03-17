"""
31_dataviz_interactive_advanced.py

Advanced Visualization:
- Interactive Plots with Plotly.
- Time Series Visualization basics.
- Brief overview of Geospatial/Network concepts.

Install: pip install plotly
"""

try:
    import plotly.graph_objects as go
    import plotly.express as px
    import pandas as pd
    import numpy as np
except ImportError:
    print("Plotly missing. Install: pip install plotly")
    exit()

# --- 1. Interactive Visualization with Plotly ---
# Plotly creates HTML files that are interactive (zoom, hover, etc.)

print("--- Creating Plotly Interactive Plot ---")
# Mock data
df = pd.DataFrame({
    'Fruit': ['Apples', 'Oranges', 'Bananas', 'Grapes'],
    'Amount': [4, 1, 2, 5],
    'City': ['SF', 'SF', 'SF', 'Montreal']
})

# Bar Chart
fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group',
             title="Interactive Fruit Sales (Plotly)")

# Save to HTML file
fig.write_html("plot_interactive.html")
print("Saved plot_interactive.html - Open this file in a browser to interact.")


# --- 2. Visualizing Time Series ---
print("\n--- Time Series Visualization ---")
# Generating dates
dates = pd.date_range(start='2024-01-01', periods=100)
values = np.cumsum(np.random.randn(100)) # Random walk

ts_df = pd.DataFrame({'Date': dates, 'Value': values})

# Using Plotly for Time Series (built-in slider/range selector)
fig_ts = px.line(ts_df, x='Date', y='Value', title='Time Series with Range Slider')
fig_ts.update_xaxes(rangeslider_visible=True)
fig_ts.write_html("plot_timeseries.html")
print("Saved plot_timeseries.html")


# --- 3. Advanced Concepts Overview (Code structure) ---

# Geospatial:
# Typically uses libraries like 'folium' or 'geopandas' or 'plotly.choropleth'.
# Example (Conceptual):
# px.choropleth(df_geo, locations="iso_alpha", color="lifeExp", hover_name="country", ...)

# Network Graphs:
# Typically uses 'networkx'.
# Example (Conceptual):
# import networkx as nx
# G = nx.Graph()
# G.add_edge(1, 2)
# nx.draw(G, with_labels=True)
