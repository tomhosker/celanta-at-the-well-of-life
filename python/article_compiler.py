"""
This code defines a class which compiles a given poem or story into a PDF.
"""

# Standard imports.
from dataclasses import dataclass
from pathlib import Path

# Non-standard imports.
from hpml import HPMLCompiler, PACKAGE_CODE as POEM_PACKAGE_CODE

# Local imports.
from .constants import (
    PATH_TO_ARTICLE_TEMPLATE,
    PACKAGES_MARKER,
    TITLE_MARKER,
    CONTENT_MARKER,
    HPML_EXT
)
from .tex_compiler import TexCompiler, TexCompilerError
from .utils import get_contents, get_title, get_prose_package_code

# Local constants.
ARTICLE_TEMPLATE = get_contents(PATH_TO_ARTICLE_TEMPLATE)
PROSE_PACKAGE_CODE = get_prose_package_code()

##############
# MAIN CLASS #
##############

@dataclass
class ArticleCompiler(TexCompiler):
    """ The class in question. """
    path_to_content: str = None
    is_prose_poem: bool = False
    is_poem: bool = False
    title: str = None
    content: str = None

    def __post_init__(self):
        if not self.path_to_content:
            raise TexCompilerError("path_to_content field not set")
        self.is_poem = self._get_is_poem()
        self.title = get_title(self.path_to_content)
        self.package_code = self._get_package_code()
        self.content = self._build_content_tex()

    def _get_is_poem(self):
        """ Determine whether the content is a poem. """
        path_obj_to_content = Path(self.path_to_content)
        if path_obj_to_content.suffix == HPML_EXT:
            return True
        return False

    def _get_package_code(self):
        """ Return the correct package code, depending on whether the article
        in question is poetry or prose. """
        if self.is_poem:
            return POEM_PACKAGE_CODE
        return PROSE_PACKAGE_CODE

    def _build_content_tex(self):
        """ Transform the raw content into LaTeX, if necessary """
        raw_content = get_contents(self.path_to_content)
        if self.is_poem:
            hpml_compiler = \
                HPMLCompiler(
                    input_string=raw_content,
                    is_prose_poem=self.is_prose_poem
                )
            result = hpml_compiler.compile()
        else:
            result = raw_content
        return result

    def _build_tex(self):
        """ Build the TeX file, which we will then compile. """
        tex = ARTICLE_TEMPLATE
        find_replace_pairs = (
            (PACKAGES_MARKER, self.package_code),
            (TITLE_MARKER, self.title),
            (CONTENT_MARKER, self.content)
        )
        for pair in find_replace_pairs:
            tex = tex.replace(*pair)
        with open(self.path_to_tex, "w") as tex_file:
            tex_file.write(tex)

    def compile(self):
        """ As with the parent's method, but build the TeX file first. """
        self._build_tex()
        super().compile()
