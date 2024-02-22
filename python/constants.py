"""
This code defines the various paths used throughout the codebase.
"""

# Standard imports.
from pathlib import Path

# Path objects.
PATH_OBJ_TO_HERE = Path(__file__).resolve()
PATH_OBJ_TO_BASE = PATH_OBJ_TO_HERE.parent.parent
PATH_OBJ_TO_TEX = PATH_OBJ_TO_BASE/"tex"
PATH_OBJ_TO_POEMS = PATH_OBJ_TO_BASE/"poems"
PATH_OBJ_TO_PROSE = PATH_OBJ_TO_BASE/"prose"

# Paths.
PATH_TO_ARTICLE_TEMPLATE = str(PATH_OBJ_TO_TEX/"article_template.tex")
PATH_TO_PROSE_PACKAGE_CODE = str(PATH_OBJ_TO_TEX/"prose_package_code.tex")

# Markers.
PACKAGES_MARKER = "#PACKAGES"
TITLE_MARKER = "#TITLE"
CONTENT_MARKER = "#CONTENT"

# Extensions.
TEX_EXT = ".tex"
PDF_EXT = ".pdf"
HPML_EXT = ".hpml"

# Other constants.
DEFAULT_LATEX_COMMAND = "lualatex"
DEFAULT_STEM = "main"
TEMP_STEM = "temp"
