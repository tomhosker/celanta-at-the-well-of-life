"""
This code tests the ArticleCompiler class.
"""

# Standard imports.
from pathlib import Path

# Source imports.
from python.article_compiler import ArticleCompiler, ARTICLE_STEM
from python.constants import PATH_OBJ_TO_POEMS

# Local constants.
PATH_TO_ARTICLE = str(PATH_OBJ_TO_POEMS/"test.tex")

###########
# TESTING #
###########

def test_compile():
    """ Test that the .compile() method works as intended. """
    path_obj_to_pdf = Path()/(ARTICLE_STEM+".pdf")
    compiler = ArticleCompiler(path_to_content=str(PATH_TO_ARTICLE))
    compiler.compile()
    # Check that the generated files are in order.
    assert path_obj_to_pdf.exists()
    assert not Path(compiler.path_to_tex).exists()
    # Clean.
    path_obj_to_pdf.unlink()

def test_compile_preserve_tex():
    """ As above, but also test that the TeX file is preserved if requested. """
    path_obj_to_pdf = Path()/(ARTICLE_STEM+".pdf")
    compiler = \
        ArticleCompiler(
            path_to_content=str(PATH_TO_ARTICLE),
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
