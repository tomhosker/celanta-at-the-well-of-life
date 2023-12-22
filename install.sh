#!/bin/sh

### This script installs any third party software used in this project.

# Local constants.
APT_PACKAGES="texlive-full"
# Paths.
PATH_TO_THIS_FOLDER="$(dirname "$0")"
PATH_TO_FONTS_SRC="$PATH_TO_THIS_FOLDER/fonts"
PATH_TO_FONTS_DST="$HOME/.fonts"
PATH_TO_REQUIREMENTS="$PATH_TO_THIS_FOLDER/pip_requirements.txt"

########################
# INSTALL APT PACKAGES #
########################

echo "I'm going to need superuser privileges to install some APT packages..."
sudo apt install --yes $APT_PACKAGES

#################
# INSTALL FONTS #
#################

# Create destination fonts folder, if necessary.
mkdir -p $PATH_TO_FONTS_DST

# Move each file across.
for filepath in "$PATH_TO_FONTS_SRC/*.ttf"; do
    cp -f $filepath $PATH_TO_FONTS_DST
done

########################
# INSTALL PIP PACKAGES #
########################

pip install -r $PATH_TO_REQUIREMENTS
