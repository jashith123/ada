"""
27_tkinter_basics.py

GUI Programming with Tkinter:
- Standard Python interface to the Tk GUI toolkit.
- Widgets: Label, Button, Entry, Text, Frame, etc.
- Event Handling: Binding functions to user actions.
"""

import tkinter as tk
from tkinter import messagebox

# 1. Create the Main Window
root = tk.Tk()
root.title("My First GUI")
root.geometry("400x300") # Width x Height

# 2. Widgets
# Label
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16))
label.pack(pady=10) # pack() is a geometry manager (simple stacking)

# Entry (Input field)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# Function to handle button click
def on_button_click():
    name = entry.get() # Get text from entry widget
    if name:
        label.config(text=f"Welcome, {name}!")
    else:
        messagebox.showwarning("Input Error", "Please enter a name.")

# Button
btn = tk.Button(root, text="Submit", command=on_button_click, bg="lightblue")
btn.pack(pady=10)

# 3. Geometry Manager: Place (Absolute positioning)
# Places a label at exact x,y coordinates
abs_label = tk.Label(root, text="I am at (50, 200)", fg="gray")
abs_label.place(x=50, y=200)

# 4. Run the Event Loop
# This keeps the window open and listening for events
print("Running Tkinter window... (Close the window to stop script)")
root.mainloop()
