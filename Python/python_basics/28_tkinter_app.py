"""
28_tkinter_app.py

Building Applications with Tkinter:
- Using 'Grid' geometry manager for structured layout.
- Creating a functional 'Simple Calculator'.
"""

import tkinter as tk

def calculate():
    try:
        val1 = float(entry_num1.get())
        val2 = float(entry_num2.get())
        operation = variable.get()
        
        if operation == "+":
            res = val1 + val2
        elif operation == "-":
            res = val1 - val2
        elif operation == "*":
            res = val1 * val2
        elif operation == "/":
            if val2 == 0:
                res = "Error"
            else:
                res = val1 / val2
        
        lbl_result.config(text=f"Result: {res}", fg="green")
    except ValueError:
        lbl_result.config(text="Invalid Input", fg="red")

root = tk.Tk()
root.title("Simple Calculator")

# --- Layout using Grid Manager ---
# Row 0: Title
tk.Label(root, text="Simple Calculator", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

# Row 1: Number 1
tk.Label(root, text="Number 1:").grid(row=1, column=0, padx=5, sticky="e")
entry_num1 = tk.Entry(root)
entry_num1.grid(row=1, column=1, padx=5)

# Row 2: Number 2
tk.Label(root, text="Number 2:").grid(row=2, column=0, padx=5, sticky="e")
entry_num2 = tk.Entry(root)
entry_num2.grid(row=2, column=1, padx=5)

# Row 3: Operation Dropdown
tk.Label(root, text="Operation:").grid(row=3, column=0, padx=5, sticky="e")
options = ["+", "-", "*", "/"]
variable = tk.StringVar(root)
variable.set("+") # default value
opt_menu = tk.OptionMenu(root, variable, *options)
opt_menu.grid(row=3, column=1, sticky="w", padx=5)

# Row 4: Calculate Button
btn_calc = tk.Button(root, text="Calculate", command=calculate)
btn_calc.grid(row=4, column=0, columnspan=2, pady=10)

# Row 5: Result Display
lbl_result = tk.Label(root, text="Result: -", font=("Arial", 12))
lbl_result.grid(row=5, column=0, columnspan=2, pady=5)

print("Running Calculator App... (Close window to finish)")
root.mainloop()
