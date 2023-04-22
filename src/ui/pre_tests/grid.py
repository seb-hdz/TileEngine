import tkinter as tk
from PIL import Image, ImageTk


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("My App")

        # Control Panel
        self.control_panel = tk.LabelFrame(self.master, text="Conditions")
        self.control_panel.grid(row=0, column=0)

        # Slider: Condition 1
        self.scale1 = tk.Scale(
            self.control_panel, orient=tk.HORIZONTAL, from_=-1, to=1, resolution=0.01
        )
        self.scale1.pack()

        # Slider: Condition 2
        self.scale2 = tk.Scale(
            self.control_panel, orient=tk.HORIZONTAL, from_=-1, to=1, resolution=0.01
        )
        self.scale2.pack()

        # Slider: Condition 3
        self.scale3 = tk.Scale(
            self.control_panel, orient=tk.HORIZONTAL, from_=-1, to=1, resolution=0.01
        )
        self.scale3.pack()

        # Input Boxes
        self.input_box = tk.Frame(self.master)
        self.input_box.grid(row=1, column=0)

        # Detail level label and input
        detail_level_label = tk.Label(self.input_box, text="Detail Level:")
        detail_level_label.grid(row=0, column=0)
        self.detail_level_input = tk.Spinbox(
            self.input_box, from_=0, to=100, increment=1
        )
        self.detail_level_input.grid(row=1, column=0)

        # Base label and input
        base_label = tk.Label(self.input_box, text="Base:")
        base_label.grid(row=2, column=0)
        self.base_input = tk.Spinbox(self.input_box, from_=0, to=100, increment=1)
        self.base_input.grid(row=3, column=0)

        # Lacunarity label and input
        lacunarity_label = tk.Label(self.input_box, text="Lacunarity:")
        lacunarity_label.grid(row=0, column=1)
        self.lacunarity_input = tk.Spinbox(
            self.input_box, from_=0.0, to=100, increment=0.1
        )
        self.lacunarity_input.grid(row=1, column=1)

        # Persistence label and input
        persistence_label = tk.Label(self.input_box, text="Persistence:")
        persistence_label.grid(row=2, column=1)
        self.persistence_input = tk.Spinbox(
            self.input_box, from_=0, to=100, increment=0.01
        )
        self.persistence_input.grid(row=3, column=1)

        # Scale label and input
        scale_label = tk.Label(self.master, text="Scale:")
        scale_label.grid(row=2, column=0)
        self.spin5 = tk.Spinbox(self.master, from_=0.0, to=100, increment=0.1)
        self.spin5.grid(row=3, column=0)

        # Button: Save to image
        self.save_to_image_button = tk.Button(self.master, text="Save to Image")
        self.save_to_image_button.grid(row=4, column=0)

        # Button: Save to tiles
        self.save_to_tiles_button = tk.Button(self.master, text="Save to Tiles")
        self.save_to_tiles_button.grid(row=5, column=0)

        # Image Preview
        self.image_preview = tk.LabelFrame(self.master, text="Image Preview")
        self.image_preview.grid(row=0, column=1, rowspan=6)

        # Load the preview image using PIL
        image = Image.open("preview.png")

        self.canvas = tk.Canvas(self.image_preview, width=512, height=512)
        self.canvas.pack()

        self.photo = ImageTk.PhotoImage(image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        # Run the main loop
        self.master.mainloop()


root = tk.Tk()
app = App(root)
