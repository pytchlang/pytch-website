Pytch website (developer guide)
===============================

The Pytch system is created from a handful of separate Git
repositories, and building the website documentation assumes a certain
structure for how they are checked out on the developer's machine.

TODO: Explain how this can be achieved via the 'superproject'
``pytch-releases``.

Within each of the two contributing repositories (``pytch-vm`` and
``pytch-webapp``), the documentation is expected to stick to the
following convention for providing *user-level* and *developer*
documentation.  Using ``pytch-vm`` as an example, the directory
structure should be::

  pytch-vm/doc/source/
    index.rst
    user/
      index.rst
      etc.
    developer/
      index.rst
      etc.

The top-level ``index.rst`` file (i.e., at
``pytch-vm/doc/source/index.rst``) is not used when the documentation
is brought in to the main website build.  It is present to allow
standalone work on the ``pytch-vm`` docs.  The ``pytch-webapp``
documentation sources follow the same structure.

The content in each ``user/`` directory is brought in to the
user-level sections of the documentation by the top-level
``pytch-website/doc/source/index.rst`` file, and the content of each
``developer/`` directory is brought in to the developer-level sections
by ``pytch-website/doc/source/developer.rst``.  The website repo also
has its own developer documentation, of which this page is part.

The sibling respository ``pytch-build`` is also brought in, although
its contents are entirely intended for developers, so there is no
further division into 'user' vs 'developer'.
