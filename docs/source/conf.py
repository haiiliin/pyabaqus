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
import inspect
import sys

project = 'PYABAQUS'
copyright = '2022, WANG Hailin'
author = 'WANG Hailin'

# The full version, including alpha/beta/rc tags
release = '2022.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_toolbox.more_autodoc.overloads',
    'sphinx.ext.autodoc',
    'numpydoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.linkcode',
    'sphinx.ext.githubpages',
]


# linkcode source
def linkcode_resolve(domain: str, info: dict):
    """Resolve linkcode source

    Parameters
    ----------
    domain : str
        specifies the language domain the object is in
    info : dict
        a dictionary with the following keys guaranteed to be present (dependent on the domain)
        - py: module (name of the module), fullname (name of the object)
        - c: names (list of names for the object)
        - cpp: names (list of names for the object)
        - javascript: object (name of the object), fullname (name of the item)

    Returns
    -------
    source url of the object
    """
    if domain != 'py':
        return None

    modname = info['module']
    fullname = info['fullname']

    filename = modname.replace('.', '/')
    baseurl = f'https://github.com/haiiliin/pyabaqus/blob/V{release.split(".")[0]}/src/{filename}.py'

    submod = sys.modules.get(modname)
    if submod is None:
        return baseurl

    obj = submod
    for part in fullname.split('.'):
        try:
            obj = getattr(obj, part)
        except Exception:
            return baseurl
    try:
        source, lineno = inspect.getsourcelines(obj)
    except Exception:
        return baseurl

    return baseurl + f'#L{lineno}-L{lineno + len(source) - 1}'


# Show short type hints for user-defined classes and defaults for parameters
python_use_unqualified_type_names = True
autodoc_typehints_format = 'short'

numpydoc_show_class_members = True
numpydoc_show_inherited_class_members = False
numpydoc_xref_param_type = True
add_module_names = False

# True to convert the type definitions in the docstrings as references. Defaults to False.
napoleon_preprocess_types = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'furo'

# Logo
# html_logo = "_static/3ds-dark.svg"


html_theme_options = {
    "announcement": "The `pyabaqus` package has been deprecated. Please use the <a href='https://github.com/haiiliin/abqpy' target='_blank'>abqpy</a> package instead.",
    "light_css_variables": {
        "color-announcement-background": "#7C4DFF",
        "color-announcement-text": "#FFFFFF",
    }
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for LaTeX output -------------------------------------------------

# If true, add page references after internal references. This is very useful
# for printed copies of the manual. Default is False.
latex_show_pagerefs = True

# Control whether to display URL addresses. This is very useful for printed
# copies of the manual. The setting can have the following values:
# 'no' – do not display URLs (default)
# 'footnote' – display URLs in footnotes
# 'inline' – display URLs inline in parentheses
latex_show_urls = 'footnote'

# If given, this must be the name of an image file (relative to the
# configuration directory) that is the logo of the docs. It is placed at the
# top of the title page. Default: None.
latex_logo = None

# The “theme” that the LaTeX output should use. It is a collection of settings
# for LaTeX output (ex. document class, top level sectioning unit and so on).
# As a built-in LaTeX themes, manual and howto are bundled.
# manual
# A LaTeX theme for writing a manual. It imports the report document class
# (Japanese documents use jsbook).
# howto
# A LaTeX theme for writing an article. It imports the article document class
# (Japanese documents use jreport rather). latex_appendices is available only for this theme.
# It defaults to 'manual'.
latex_theme = 'manual'

# autoclass_content = 'both'

latex_toplevel_sectioning = 'part'
latex_engine = 'xelatex'
latex_use_xindy = False
latex_elements = {
    'preamble': '\\usepackage[UTF8]{ctex}\n\\setcounter{tocdepth}{3}\n\\setcounter{secnumdepth}{5}',
    'printindex': '\\def\\twocolumn[#1]{#1}\\printindex',
}
