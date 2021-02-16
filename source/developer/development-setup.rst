Getting started with Pytch development
======================================

Pytch source code is available on GitHub, organised into git
submodules.  The most convenient way to work with it is via the
superproject:

* `pytch-releases on GitHub <https://github.com/pytchlang/pytch-releases/>`_

To start work on developing Pytch itself, clone this project, and run
the top-level ``develop.sh`` script.  This will first initialise and
update the submodules' content, and will appear to be doing nothing
for a short while.  You should then see messages indicating progress,
finishing with a suggestion to run a ``dev-server.sh`` script.

That script should launch various webservers, and launch a browser
running the webapp.  This should support live reload, so if you make a
small visible change to the UI, for example changing a button's text,
it should be reflected in the browser within a couple of seconds of
saving the file from your editor/IDE.


Requirements
------------

Python 3
  The build tools, for example for building tutorials, are based on
  version 3 of Python.

Node.js
  For building the Skulpt-based VM, and the webapp.  Pytch is
  developed using the Long Term Support release of Node.js, which is
  the v14 series at the time of writing.  The ``npm`` package manager
  is also required.  It usually comes bundled with Node.js.

Docker
  Optional, for :ref:`easy testing of a built
  zipfile<testing_deployment_zipfile>`.

The ``tmux`` terminal multiplexer
  The dev-server script requires ``tmux``, which is available for
  Linux and Mac machines.  It appears to be usable on Windows with
  some effort, although we have not verified this.

(This list might be incomplete; please let us know of any gaps.)
