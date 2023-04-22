import tkinter as tk


class ControlPanel(tk.LabelFrame):
    def __init__(self, master):
        super().__init__(master, text="Conditions")

        # Slider: Condition 1
        self.scale1 = tk.Scale(
            self,
            orient=tk.HORIZONTAL,
            from_=-1,
            to=1,
            resolution=0.001,
        )
        self.scale1.pack()

        # Slider: Condition 2
        self.scale2 = tk.Scale(
            self,
            orient=tk.HORIZONTAL,
            from_=-1,
            to=1,
            resolution=0.001,
        )
        self.scale2.pack()

        # Slider: Condition 3
        self.scale3 = tk.Scale(
            self,
            orient=tk.HORIZONTAL,
            from_=-1,
            to=1,
            resolution=0.001,
        )
        self.scale3.pack()

    def get_values(self):
        return self.scale1.get(), self.scale2.get(), self.scale3.get()
