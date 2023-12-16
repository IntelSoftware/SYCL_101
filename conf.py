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
author = 'Urszula Guminska, Roberto Marivela, Benjamin Odom'

# -- Publishing Meta Data ----------------------------------------------------

ditaxml_default_codeblock_type='cpp'
ditaxml_make_flat=True
ditaxml_topic_meta={}
ditaxml_topic_meta["audience"]="etm-bd7e6ab0b34d4e95901e82eaa67c07a8" # Software Developer
ditaxml_topic_meta["classification_type"]="Public"
ditaxml_topic_meta["content_classification"]="Public"
ditaxml_topic_meta["metadata_classification"]="Public"
ditaxml_topic_meta["content_type"]="etm-8f11476223194fa68d9e0bad77696e2f" # Tutorial
ditaxml_topic_meta["document_title"]="SYCL 101"
ditaxml_topic_meta["description"]="An introduction to modern C++ using C++ 20 examples."
ditaxml_topic_meta["group_content_id"]="694972" # 694972_694973 for version 2023.0 #requested
ditaxml_topic_meta["publication_content_id"]="694973"
ditaxml_topic_meta["keywords"]="None"
ditaxml_topic_meta["locale"]="en-us"
ditaxml_topic_meta["menu"]="/content/data/globalelements/US/en/sub-navigation/idz/developer-sub-navigation-breadcrumb"
ditaxml_topic_meta["menu_parent"]="/content/www/us/en/developer/tools/overview"
ditaxml_topic_meta["notification_dl"]="infodev.book.publishing.notices@intel.com"
ditaxml_topic_meta["primary_business_owner"]="Odom, Benjamin J (benjamin.j.odom@intel.com)"
ditaxml_topic_meta["primary_owner"]="Odom, Benjamin J (benjamin.j.odom@intel.com)"
ditaxml_topic_meta["primary_tags"]="etm-086ec8c4b4074875b84ba0e35d214cf5" # Product Documentation
ditaxml_topic_meta["program_identifier"]="idz"
ditaxml_topic_meta["latest_version"]="true"
ditaxml_topic_meta["publish_date"]="2023-12-20" #TBD
ditaxml_topic_meta["revision_date"]="2023-12-01" #TBD
ditaxml_topic_meta["publication_root_node"]="test"
ditaxml_topic_meta["publication_name"]="SYCL 101"
ditaxml_topic_meta["latest_version"]="true"
ditaxml_prod_info={}
ditaxml_prod_info["prodname"]=""
ditaxml_prod_info["version"]="2023.1"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.]

