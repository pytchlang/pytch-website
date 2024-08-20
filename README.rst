=====================
Pytch Website Content
=====================


Development setup
-----------------

This project uses `poetry <https://python-poetry.org/>`_.  We
currently use version 1.8.3.

To set up a virtualenv for development and testing::

  poetry install

which will cause *poetry* to create a virtual environment in a
``.venv`` folder.

For live reload while editing docs, first enter a shell which has the
poetry virtualenv activated by doing::

  poetry shell

then within that shell, run::

  sphinx-autobuild --re-ignore '/\.#' source build/html

and then visit the URL mentioned in the output.  (The ``--re-ignore
'/\.#'`` avoids Emacs auto-save files; other editors might require
something analogous.)
