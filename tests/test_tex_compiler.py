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
PATH_OBJ_TO_TEXTPUT_LOG = Path("texput.log")

###########
# TESTING #
###########

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
    PATH_OBJ_TO_TEXTPUT_LOG.unlink(missing_ok=True)
