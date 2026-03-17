"""
30_dataviz_seaborn.py

Data Visualization with Seaborn:
- Built on top of Matplotlib.
- High-level interface for drawing attractive statistical graphics.
- Great for visualizing relationships and correlations.

Install: pip install seaborn
"""

try:
    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
except ImportError:
    print("Seaborn/Pandas missing. Install: pip install seaborn pandas")
    exit()

# Load built-in dataset 'tips'
# If internet access is blocked, we mock a dataframe
try:
    df = sns.load_dataset('tips')
except:
    print("Could not load 'tips' dataset from web, using mock data.")
    df = pd.DataFrame({
        'total_bill': np.random.uniform(10, 50, 100),
        'tip': np.random.uniform(1, 10, 100),
        'sex': np.random.choice(['Male', 'Female'], 100),
        'time': np.random.choice(['Lunch', 'Dinner'], 100),
        'size': np.random.randint(1, 6, 100)
    })

print("Dataset Head:")
print(df.head())

# 1. Visualizing Relationships (Scatter with Regression info)
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='total_bill', y='tip', hue='time', style='sex')
plt.title("Total Bill vs Tip (by Time and Sex)")
plt.savefig("plot_seaborn_scatter.png")
print("Saved plot_seaborn_scatter.png")

# 2. Correlation Heatmap
plt.figure(figsize=(6, 5))
# Select only numeric columns for correlation matrix
numeric_df = df.select_dtypes(include=[np.number])
corr = numeric_df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.savefig("plot_seaborn_heatmap.png")
print("Saved plot_seaborn_heatmap.png")

# 3. Pairplot (View all pairwise relationships)
# Creates a grid of Axes such that each variable in data will by shared
# across the y-axes across a single row and x-axes across a single column.
sns.pairplot(df, hue='sex')
plt.savefig("plot_seaborn_pairplot.png")
print("Saved plot_seaborn_pairplot.png")
