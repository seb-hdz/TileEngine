from os import path

# Directories
SRC_DIR = path.dirname(path.abspath(__file__))
ROOT_DIR = path.dirname(SRC_DIR)
DUMP_DIR = path.join(ROOT_DIR, "dumps")

MAP_PREVIEW_DIR = path.join(DUMP_DIR, "previews")
MAP_TILES_DIR = path.join(DUMP_DIR, "tiles")
