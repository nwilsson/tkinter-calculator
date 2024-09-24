import tkinter
from tkinter import ttk
import sv_ttk

# Number submission
def submit_number(number):
    # Get the current text in the entry widget
    current_text = entry_a.get()
    entry_a.delete(0, tkinter.END)  # Clear the entry first
    entry_a.insert(0, current_text + str(number))  # Insert the new text

def calculate():
    try:
        # Get the current expression from the entry widget
        expression = entry_a.get()
        # Evaluate the expression and display the result
        result = eval(expression)
        entry_a.delete(0, tkinter.END)  # Clear the entry first
        entry_a.insert(0, str(result))  # Insert the result
    except Exception as e:
        entry_a.delete(0, tkinter.END)  # Clear the entry first
        entry_a.insert(0, "Error")  # Display an error message

def clear():
    entry_a.delete(0,tkinter.END)

# Main window setup
window = tkinter.Tk()

def key_handler(event):
        try:
        # Get the current expression from the entry widget
            expression = entry_a.get()
        # Evaluate the expression and display the result
            result = eval(expression)
            entry_a.delete(0, tkinter.END)  # Clear the entry first
            entry_a.insert(0, str(result))  # Insert the result
        except Exception as e:
            entry_a.delete(0, tkinter.END)  # Clear the entry first
            entry_a.insert(0, "Error")  # Display an error message

window.bind("<Return>", key_handler, calculate)

# Entry widget for displaying the numbers
entry_a = tkinter.Entry(window)
entry_a.grid(row=0, column=1, pady=2, columnspan=3)

# Number buttons with correct lambda expressions
one = ttk.Button(window, text="1", command=lambda: submit_number(1))
one.grid(row=1, column=1, pady=2)
two = ttk.Button(window, text="2", command=lambda: submit_number(2))
two.grid(row=1, column=2, pady=2)
three = ttk.Button(window, text="3", command=lambda: submit_number(3))
three.grid(row=1, column=3, pady=2)
four = ttk.Button(window, text="4", command=lambda: submit_number(4))
four.grid(row=2, column=1, pady=2)
five = ttk.Button(window, text="5", command=lambda: submit_number(5))
five.grid(row=2, column=2, pady=2)
six = ttk.Button(window, text="6", command=lambda: submit_number(6))
six.grid(row=2, column=3, pady=2)
seven = ttk.Button(window, text="7", command=lambda: submit_number(7))
seven.grid(row=3, column=1, pady=2)
eight = ttk.Button(window, text="8", command=lambda: submit_number(8))
eight.grid(row=3, column=2, pady=2)
nine = ttk.Button(window, text="9", command=lambda: submit_number(9))
nine.grid(row=3, column=3, pady=2)
zero = ttk.Button(window, text="0", command=lambda: submit_number(0))
zero.grid(row=4, column=2, pady=2)

# Arithmetic operation buttons
plus_button = ttk.Button(window, text="+", command=lambda: submit_number("+"))
plus_button.grid(row=1, column=4, pady=5)
minus_button = ttk.Button(window, text="-", command=lambda: submit_number("-"))
minus_button.grid(row=2, column=4, pady=5)
times_button = ttk.Button(window, text="*", command=lambda: submit_number("*"))
times_button.grid(row=3, column=4, pady=5)
divide_button = ttk.Button(window, text="/", command=lambda: submit_number("/"))
divide_button.grid(row=4, column=4, pady=5)
clear_button = ttk.Button(window, text="C", command=clear)
clear_button.grid(row=4, column=3, pady=5)

# Submit button to execute the calculation
submit_button = ttk.Button(window, text="=", command=calculate)
submit_button.grid(row=0, column=4, pady=5)

# Apply the theme
sv_ttk.set_theme("light")

window.title("My Calculator")
window.mainloop()
