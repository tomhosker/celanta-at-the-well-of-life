# Celanta at the Well of Life

This repository holds the poems and stories which constitute ***Celanta at the Well of Life***, as well as the code necessary for stitching it together.

## Getting Started

Ensure that you have Python and `hosker_utils` installed (`pip install hosker-utils`), then run `install.py`.

## Scripts

### (Re)Compile Project

To (re)compile the PDF corresponding to the whole project, navigate to this directory, and then run:

```sh
python3 compile_project.py
```

### Compile Poem or Story

To compile the LaTeX for a given poem or story, navigate to this directory, and then run:

```sh
    python3 compile_article.py path/to/poem-or-story.tex
```
