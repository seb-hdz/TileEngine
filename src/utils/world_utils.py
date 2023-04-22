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
    detail_level: int,  # octaves
    persistence: float,  # amplitude
    lacunarity: float,  # frequency
    base: int = 0,  # base height
):
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
    conditions: list[float] | tuple[float, float, float],
    colors: list[tuple[int, int, int]],
):
    # Create a matrix of zeros with extra channels for RGB
    color_world = np.zeros(world_data.shape + (3,), dtype="uint8")

    for x in range(world_data.shape[0]):
        for y in range(world_data.shape[1]):
            # An index value is calculated
            # This is how colors are assigned to the world data
            index = multi_compare(world_data[x][y], conditions)
            color_world[x][y] = colors[index]

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
