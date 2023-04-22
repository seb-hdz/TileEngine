import tkinter as tk


class SliderWindow:
    def __init__(self):
        # Create a Tkinter window
        self.root = tk.Tk()

        # Create a Scale widget with a range from 0 to 100
        self.slider = tk.Scale(self.root, from_=0, to=100, orient="horizontal")
        self.slider.pack()

        # Add a button to print the current value of the slider
        button = tk.Button(self.root, text="Print Value", command=self.print_value)
        button.pack()

        # Run the Tkinter event loop
        self.root.mainloop()

    def print_value(self):
        # Print the current value of the slider
        print(self.slider.get())


if __name__ == "__main__":
    slider_window = SliderWindow()
