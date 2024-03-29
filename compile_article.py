"""
This code defines a script which compiles an article at a given path.
"""

# Standard imports.
import argparse

# Local imports.
from python.article_compiler import ArticleCompiler

##############
# RUN SCRIPT #
##############

def make_parser():
    """ Return an argument parser. """
    result = \
        argparse.ArgumentParser(
            description="Compile a given article"
        )
    result.add_argument(
        "path_to_content",
        help="The path to the content of the article to be compiled"
    )
    result.add_argument(
        "--path-to-output",
        default="temp.pdf",
        dest="path_to_output",
        help="The path to which we want our document to be compiled"
    )
    result.add_argument(
        "--preserve-tex",
        action="store_true",
        default=False,
        dest="preserve_tex",
        help="Preserve the .tex file used to build the PDF"
    )
    result.add_argument(
        "--prose-poem",
        action="store_true",
        default=False,
        dest="is_prose_poem",
        help="Declare a prose poem"
    )
    return result

def run():
    """ Run this file. """
    parser = make_parser()
    arguments = parser.parse_args()
    compiler = \
        ArticleCompiler(
            path_to_content=arguments.path_to_content,
            path_to_output=arguments.path_to_output,
            preserve_tex=arguments.preserve_tex,
            is_prose_poem=arguments.is_prose_poem
        )
    compiler.compile()

if __name__ == "__main__":
    run()
