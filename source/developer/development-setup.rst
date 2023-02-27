Getting started with Pytch development
======================================

Pytch source code is available on GitHub, organised into git
submodules.  The most convenient way to work with it is via the
superproject:

* `pytch-releases on GitHub <https://github.com/pytchlang/pytch-releases/>`_

.. note::

   If you are developing on a Windows machine, see
   :ref:`developing_on_Windows` below for suggestions.

To start work on developing Pytch itself, clone this project, and run
the top-level ``develop.sh`` script.  This will first initialise and
update the submodules' content, and will appear to be doing nothing
for a short while.  You should then see messages indicating progress,
finishing with a suggestion to run a ``dev-server.sh`` script.

You only need to run ``develop.sh`` once.

The ``dev-server.sh`` script should launch various webservers, and
launch a browser running the webapp.  This should support live reload,
so if you make a small visible change to the UI, for example changing
a button's text, it should be reflected in the browser within a couple
of seconds of saving the file from your editor/IDE.

To exit, type ``Ctrl-C`` repeatedly until you're back at your shell
prompt.

By default, the development webserver listens for connections from
other machines on your local network.  This can be useful in some
settings, but in other settings you might prefer to only allow
connections from your development machine.  If so, you can launch the
``dev-server.sh`` script with the environment variable ``HOST`` set to
``localhost``.  This can be done with the shell command

.. code-block:: shell

   HOST=localhost ./pytch-build/makesite/local-server/dev-server.sh

(assuming your shell is currently in the top-level ``pytch-releases``
directory).

.. note::

   If you get an error ``duplicate session: pytchdev`` when trying to
   run the ``dev-server.sh`` script, this is probably because you
   closed the terminal window running a previous invocation of the
   ``dev-server.sh`` script without typing ``Ctrl-C``\ s.  To fix the
   error, run ``tmux kill-session -t pytchdev`` and then run the
   ``dev-server.sh`` script again.


Requirements
------------

Python 3
  The build tools, for example for building tutorials, are based on
  version 3 of Python.  Note that on macOS, you need to have run the
  ``Install Certificates`` command, as is suggested by the Python
  installer, to ensure that the Python's package installer ``pip`` can
  make secure connections.

Poetry
  For managing Python projects and their dependencies.  See `its web
  page <https://python-poetry.org/docs/#installation>`_ for
  installation instructions.

Node.js
  For building the Skulpt-based VM, and the webapp.  Pytch is
  developed using the v14 Long Term Support release of Node.js.  The
  ``npm`` package manager is also required, which usually comes
  bundled with Node.js.  Your operating system might come with
  different versions of ``node`` and/or ``npm``.  A convenient way to
  manage multiple ``node``/``npm`` versions on your machine is to use
  `the nvm tool <https://github.com/nvm-sh/nvm>`_.

Docker
  Optional, for :ref:`easy testing of a built
  zipfile<testing_deployment_zipfile>`.

The ``tmux`` terminal multiplexer
  The dev-server script requires ``tmux``, which is available for
  Linux and Mac machines.  It is also available on Windows, under the
  Windows Subsystem for Linux (:ref:`see below
  <developing_on_Windows>`).

GNU ``coreutils``
  The build scripts use ``realpath`` from GNU ``coreutils``.  Most
  Linux-based systems will install these tools by default.  On macOS
  you may need to run ``brew install coreutils``.

(This list might be incomplete; please let us know of any gaps.)


.. _developing_on_Windows:

Developing on Windows
---------------------

The preferred way to do development work on Pytch within Windows is to
do so under the Windows Subsystem for Linux.  Follow `Microsoft's
instructions <https://learn.microsoft.com/en-us/windows/wsl/install>`_
to set up what amounts to an Ubuntu virtual machine inside your
Windows machine.

(If you encounter an error like

   Error: 0xc03a001a The requested operation could not be completed due
   to a virtual disk system limitation.  Virtual hard disk files must be
   uncompressed and unencrypted and must not be sparse.

then `this blog post <https://utf9k.net/blog/wsl2-vhd-issue/>`_
describes how the author solved it.)

Once you have WSL set up, within your Ubuntu distribution run:

.. code-block:: shell

   sudo apt update
   sudo apt install python3-virtualenv unzip

and then install ``nvm`` following the instructions in `its README
<https://github.com/nvm-sh/nvm>`_.

Once this is all done, you should be able to follow the main
instructions above, starting with cloning the ``pytch-releases``
super-project.

If you would like to use Microsoft's VSCode for development work, you
can run your native Windows VSCode, and access your Ubuntu files using
a Windows pathname starting ``\\wsl$\Ubuntu\home\your_username\``.
