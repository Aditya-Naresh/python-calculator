import tkinter as tk

# Create app window
win = tk.Tk()

# Screen Size of App Window
win.geometry("312x324")

# Disable resizing
win.resizable()

# App name
win.title("Calculator")

# Functions for calculator
input_value = ""

# Initialize StringVar
display_text = tk.StringVar()


# Function to update the input
def click_button_action(item):
    global input_value
    input_value = input_value + str(item)
    display_text.set(input_value)


# Function to clear the display
def clear_button_action():
    global input_value
    input_value = " "
    display_text.set(" ")


# function to calculate input values
def equal_button_action():
    global input_value
    result = str(eval(input_value))
    display_text.set(result)
    input_value = ""


# Create a frame for the display field
input_frame = tk.Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                       highlightthickness=2)
input_frame.pack(side=tk.TOP)

# Entry Widget inside the frame
input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=display_text, width=50, bg='#eee', bd=0,
                       justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

win.mainloop()
