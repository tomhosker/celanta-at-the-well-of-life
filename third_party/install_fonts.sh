#!/bin/sh

### This script installs the fonts used within this project. Note that the new
### fonts are installed centrally, and not in the virtual environment.

# Crash on the first non-zero exit code.
set -e

# Paths.
PATH_TO_THIS_DIR=$(dirname $(realpath $0))
PATH_TO_FONTS_SRC="$PATH_TO_THIS_DIR/fonts"
PATH_TO_FONTS_DST="$HOME/.fonts"

# Let's get cracking.
mkdir -p $PATH_TO_FONTS_DST
for filepath in "$PATH_TO_FONTS_SRC/*.ttf"; do
    cp -f $filepath $PATH_TO_FONTS_DST
done
