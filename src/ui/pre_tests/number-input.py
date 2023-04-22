import tkinter as tk

root = tk.Tk()

# Create a label for the number input field
label = tk.Label(root, text="Enter a number:")
label.pack()

# Create a number input field
number_input = tk.Spinbox(root, from_=0, to=100)
number_input.pack()


def get_input_value():
    value = number_input.get()
    print("The user entered:", value)


# Create a button to get the input value
button = tk.Button(root, text="Get input value", command=get_input_value)
button.pack()

root.mainloop()
