"""
This code defines the various paths used throughout the codebase.
"""

# Standard imports.
from pathlib import Path

# Path objects.
PATH_OBJ_TO_HERE = Path(__file__).resolve()
PATH_OBJ_TO_BASE = PATH_OBJ_TO_HERE.parent.parent
PATH_OBJ_TO_TEX = PATH_OBJ_TO_BASE/"tex"
PATH_OBJ_TO_POEMS = PATH_OBJ_TO_TEX/"poems"
PATH_OBJ_TO_STORIES = PATH_OBJ_TO_TEX/"stories"
PATH_OBJ_TO_SCAFFOLDING = PATH_OBJ_TO_TEX/"scaffolding"

# Paths.
PATH_TO_PACKAGES = str(PATH_OBJ_TO_SCAFFOLDING/"packages.tex")

# Markers.
PACKAGES_MARKER = "#PACKAGES"
TITLE_MARKER = "#TITLE"
CONTENT_MARKER = "#CONTENT"

# Other constants.
DEFAULT_LATEX_COMMAND = "lualatex"
DEFAULT_STEM = "main"
TEX_EXT = ".tex"
PDF_EXT = ".pdf"
