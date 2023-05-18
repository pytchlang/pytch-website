Overview of Pytch design
========================

Pytch is made of several components.  A summary follows, with more
detail on each one below.

Skulpt-based Python runtime (``pytch-vm``, for “Virtual Machine”) :doc:`[more] <../vm/developer/index>`
  A fork of the Skulpt system for running Python in the browser.  We
  have made a small change to the compiler, added a library of
  user-visible and support functions for running Pytch programs, and
  created a concurrency system resembling Scratch’s.

Webapp (``pytch-webapp``) :doc:`[more] <../webapp/developer/index>`
  The React-based frontend app.  Browser-based storage of user
  projects.  Allows user to edit program text, and add images and
  sounds.  Feeds user programs to the VM, drives the concurrency
  scheduler, and displays the results frame-by-frame on the stage.
  Handles content printed to stdout by the VM, and errors thrown by
  the VM.  Integrates self-paced tutorials (see below).

Media library (``pytch-medialib``) :doc:`[more] <../medialib/developer/index>`
  Skeleton which will in due course hold the media assets (images and
  sounds) for users to use in their projects, and for use in
  tutorials.  Currently, the assets live in the ``pytch-tutorials``
  repo and there’s a build stage which populates the media library.

Tutorials (``pytch-tutorials``) [see :doc:`Build tools <../build-tools/index>` for more]
  Data for the self-paced tutorials.  This repo is unusual in that the
  entire history of a branch is important, not just the current state.
  Each tutorial has its own branch.  Commits which update the Python
  code are available for inclusion as diffs in the tutorial as
  presented to the user.

Build tools (``pytch-build``) :doc:`[more] <../build-tools/index>`
  Mostly used to turn the tutorials into a form ready for inclusion in
  the webapp.  The main tool is a “compiler” which reads the git
  history of each tutorial’s branch, and emits a big lump of HTML, as
  well as an index.  The webapp then requests this and presents it to
  the user in interactive form.  Also contains scripts to help develop
  the system.

Website (``pytch-website``)
  Content of the Pytch website which is not the app.  Documentation is
  driven from here, although it brings in sections taken from the
  other repos.

Top-level superproject (``pytch-releases``)
  Combines all the above.  Also has various build and set-up scripts.
