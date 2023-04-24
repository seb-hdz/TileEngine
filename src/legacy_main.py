from os import mkdir
import random

from .constants import *

from .utils.world_utils import (
    generate_world_data,
    colorize_world_data,
    save_as_image,
    save_as_tiles,
)


def main():
    # Creating the dump directory
    try:
        mkdir(DUMP_DIR)
    except FileExistsError:
        pass

    # Setting the array of conditions
    conditions = [-0.05, 0.0, 1.0]

    # Setting the array of colors
    colors = [
        (230, 182, 200),  # This is a pastel pink color
        (182, 200, 230),  # This is a pastel blue color
        (200, 230, 182),  # This is a pastel green color
    ]

    # Defining world's parameters
    world_shape = (1024, 1024)
    scale = 100.0
    detail_level = 6
    persistence = 0.5
    lacunarity = 2.0
    base = random.randint(5, 100)

    # Generating the world data
    world_data = generate_world_data(
        world_shape=world_shape,
        scale=scale,
        detail_level=detail_level,
        persistence=persistence,
        lacunarity=lacunarity,
        base=base,
    )

    # Coloring the world
    color_world = colorize_world_data(
        world_data=world_data, conditions=conditions, colors=colors
    )

    # Saving the world data
    # As an image (colorized data)
    save_as_image(color_world)

    # As tile data (raw data)
    save_as_tiles(world_data=world_data, conditions=conditions)


if __name__ == "__main__":
    main()
