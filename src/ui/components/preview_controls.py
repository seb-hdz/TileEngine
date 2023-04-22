import tkinter as tk


class PreviewControls(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        name_label = tk.Label(self, text="World name:")
        name_label.grid(row=0, column=0, columnspan=2)
        self.name_input = tk.Entry(self)
        self.name_input.grid(row=1, column=0, columnspan=2)

        # Width label and input
        width_label = tk.Label(self, text="Width:")
        width_label.grid(row=2, column=0)
        self.width_input = tk.Spinbox(self, from_=8, to=1024, increment=1)
        self.width_input.grid(row=3, column=0)

        # Height label and input
        height_label = tk.Label(self, text="Height:")
        height_label.grid(row=2, column=1)
        self.height_input = tk.Spinbox(self, from_=8, to=1024, increment=1)
        self.height_input.grid(row=3, column=1)

    def get_world_name(self):
        return self.name_input.get()

    def get_width(self):
        return int(self.width_input.get())

    def get_height(self):
        return int(self.height_input.get())

    def get_dimensions(self):
        return self.get_width(), self.get_height()
