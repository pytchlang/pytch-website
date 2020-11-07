# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Pytch'
copyright = '2020, Ben North, Glenn Strong'
author = 'Ben North, Glenn Strong'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
#
# Ignore the index.rst files used for standalone/development builds of
# the VM and webapp documentations, otherwise they override the
# parent/child relationships between the docs.  The effect of this was
# that the sidebar ToC was not expanding properly under the "Developer
# documentation" entry.
#
exclude_patterns = [
    "vm/index.rst",
    "webapp/index.rst",
    "build-tools/index.rst",
]

primary_domain = "py"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "classic"
html_copy_source = False

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    "css/pytch-classic.css",
]

html_sidebars = { "**": [ "globaltoc.html", "dochome.html" ] }

pytch_fonts = ('"Lato", -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto",'
               + '"Oxygen", "Ubuntu", "Cantarell", "Fira Sans", "Droid Sans",'
               + '"Helvetica Neue", sans-serif')

html_theme_options = {
    "globaltoc_maxdepth": 3,
    "bgcolor": "#ddf",
    "headbgcolor": "#ddf",
    "headtextcolor": "black",
    "sidebarbgcolor": "#cce",
    "sidebartextcolor": "black",
    "sidebarlinkcolor": "black",
    "bodyfont": pytch_fonts,
    "headfont": pytch_fonts,
    "body_max_width": None,
}
