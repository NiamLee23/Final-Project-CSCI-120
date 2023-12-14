import tkinter as tk
from tkinter import ttk
import final_project
import random

root = tk.Tk()
root.title("Guessing Game")

lower_bound = 0
upper_bound = 0
correctValue = ''
rounds = 0
guess = 0

# Define functions for input and output
def get_input():
    global correctValue
    global lower_bound
    global upper_bound
    global rounds
    global guess
    
    if correctValue == '': #Generates starting correct value
        lower_bound = int(entry_lower_bound.get())
        upper_bound = int(entry_upper_bound.get())
        guess = int(entry_guess_number.get())   
        correctValue = random.choice(range(lower_bound, upper_bound + 1))
        
        rounds += 1
        response = final_project.guess_game(lower_bound, upper_bound, guess, correctValue)
        update_t_chart(rounds, guess, response)
   
    else: #Continues game
        print('here')
        rounds += 1
        guess = int(entry_guess_number.get())
        response = final_project.guess_game(lower_bound, upper_bound, guess, correctValue)
        update_t_chart(rounds, guess, response)

#Inserts new/updated row on t-chart
def update_t_chart(round_num, guess, response):
    t_chart.insert("", "end", text=str(guess), values=(response, round_num))

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
button_get_input.grid(row=5, column=0, columnspan=2)


label_guess_number = tk.Label(root, text="Enter A Number:")
label_guess_number.grid(row=3, column=0)

entry_guess_number = tk.Entry(root)
entry_guess_number.grid(row=3, column=1)

#Styles the t-chart
style = ttk.Style(root)
style.theme_use('clam')
style.configure("Treeview.Heading", background='PowderBlue')

# Create a t-chart for displaying guesses and responses
t_chart = ttk.Treeview(root, columns=("Response", "Round"))
t_chart.heading("#0", text="Guess")
t_chart.heading("#1", text="Response")
t_chart.heading("#2", text="Round")

t_chart.column("#0", stretch=tk.YES)
t_chart.column("#1", stretch=tk.YES)
t_chart.column("#2", stretch=tk.YES)

t_chart.grid(row=7, column=0, columnspan=3, sticky='nsew')

# Start the main loop
root.mainloop()
