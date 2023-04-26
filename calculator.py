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
