# Configuration file for the Sphinx documentation builder.

import os
import sys
from datetime import datetime

# -- Path setup --------------------------------------------------------------
# Add the project root and source folders to sys.path
sys.path.insert(0, os.path.abspath('../../dl_utils'))

# -- Project information -----------------------------------------------------
project = 'dl-utils'
author = 'Blessy Moses'
copyright = f'{datetime.now().year}, {author}'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
    'sphinx_autodoc_typehints',
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']

# -- Extension configuration -------------------------------------------------

# Napoleon settings (for Google-style docstrings)
napoleon_google_docstring = True
napoleon_numpy_docstring = False

# Autodoc options
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}

# Type hints displayed in the function descriptions
autodoc_typehints = 'description'

# Enable todo notes
todo_include_todos = True