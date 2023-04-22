import tkinter as tk
import tkinter.colorchooser as colorchooser


class ColorPicker(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.color_button = tk.Button(
            self, text="Choose Color", command=self.choose_color
        )
        self.color_button.pack()

    def choose_color(self):
        color = colorchooser.askcolor()
        print(
            color
        )  # prints a tuple of RGB values and the chosen color in hexadecimal format


if __name__ == "__main__":
    root = tk.Tk()
    color_picker = ColorPicker(root)
    color_picker.pack()
    root.mainloop()
