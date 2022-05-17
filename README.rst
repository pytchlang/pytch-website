=====================
Pytch Website Content
=====================


Development setup
-----------------

To set up a virtualenv for development::

  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements_dev.txt

To develop documentation with live-reload::

  sphinx-autobuild --re-ignore '/\.#' source build/html

and visit the URL mentioned in the output.  (The ``--re-ignore
'/\.#'`` avoids Emacs auto-save files; other editors might require
something analogous.)
