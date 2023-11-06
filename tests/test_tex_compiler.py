"""
This code tests the TexCompiler class.
"""

# Standard imports.
from pathlib import Path

# Source imports.
from python.tex_compiler import TexCompiler

# Local constants.
PATH_OBJ_TO_THIS_DIR = Path(__file__).resolve().parent
PATH_OBJ_TO_TEX_TO_COMPILE = PATH_OBJ_TO_THIS_DIR/"test_files"/"standalone.tex"

###########
# TESTING #
###########

def test_compile():
    """ Test that the .compile() method works as intended. """
    stem = PATH_OBJ_TO_TEX_TO_COMPILE.stem
    path_obj_to_pdf = Path()/(stem+".pdf")
    compiler = TexCompiler(path_to_tex=str(PATH_OBJ_TO_TEX_TO_COMPILE))
    compiler.compile()
    # Check that the generated files are in order.
    assert path_obj_to_pdf.exists()
    assert not (Path()/(stem+".aux")).exists()
    # Clean.
    path_obj_to_pdf.unlink()
