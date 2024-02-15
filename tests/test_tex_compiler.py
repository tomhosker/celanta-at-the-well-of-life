"""
This code tests the TexCompiler class.
"""

# Standard imports.
from pathlib import Path

# Source imports.
from python.constants import TEMP_STEM, PDF_EXT
from python.tex_compiler import TexCompiler

# Local constants.
PATH_OBJ_TO_THIS_DIR = Path(__file__).parent
PATH_OBJ_TO_TEX_TO_COMPILE = PATH_OBJ_TO_THIS_DIR/"test_files"/"standalone.tex"

###########
# TESTING #
###########

def test_compile():
    """ Test that the .compile() method works as intended. """
    stem = PATH_OBJ_TO_TEX_TO_COMPILE.stem
    path_obj_to_pdf = Path.cwd()/(TEMP_STEM+PDF_EXT)
    compiler = TexCompiler(path_to_tex=str(PATH_OBJ_TO_TEX_TO_COMPILE))
    compiler.compile()
    # Check that the generated files are in order.
    assert path_obj_to_pdf.exists()
    assert not (Path()/(stem+".aux")).exists()
    # Clean.
    path_obj_to_pdf.unlink()

def test_compile_preserve_tex():
    """ As above, but also test that the TeX file is preserved if requested. """
    path_obj_to_pdf = Path.cwd()/(TEMP_STEM+PDF_EXT)
    compiler = \
        TexCompiler(
            path_to_tex=str(PATH_OBJ_TO_TEX_TO_COMPILE),
            preserve_tex=True
        )
    compiler.compile()
    # Check that the generated files are in order.
    path_obj_to_tex = Path(compiler.path_to_tex)
    assert path_obj_to_pdf.exists()
    assert path_obj_to_tex.exists()
    # Clean.
    path_obj_to_pdf.unlink()
    path_obj_to_tex.unlink()
