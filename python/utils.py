"""
This code defines some utilities used across the codebase.
"""

# Standard imports.
from pathlib import Path

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
