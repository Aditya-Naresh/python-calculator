import tkinter as tk

# Create app window
win = tk.Tk()

# Screen Size of App Window
win.geometry("360x324")

# Disable resizing
# win.resizable(False, False)

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


# A frame for the display field
input_frame = tk.Frame(win, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                       highlightthickness=2)
input_frame.pack(side=tk.TOP)

# Entry Widget inside the frame
input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=display_text, width=35, bg='#eee', bd=0,
                       justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Frame for buttons
button_frame = tk.Frame(win, width=312, height=272.5, bg="grey")
button_frame.pack()

# 1st row
clear_button = tk.Button(button_frame, text="C", fg="black", width=40, height=3, bd=0, bg="#eee", cursor="hand2",
                         command=lambda: clear_button_action())
clear_button.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

divide_button = tk.Button(button_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                          command=lambda: click_button_action("/"))
divide_button.grid(row=0, column=3, padx=1, pady=1)

# 2nd row
button_7 = tk.Button(button_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                     command=lambda: click_button_action("7"))
button_8 = tk.Button(button_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                     command=lambda: click_button_action("8"))
button_9 = tk.Button(button_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                     command=lambda: click_button_action("9"))
multiplication_button = tk.Button(button_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee",
                                  cursor="hand2",
                                  command=lambda: click_button_action("*"))

button_7.grid(row=1, column=0, padx=1, pady=1)
button_8.grid(row=1, column=1, padx=1, pady=1)
button_9.grid(row=1, column=2, padx=1, pady=1)
multiplication_button.grid(row=1, column=3, padx=1, pady=1)

# 3rd row
button_4 = tk.Button(button_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                     command=lambda: click_button_action("4"))
button_5 = tk.Button(button_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                     command=lambda: click_button_action("5"))
button_6 = tk.Button(button_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                     command=lambda: click_button_action("6"))
subtraction_button = tk.Button(button_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee",
                               cursor="hand2",
                               command=lambda: click_button_action("-"))

button_4.grid(row=2, column=0, padx=1, pady=1)
button_5.grid(row=2, column=1, padx=1, pady=1)
button_6.grid(row=2, column=2, padx=1, pady=1)
subtraction_button.grid(row=2, column=3, padx=1, pady=1)

# 4th row
button_1 = tk.Button(button_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                     command=lambda: click_button_action("1"))
button_2 = tk.Button(button_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                     command=lambda: click_button_action("2"))
button_3 = tk.Button(button_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                     command=lambda: click_button_action("3"))
plus_button = tk.Button(button_frame, text="+", fg="black", width=10, height=7, bd=0, bg="#eee",
                        cursor="hand2",
                        command=lambda: click_button_action("+"))

button_1.grid(row=3, column=0, padx=1, pady=1)
button_2.grid(row=3, column=1, padx=1, pady=1)
button_3.grid(row=3, column=2, padx=1, pady=1)
plus_button.grid(row=3, column=3, padx=1, pady=1, rowspan=2)

# 4th row
button_0 = tk.Button(button_frame, text="0", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                     command=lambda: click_button_action("0"))
button_point = tk.Button(button_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                         command=lambda: click_button_action("."))
button_equal = tk.Button(button_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                         command=lambda: equal_button_action())
button_0.grid(row=4, column=0, padx=1, pady=1)
button_point.grid(row=4, column=1, padx=1, pady=1)
button_equal.grid(row=4, column=2, padx=1, pady=1)
win.mainloop()
