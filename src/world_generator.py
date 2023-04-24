import tkinter as tk
import numpy as np

from .ui.components.control_panel import ControlPanel
from .ui.components.input_box import InputBox
from .ui.components.image_preview import ImagePreview
from .ui.components.preview_controls import PreviewControls

from .utils.world_utils import (
    generate_world_data,
    colorize_world_data,
    save_as_image,
    save_as_tiles,
)


class MainWindow:
    def __init__(self):
        # Variables
        self.world_data: np.ndarray = None
        self.color_world: np.ndarray = None
        self.world_name: str = ""

        # Create a Tkinter window
        self.root = tk.Tk()
        self.root.title("My App")

        # Control panel
        self.control_panel = ControlPanel(self.root)
        self.control_panel.grid(row=0, column=0)

        # Input box
        self.input_box = InputBox(self.root)
        self.input_box.grid(row=1, column=0)

        # Scale label and input
        scale_label = tk.Label(self.root, text="Scale:")
        scale_label.grid(row=2, column=0)
        self.scale_input = tk.Spinbox(
            self.root,
            from_=1.0,
            to=100.0,
            increment=0.1,
        )
        self.scale_input.grid(row=3, column=0)

        # ! This should be deleted
        # TODO: The image should update automatically
        self.generate_button = tk.Button(
            self.root, text="Generate / Save", command=self.generate
        )
        self.generate_button.grid(row=4, column=0)

        # Button: Save to image
        self.save_to_image_button = tk.Button(
            self.root, text="Save to Image", command=self.save_to_image
        )
        self.save_to_image_button.grid(row=5, column=0)

        # Button: Save to tiles
        self.save_to_tiles_button = tk.Button(
            self.root, text="Save to Tiles", command=self.save_to_tiles
        )
        self.save_to_tiles_button.grid(row=6, column=0)

        # Image preview controls
        self.preview_controls = PreviewControls(self.root)
        self.preview_controls.grid(row=0, column=1)

        # Run the main loop
        self.root.mainloop()

    def generate(self):
        # Set the conditions array
        conditions = self.control_panel.get_values()

        # Setting the array of colors
        # TODO: This should also be set by user input
        colors = [
            (182, 200, 230),  # This is a pastel blue color
            (230, 182, 200),  # This is a pastel pink color
            (200, 230, 182),  # This is a pastel green color
        ]

        # Defining world's parameters
        world_shape = self.preview_controls.get_dimensions()
        scale = float(self.scale_input.get())
        detail_level = int(self.input_box.detail_level_input.get())
        persistence = float(self.input_box.persistence_input.get())
        lacunarity = float(self.input_box.lacunarity_input.get())
        base = int(self.input_box.base_input.get())

        # Getting the world name
        self.world_name = self.preview_controls.get_world_name()

        # Generating the world data
        self.world_data = generate_world_data(
            world_shape=world_shape,
            scale=scale,
            detail_level=detail_level,
            persistence=persistence,
            lacunarity=lacunarity,
            base=base,
        )

        # Coloring the world
        self.color_world = colorize_world_data(self.world_data, conditions, colors)

        preview = save_as_image(self.color_world, save=False)

        self.image_preview = ImagePreview(self.root, preview)
        self.image_preview.grid(row=1, column=1, rowspan=7)

    def save_to_image(self):
        if self.world_data is None:
            return

        save_as_image(self.color_world, file_name=self.world_name)

    def save_to_tiles(self):
        if self.world_data is None:
            return

        conditions = self.control_panel.get_values()
        save_as_tiles(self.world_data, conditions, file_name=self.world_name)


if __name__ == "__main__":
    main_window = MainWindow()
