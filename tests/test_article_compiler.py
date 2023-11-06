"""
This code tests the ArticleCompiler class.
"""

# Standard imports.
from pathlib import Path

# Source imports.
from python.article_compiler import ArticleCompiler
from python.constants import PATH_OBJ_TO_POEMS, DEFAULT_STEM

# Local constants.
PATH_TO_ARTICLE = str(PATH_OBJ_TO_POEMS/"test.tex")

###########
# TESTING #
###########

def test_compile():
    """ Test that the .compile() method works as intended. """
    path_obj_to_pdf = Path()/(DEFAULT_STEM+".pdf")
    compiler = ArticleCompiler(path_to_content=str(PATH_TO_ARTICLE))
    compiler.compile()
    # Check that the generated files are in order.
    assert path_obj_to_pdf.exists()
    assert not Path(compiler.path_to_tex).exists()
    # Clean.
    path_obj_to_pdf.unlink()
