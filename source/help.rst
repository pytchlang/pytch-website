Writing Pytch programs
======================

In Pytch, you describe what you want the Sprites in your project to do
by writing Python code.


Editing and building
--------------------

You write and edit your Python program in the top-left panel. Unlike
Scratch, where changes take effect straight away, in Python you must
*build* your program first. In Pytch, this is done with the *BUILD*
button above the stage. Compiling can take a few seconds for a
complicated program. If there are errors in your program, a
description of the problem will appear in the ‘Errors’ tab of the
information pane.

It is a good idea to save your project's code often, with the *Save*
button above the stage.

Running and stopping
--------------------

Once your program builds successfully, you can click on the stage and
then use your program. Many projects will need the user to click the
*green flag*. To stop all running scripts, hit the *red stop
button*. The green flag and stop button are both above the stage.

Sprites
-------

Each sprite in your project has its own Python ``class``, which must be
derived from the ``pytch.Sprite`` class. For example,

.. code:: python

   class Star(pytch.Sprite):
       # Code for Star goes here

Stage
-----

Your project must have a ``class`` for the stage, which must be derived
from the ``pytch.Stage`` class. For example,

.. code:: python

   class Stage(pytch.Stage):
       # Code for your stage goes here

Scripts
-------

The Pytch equivalent of a Scratch script for a sprite is a *method* on
that sprite. For example,

.. code:: python

       @pytch.when_key_pressed("ArrowUp")
       def move_up(self):
           self.change_y_pos(10)

Here we see that a *method decorator* does the job of a Scratch *hat
block*, and the method call ``self.change_y_pos(10)`` does the job of
the *change y by* Scratch block.

Costumes
--------

Your sprite usually has at least one costume. These are given in a *class
attribute* called ``Costumes``, for example

.. code:: python

   class Player(pytch.Sprite):
       Costumes = ["python-logo.png"]
       # ... other code for Player ...

More details on how you tell Pytch what Costumes to use are available
in a separate document.  (TODO: Link to it.)

Stage backdrops
---------------

Your ``Stage``-derived class must have an attribute ``Backdrops`` of the
same form as a Sprite’s ``Costumes`` attribute, for example

.. code:: python

   class Stage(pytch.Stage):
       Backdrops = ["starry-sky.jpg"]
       # ... other code for Stage ...

The image should 480 pixels wide and 360 high.

More details on how you tell Pytch what Backdrops to use are available
in a separate document.  (TODO: Link to it.)

Sounds
------

If you want to use sounds, your sprite must have a class attribute
called ``Sounds``, for example

.. code:: python

   class Player(pytch.Sprite):
       Sounds = ["pop.mp3"]
       # ... other code for Player ...

More details on how you tell Pytch what Sounds to use are available
in a separate document.  (TODO: Link to it.)

Equivalents to Scratch blocks
-----------------------------

Apart from ‘hat’ blocks, Pytch provides equivalents to (some) Scratch
blocks in three ways:

Methods on a ``Sprite``
~~~~~~~~~~~~~~~~~~~~~~~

-  ``self.x_pos()`` gives the Sprite’s current x coordinate
-  ``self.y_pos()`` gives the Sprite’s current y coordinate
-  ``self.change_x_pos(dx)`` adds ``dx`` to the Sprite’s current x
   coordinate
-  ``self.change_y_pos(dy)`` adds ``dy`` to the Sprite’s current y
   coordinate
-  ``self.set_x_pos(x)`` sets the Sprite’s x coordinate to ``x``
-  ``self.set_y_pos(y)`` sets the Sprite’s x coordinate to ``y``
-  ``self.go_to_xy(x, y)`` sets the Sprite’s current x and y coordinates
   to ``x`` and ``y`` respectively
-  ``self.show()`` makes the Sprite be visible
-  ``self.hide()`` makes the Sprite be not visible
-  ``self.switch_costume(costume_name)`` sets the Sprite’s costume to
   the one given by ``costume_name``
-  ``self.touching(other_name)`` gives a true/false answer as to whether
   the Sprite is touching the Sprite whose name is ``other_name``;
   currently this is done by rectangular bounding-box so is an
   approximation only
-  ``self.start_sound(sound_name)`` launches the playback of the sound
   with name ``sound_name``; the script continues with the sound playing
   in the background

TODO: Finish this summary list.

Methods on the stage
~~~~~~~~~~~~~~~~~~~~

In future we hope to implement the various Stage-only blocks from
Scratch, for example ``next_backdrop()``.

TODO: We do have switch-backdrop; describe this.


Functions within the ``pytch`` module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  ``pytch.wait_seconds(n_seconds)`` makes the script calling
   ``wait_seconds()`` do nothing for ``n_seconds`` seconds before
   resuming; currently this is done by counting frames, so complicated
   scripts which render at less than 60fps will wait for the wrong
   amount of time; fixing this is on the roadmap
-  ``pytch.broadcast(message_string)`` broadcasts the message
   ``message_string``, launching any scripts with a matching
   ``@pytch.when_I_receive()`` decorator (hat-block); the script calling
   ``broadcast()`` continues, with the responses happening concurrently
- ``pytch.broadcast_and_wait(message_string)`` broadcasts the message
   ``message_string``, launching any scripts with a matching
   ``@pytch.when_I_receive()`` decorator (hat-block); the script
   calling ``broadcast_and_wait()`` waits until all those scripts have
   finished before continuing
-  ``pytch.key_is_pressed(key_name)`` gives a true/false answer as to
   whether the key with name ``key_name`` is currently pressed

Scratch ‘hat’ blocks
--------------------

Done via Python *decorators*. E.g.,

.. code:: python

       @pytch.when_I_receive("Play_One_Point")
       def prepare_to_play(self):
           # ... do stuff ...

The available decorators are:

* ``@pytch.when_I_receive(message_string)`` causes the decorated
  method to be called whenever somebody broadcasts the given
  ``message_string``
* ``@pytch.when_green_flag_clicked()`` causes the decorated method to
  be called whenever the green flag is clicked by the user
* ``@pytch.when_key_pressed(key_name_as_string)`` causes the decorated
  method to be called whenever the user presses the given key
* ``@pytch.when_this_sprite_clicked()`` causes the decorated method to
  be called whenever the user clicks / taps on the sprite

Errors
------

If there is an error in your Python program, this will be shown in the
‘Errors’ tab of the information pane.  The error report includes
clickable buttons to take you to the point in your code which caused
the problem.

Multitasking
------------

All scripts under hat blocks generally run to completion when that
script is triggered, before the screen is updated. The exceptions are:

-  when an ‘and wait’ call is made, e.g., ``broadcast_and_wait()``;
-  during a ``while`` or ``for`` loop: one iteration of the loop runs
   per display frame.

TODO: Other syscalls also suspend for a frame; check and document
this.

One consequence of this is that if you have a very complex piece of
processing inside an event handler, your project might appear to have
crashed. Try to keep things simple!

Privacy
-------

No project code ever leaves your browser. Everything you create is
stored locally.
