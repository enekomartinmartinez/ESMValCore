# -*- coding: utf-8 -*-
#
# ESMValTool documentation build configuration file, created by
# sphinx-quickstart on Tue Jun  2 11:34:13 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys
from datetime import datetime
from pathlib import Path

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
root = Path(__file__).absolute().parent.parent
sys.path.insert(0, str(root))

from esmvalcore import __version__

# -- RTD configuration ------------------------------------------------

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from
# docs.readthedocs.org
on_rtd = os.environ.get("READTHEDOCS", None) == "True"

# This is used for linking and such so we link to the thing we're building
rtd_version = os.environ.get("READTHEDOCS_VERSION", "latest")
if rtd_version not in ["latest", "doc"]:  # TODO: add "stable" once we have it
    rtd_version = "latest"

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'autodocsumm',
]

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'inherited-members': True,
    'show-inheritance': True,
    'autosummary': True,
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'ESMValTool'
copyright = u'{0}, ESMValTool Development Team'.format(datetime.now().year)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '.'.join(__version__.split('.')[0:1])
# The full version, including alpha/beta/rc tags.
release = __version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns: list = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "ESMValTool {0}".format(release)

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'figures/ESMValTool-logo-2.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path: list = []

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'ESMValTooldoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'preamble':
    r'''
   \makeatletter
   \renewcommand{\maketitle}{
     \newcommand{\MONTH}{%
       \ifcase\the\month
       \or January% 1
       \or February% 2
       \or March% 3
       \or April% 4
       \or May% 5
       \or June% 6
       \or July% 7
       \or August% 8
       \or September% 9
       \or October% 10
       \or November% 11
       \or December% 12
     \fi}
     \begin{titlepage}
     \begin{center}
     \includegraphics[width=\textwidth]{figures/ESMValTool-logo-2.pdf}\par
     \vspace{2cm}
     {\Huge \bf \sffamily User's and Developer's Guide \par}
     \vspace{1cm}
     {\Large \sffamily \MONTH ~ \the\year \par}
     \vspace{12cm}
     Deutsches Zentrum f\"ur Luft- und Raumfahrt (DLR),
     Institut f\"ur Physik der Atmosph\"are, Oberpfaffenhofen, Germany \par
     \vspace{0.5cm}
     http://www.esmvaltool.org/ \par
     \end{center}
     \end{titlepage}
     \clearpage
   }
   \makeatother'''
}

# latex_additional_files = []

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', 'ESMValTool_Users_Guide.tex',
     u'ESMValTool User\'s and Developer\'s Guide',
     u'ESMValTool Development Team', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = True
latex_toplevel_sectioning = "part"

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
# man_pages = [
#    ('index', 'esmvaltool', u'ESMValTool Documentation',
#     [
#         (u'Veronika Eyring, Axel Lauer, Mattia Righi,'
#          u' Martin Evaldsson et al.')
#     ], 1)
# ]

# If true, show URL addresses after external links.
# man_show_urls = False

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
# texinfo_documents = [
#  ('index', 'ESMValTool', u'ESMValTool Documentation',
#   u'Veronika Eyring, Axel Lauer, Mattia Righi, Martin Evaldsson et al.',
#   'ESMValTool',
#   'One line #description of project.',
#   'Miscellaneous'),
# ]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'ESMValTool'
epub_author = u'ESMValTool Development Team'
epub_publisher = u'ESMValTool Development Team'
epub_copyright = u'ESMValTool Development Team'

# The basename for the epub file. It defaults to the project name.
# epub_basename = u'ESMValTool'

# The HTML theme for the epub output. Since the default themes are not
# optimized for small screen space, using the same theme for HTML and epub
# output is usually not wise. This defaults to 'epub', a theme designed to
# save visual space.
# epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or en if the language is not set.
# epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
# epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
# epub_identifier = ''

# A unique identification for the text.
# epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
# epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
# epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
# epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
# epub_tocdepth = 3

# Allow duplicate toc entries.
# epub_tocdup = True

# Choose between 'default' and 'includehidden'.
# epub_tocscope = 'default'

# Fix unsupported image types using the PIL.
# epub_fix_images = False

# Scale large images.
# epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# epub_show_urls = 'inline'

# If false, no index is generated.
# epub_use_index = True

numfig = True

# Configuration for intersphinx
intersphinx_mapping = {
    'cf_units': ('https://cf-units.readthedocs.io/en/latest/', None),
    'cftime': ('https://unidata.github.io/cftime/', None),
    'esmvalcore':
    (f'https://docs.esmvaltool.org/projects/esmvalcore/en/{rtd_version}/',
     None),
    'esmvaltool': (f'https://docs.esmvaltool.org/en/{rtd_version}/', None),
    'iris': ('https://scitools-iris.readthedocs.io/en/latest/', None),
    'iris-esmf-regrid': ('https://iris-esmf-regrid.readthedocs.io/en/latest',
                         None),
    'matplotlib': ('https://matplotlib.org/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    'pyesgf': ('https://esgf-pyclient.readthedocs.io/en/latest/', None),
    'python': ('https://docs.python.org/3/', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/', None),
}

# -- Custom Document processing ----------------------------------------------

sys.path.append(os.path.dirname(__file__))
from gensidebar import generate_sidebar

generate_sidebar(globals(), "esmvalcore")
