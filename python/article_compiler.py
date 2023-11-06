"""
This code defines a class which compiles a given poem or story into a PDF.
"""

# Standard imports.
from pathlib import Path

# Local imports.
from .constants import (
    PATH_OBJ_TO_SCAFFOLDING,
    PATH_TO_PACKAGES,
    PACKAGES_MARKER,
    TITLE_MARKER,
    CONTENT_MARKER,
    DEFAULT_LATEX_COMMAND,
    DEFAULT_STEM,
    TEX_EXT,
    PDF_EXT
)
from .tex_compiler import TexCompiler
from .utils import get_contents, get_title

# Local constants.
ARTICLE_TEMPLATE = \
    get_contents(str(PATH_OBJ_TO_SCAFFOLDING/"article_template.tex"))
ARTICLE_STEM = "article"

##############
# MAIN CLASS #
##############

class ArticleCompiler(TexCompiler):
    """ The class in question. """
    def __init__(
            self,
            path_to_content,
            path_to_tex=DEFAULT_STEM+TEX_EXT,
            latex_command=DEFAULT_LATEX_COMMAND,
            preserve_tex=False
        ):
        super().__init__()
        self.preserve_tex = preserve_tex
        self.title = get_title(path_to_content)
        self.content = get_contents(path_to_content)
        self.packages = get_contents(PATH_TO_PACKAGES)

    def build_tex(self):
        """ Build the TeX file, which we will then compile. """
        tex = ARTICLE_TEMPLATE
        find_replace_pairs = (
            (PACKAGES_MARKER, self.packages),
            (TITLE_MARKER, self.title),
            (CONTENT_MARKER, self.content)
        )
        for pair in find_replace_pairs:
            tex = tex.replace(*pair)
        with open(self.path_to_tex, "w") as tex_file:
            tex_file.write(tex)

    def clean(self):
        """ Remove any generated files as necessary. """
        super().clean()
        if not self.preserve_tex:
            Path(self.path_to_tex).unlink()

    def compile(self):
        """ As with the parent's method, but build the TeX file first. """
        path_obj_to_tex = Path(self.path_to_tex)
        path_obj_to_pdf = path_obj_to_tex.parent/(path_obj_to_tex.stem+PDF_EXT)
        new_path_obj_to_pdf = path_obj_to_tex.parent/(ARTICLE_STEM+PDF_EXT)
        self.build_tex()
        super().compile()
        path_obj_to_pdf.rename(new_path_obj_to_pdf)