extensions = ['myst_parser',
    'sphinx_md', 
    'rst2pdf.pdfbuilder',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',]
    # 'sphinx_new_tab_link',]   # to open links in a new tab

pdf_documents = [('index', u'SYCL_101', u'SYCL 101', u'Intel Corporation'),]

# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md']

smartquotes=False
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

project_title = 'SYCL 101'
html_title    = project_title
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

    # -- Options for LaTeX output ---------------------------------------------

latex_engine = 'pdflatex'
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'letterpaper',
    'releasename':" ",
    # Sonny, Lenny, Glenn, Conny, Rejne, Bjarne and Bjornstrup
    # 'fncychap': '\\usepackage[Lenny]{fncychap}',
    'fncychap': '\\usepackage{fncychap}',
    'fontpkg': '\\usepackage{amsmath,amsfonts,amssymb,amsthm}',

    'figure_align':'htbp',
    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '12pt',

    # Additional stuff for the LaTeX preamble.
    #
    'preamble': r'''
        %%%%%%%%%%%%%%%%%%%% Meher %%%%%%%%%%%%%%%%%%
        %%%add number to subsubsection 2=subsection, 3=subsubsection
        %%% below subsubsection is not good idea.
        \setcounter{secnumdepth}{3}
        %
        %%%% Table of content upto 2=subsection, 3=subsubsection
        \setcounter{tocdepth}{2}

        \usepackage{amsmath,amsfonts,amssymb,amsthm}
        \usepackage{graphicx}

        %%% reduce spaces for Table of contents, figures and tables
        %%% it is used "\addtocontents{toc}{\vskip -1.2cm}" etc. in the document
        \usepackage[notlot,nottoc,notlof]{}

        \usepackage{color}
        \usepackage{transparent}
        \usepackage{eso-pic}
        \usepackage{lipsum}

        \usepackage{footnotebackref} %%link at the footnote to go to the place of footnote in the text

        %% spacing between line
        \usepackage{setspace}
        %%%%\onehalfspacing
        %%%%\doublespacing
        \singlespacing


        %%%%%%%%%%% datetime
        \usepackage{datetime}

        \newdateformat{MonthYearFormat}{%
            \monthname[\THEMONTH], \THEYEAR}


        %% RO, LE will not work for 'oneside' layout.
        %% Change oneside to twoside in document class
        \usepackage{fancyhdr}
        \pagestyle{fancy}
        \fancyhf{}

        %%% Alternating Header for oneside
        \fancyhead[L]{\ifthenelse{\isodd{\value{page}}}{ \small \nouppercase{\leftmark} }{}}
        \fancyhead[R]{\ifthenelse{\isodd{\value{page}}}{}{ \small \nouppercase{\rightmark} }}

        %%% Alternating Header for two side
        %\fancyhead[RO]{\small \nouppercase{\rightmark}}
        %\fancyhead[LE]{\small \nouppercase{\leftmark}}

        %% for oneside: change footer at right side. If you want to use Left and right then use same as header defined above.
        \fancyfoot[R]{\ifthenelse{\isodd{\value{page}}}{{\tiny Meher Krishna Patel} }{\href{http://pythondsp.readthedocs.io/en/latest/pythondsp/toc.html}{\tiny PythonDSP}}}

        %%% Alternating Footer for two side
        %\fancyfoot[RO, RE]{\scriptsize Meher Krishna Patel (mekrip@gmail.com)}

        %%% page number
        \fancyfoot[CO, CE]{\thepage}

        \renewcommand{\headrulewidth}{0.5pt}
        \renewcommand{\footrulewidth}{0.5pt}

        \RequirePackage{tocbibind} %%% comment this to remove page number for following
        \addto\captionsenglish{\renewcommand{\contentsname}{Table of contents}}
        \addto\captionsenglish{\renewcommand{\listfigurename}{List of figures}}
        \addto\captionsenglish{\renewcommand{\listtablename}{List of tables}}
        % \addto\captionsenglish{\renewcommand{\chaptername}{Chapter}}


        %%reduce spacing for itemize
        \usepackage{enumitem}
        \setlist{nosep}

        %%%%%%%%%%% Quote Styles at the top of chapter
        \usepackage{epigraph}
        \setlength{\epigraphwidth}{0.8\columnwidth}
        \newcommand{\chapterquote}[2]{\epigraphhead[60]{\epigraph{\textit{#1}}{\textbf {\textit{--#2}}}}}
        %%%%%%%%%%% Quote for all places except Chapter
        \newcommand{\sectionquote}[2]{{\quote{\textit{``#1''}}{\textbf {\textit{--#2}}}}}
    ''',


    'maketitle': r'''
        \pagenumbering{Roman} %%% to avoid page 1 conflict with actual page 1

        \begin{titlepage}
            \centering

            \vspace*{40mm} %%% * is used to give space from top
            \textbf{\Huge {Sphinx format for Latex and HTML}}

            \vspace{0mm}
            \begin{figure}[!h]
                \centering
                \includegraphics[scale=0.3]{logo.jpg}
            \end{figure}

            \vspace{0mm}
            \Large \textbf{{Meher Krishna Patel}}

            \small Created on : Octorber, 2017

            \vspace*{0mm}
            \small  Last updated : \MonthYearFormat\today


            %% \vfill adds at the bottom
            \vfill
            \small \textit{More documents are freely available at }{\href{http://pythondsp.readthedocs.io/en/latest/pythondsp/toc.html}{PythonDSP}}
        \end{titlepage}

        \clearpage
        \pagenumbering{roman}
        \tableofcontents
        \listoffigures
        \listoftables
        \clearpage
        \pagenumbering{arabic}

        ''',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    'sphinxsetup': \
        'hmargin={0.7in,0.7in}, vmargin={1in,1in}, \
        verbatimwithframe=true, \
        TitleColor={rgb}{0,0,0}, \
        HeaderFamily=\\rmfamily\\bfseries, \
        InnerLinkColor={rgb}{0,0,1}, \
        OuterLinkColor={rgb}{0,0,1}',

        'tableofcontents':' ',



}

#latex_logo = '_static/logo.jpg'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
#latex_documents = [
#    ('main.tex', 'Sphinx format for Latex and HTML',
#     'Meher Krishna Patel', 'report')
#]
