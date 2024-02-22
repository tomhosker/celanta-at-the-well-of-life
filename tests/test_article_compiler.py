"""
This code tests the ArticleCompiler class.
"""

# Standard imports.
from pathlib import Path

# Source imports.
from python.article_compiler import ArticleCompiler
from python.constants import (
    PATH_OBJ_TO_POEMS,
    PATH_OBJ_TO_PROSE,
    TEMP_STEM,
    PDF_EXT
)

# Local constants.
PATH_TO_POEM_SOURCE = str(PATH_OBJ_TO_POEMS/"test.hpml")
PATH_TO_PROSE_SOURCE = str(PATH_OBJ_TO_PROSE/"test.tex")

###########
# TESTING #
###########

def test_compile_poem():
    """ Test that the .compile() method works as intended. """
    path_obj_to_pdf = Path.cwd()/(TEMP_STEM+PDF_EXT)
    compiler = ArticleCompiler(path_to_content=PATH_TO_POEM_SOURCE)
    compiler.compile()
    # Check that the generated files are in order.
    assert path_obj_to_pdf.exists()
    assert not Path(compiler.path_to_tex).exists()
    # Clean.
    path_obj_to_pdf.unlink()

def test_compile_prose():
    """ Test that the .compile() method works as intended. """
    path_obj_to_pdf = Path.cwd()/(TEMP_STEM+PDF_EXT)
    compiler = ArticleCompiler(path_to_content=PATH_TO_PROSE_SOURCE)
    compiler.compile()
    # Check that the generated files are in order.
    assert path_obj_to_pdf.exists()
    assert not Path(compiler.path_to_tex).exists()
    # Clean.
    path_obj_to_pdf.unlink()
