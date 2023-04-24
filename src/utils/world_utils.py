import numpy as np
import noise
from PIL import Image
from os.path import join
from os import mkdir

from ..constants import MAP_TILES_DIR, MAP_PREVIEW_DIR

from .common_utils import multi_compare
from .datetime_utils import get_current_datetime


def generate_world_data(
    world_shape: tuple[int, int],
    scale: float,
    detail_level: int,
    persistence: float,
    lacunarity: float,
    base: int = 0,
) -> np.ndarray:
    """
    Generates a 2D array (matrix) of Perlin noise values representing a world terrain.

    Args:
    - world_shape: A tuple of integers representing the dimensions of the world in pixels.
    - scale: A float representing the scale of the Perlin noise.
    - detail_level: An integer representing the number of octaves used to generate the Perlin noise.
    - persistence: A float representing the amplitude of the Perlin noise.
    - lacunarity: A float representing the frequency of the Perlin noise.
    - base: An integer representing the base height of the terrain.

    Returns:
    - A 2D numpy array (matrix) of floats representing the terrain of the world.
    """
    # Create a matrix of zeros
    world = np.zeros(world_shape)

    # Fill the matrix with Perlin noise
    for x in range(world_shape[0]):
        for y in range(world_shape[1]):
            world[x][y] = noise.pnoise2(
                y / scale,
                x / scale,
                octaves=detail_level,
                persistence=persistence,
                lacunarity=lacunarity,
                base=base,
            )

    return world


def colorize_world_data(
    world_data: np.ndarray,
    conditions: list[float],
    colors: list[tuple[int, int, int]],
    default_color: tuple[int, int, int] = (0, 0, 0),
) -> np.ndarray:
    """
    Takes in a 2D array of world data and applies colors to the values based on a list of conditions.

    Args:
    - world_data: A 2D numpy array of floats representing the terrain of the world.
    - conditions: A list of floats representing the threshold values to be compared against the `world_data`.
    - colors: A list of tuples representing the RGB colors to be assigned to the world data based on the threshold values.

    Returns:
    - A 3D numpy array of RGB values representing the terrain of the world with colors applied based on the threshold values.
    """
    if len(conditions) != len(colors):
        raise ValueError(
            f"Length of conditions ({len(conditions)}) must equal length of colors ({len(colors)})."
        )

    # Create a matrix of zeros with extra channels for RGB
    color_world = np.zeros(world_data.shape + (3,), dtype="uint8")

    for x in range(world_data.shape[0]):
        for y in range(world_data.shape[1]):
            # An index value is calculated
            # This is how colors are assigned to the world data
            index = multi_compare(world_data[x][y], conditions)

            if index is not None:
                color_world[x][y] = colors[index]
            else:
                color_world[x][y] = default_color

    return color_world


def save_as_image(world_data: np.ndarray, file_name: str = "", save: bool = True):
    if file_name == "":
        file_name = f"world_{get_current_datetime()}.png"

    # Create an image from the colored world data
    image = Image.fromarray(world_data, "RGB")

    if save:
        # Check for a directory for map previews
        # If not, one is created
        try:
            mkdir(MAP_PREVIEW_DIR)
        except FileExistsError:
            pass

        image.save(join(MAP_PREVIEW_DIR, f"{file_name}.png"))

    return image


def save_as_tiles(world_data: np.ndarray, conditions: list[float], file_name: str = ""):
    # Create a matrix of zeros
    tiles = np.zeros(world_data.shape, dtype="uint8")

    for x in range(world_data.shape[0]):
        for y in range(world_data.shape[1]):
            # A tile value is calculated
            tile_value = multi_compare(world_data[x][y], conditions)
            tiles[x][y] = tile_value

    # Check for a directory for map tiles
    # If not, one is created
    try:
        mkdir(MAP_TILES_DIR)
    except FileExistsError:
        pass

    if file_name == "":
        file_name = f"world_{get_current_datetime()}.tiles"

    np.savetxt(
        join(MAP_TILES_DIR, f"{file_name}.tiles"), tiles, delimiter=" ", fmt="%d"
    )
