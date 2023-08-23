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
from docutils import nodes

# -- Project information -----------------------------------------------------

project = 'SYCL 101'
copyright = '2023, various'
author = 'various'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.]

extensions = ['myst_parser','sphinx_md', 'rst2pdf.pdfbuilder']

pdf_documents = [('index', u'rst2pdf', u'Sample rst2pdf doc', u'Intel Corporation'),]


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

smartquotes=False
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'
html_output_encoding = 'ascii'
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['tiles.css','custom.css']

def fixFigureTargets(app, doctree, docname):
    for node in doctree.traverse(nodes.reference):
        internal = node.get('internal')
        if not internal:
            uri = node.get('refuri')
            if not uri:
                continue
            if uri.endswith('.rst') and '://' not in uri:
                node['refuri'] = uri.replace('.rst',app.builder.out_suffix)

def setup(app):
    app.connect('doctree-resolved',fixFigureTargets)