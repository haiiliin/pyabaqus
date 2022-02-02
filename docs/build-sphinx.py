from sphinx.application import Sphinx

sphinx = Sphinx('docs\\source', 'docs\\source', 'docs\\build', 'docs\\build\\doctrees', 'html')
sphinx.build()
