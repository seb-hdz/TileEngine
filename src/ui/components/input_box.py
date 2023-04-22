import tkinter as tk


class InputBox(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Detail level label and input
        detail_level_label = tk.Label(self, text="Detail Level:")
        detail_level_label.grid(row=0, column=0)
        self.detail_level_input = tk.Spinbox(self, from_=1, to=100, increment=1)
        self.detail_level_input.grid(row=1, column=0)

        # Base label and input
        base_label = tk.Label(self, text="Base:")
        base_label.grid(row=2, column=0)
        self.base_input = tk.Spinbox(self, from_=0, to=100, increment=1)
        self.base_input.grid(row=3, column=0)

        # Lacunarity label and input
        lacunarity_label = tk.Label(self, text="Lacunarity:")
        lacunarity_label.grid(row=0, column=1)
        self.lacunarity_input = tk.Spinbox(self, from_=0.0, to=100, increment=0.1)
        self.lacunarity_input.grid(row=1, column=1)

        # Persistence label and input
        persistence_label = tk.Label(self, text="Persistence:")
        persistence_label.grid(row=2, column=1)
        self.persistence_input = tk.Spinbox(self, from_=0, to=1, increment=0.01)
        self.persistence_input.grid(row=3, column=1)
