import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Guessing Game")

# Define functions for input and output
def get_input():
    lower_bound = int(entry_lower_bound.get())
    upper_bound = int(entry_upper_bound.get())
    return lower_bound, upper_bound

def set_output(text):
    label_output.configure(text=text)

# Define labels and input fields
label_lower_bound = tk.Label(root, text="Lower Bound:")
label_lower_bound.grid(row=0, column=0)

entry_lower_bound = tk.Entry(root)
entry_lower_bound.grid(row=0, column=1)

label_upper_bound = tk.Label(root, text="Upper Bound:")
label_upper_bound.grid(row=1, column=0)

entry_upper_bound = tk.Entry(root)
entry_upper_bound.grid(row=1, column=1)

# Define button for getting input
button_get_input = tk.Button(root, text='enter', command=get_input)
button_get_input.grid(row=2, column=0, columnspan=2)

# Define label for output
label_output = tk.Label(root, text="")
label_output.grid(row=3, column=0, columnspan=2)

# Create a t-chart for displaying guesses and responses
t_chart = ttk.Treeview(root, columns=("Guess", "Response"))
t_chart.heading("#0", text="Round")
t_chart.heading("#1", text="Guess")
t_chart.heading("#2", text="Response")
t_chart.grid(row=4, column=0, columnspan=2)

# Start the main loop
root.mainloop()

