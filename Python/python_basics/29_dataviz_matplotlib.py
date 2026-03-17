"""
29_dataviz_matplotlib.py

Data Visualization with Matplotlib:
- Foundation library for plotting in Python.
- Topics: Line, Bar, Scatter, Histogram, Customization, Subplots.

Install: pip install matplotlib
"""

try:
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError:
    print("Matplotlib/NumPy missing. Install: pip install matplotlib numpy")
    exit()

# Data Generation
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# 1. Basic Line Plot
plt.figure(figsize=(8, 4))
plt.plot(x, y1, label='Sin(x)', color='blue', linestyle='--')
plt.plot(x, y2, label='Cos(x)', color='red', linewidth=2)
plt.title("Sine vs Cosine")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.savefig("plot_line.png") # Save plot to file
print("Saved plot_line.png")
# plt.show() # Uncomment to view window

# 2. Subplots (Multiple Axes)
fig, ax = plt.subplots(2, 2, figsize=(10, 8))

# Top Left: Scatter
ax[0, 0].scatter(np.random.rand(50), np.random.rand(50), color='green')
ax[0, 0].set_title("Random Scatter")

# Top Right: Bar Chart
categories = ['A', 'B', 'C']
values = [10, 24, 36]
ax[0, 1].bar(categories, values, color='orange')
ax[0, 1].set_title("Category Values")

# Bottom Left: Histogram
data = np.random.randn(1000)
ax[1, 0].hist(data, bins=30, color='purple', alpha=0.7)
ax[1, 0].set_title("Histogram (Normal Dist)")

# Bottom Right: Multi-line
ax[1, 1].plot(x, y1 * x)
ax[1, 1].set_title("Damped Sine")

plt.tight_layout() # Adjusts spacing
plt.savefig("plot_subplots.png")
print("Saved plot_subplots.png")
