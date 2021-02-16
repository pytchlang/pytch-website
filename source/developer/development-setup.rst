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
