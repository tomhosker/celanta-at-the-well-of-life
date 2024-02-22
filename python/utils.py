"""
This code defines some utilities used across the codebase.
"""

# Standard imports.
from pathlib import Path

# Local imports.
from .constants import PATH_TO_PROSE_PACKAGE_CODE

#############
# UTILITIES #
#############

def get_contents(path_to):
    """ Return, as a string, the contents of a file at a given path. """
    with open(path_to, "r") as file_to_read:
        result = file_to_read.read()
    return result

def get_title(path_to_content):
    """ Get the title of a given article from its path. """
    result = Path(path_to_content).stem
    result = result.replace("_", " ")
    return result

def get_prose_package_code():
    """ Return the contents of the file. """
    return get_contents(PATH_TO_PROSE_PACKAGE_CODE)
