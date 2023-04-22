import tkinter as tk

root = tk.Tk()

# Create a label for the text input field
label = tk.Label(root, text="Enter your name:")
label.pack()

# Create a text input field
text_input = tk.Entry(root)
text_input.pack()

root.mainloop()
