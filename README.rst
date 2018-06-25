=====================
plonetheme.transition
=====================

`Transition Theme`_, is an installable Diazo theme for Plone 4 developed 
by `Guido Stevens`_.


Introduction
============

The ``plonetheme.transition`` package uses the *theming & packaging* features
available in `plone.app.theming`_ to make the theme `Transition Theme`_ easily
available in *Plone 4*.


Requirements
============

- From the Plone 4.1.x To the Plone 4.3 latest version (https://plone.org/download)
- The ``plone.app.theming`` package (*will be installed as a dependency of this package*)


Screenshots
===========

Layout of the site when viewed in a computer resolution:

.. image:: https://github.com/collective/plonetheme.transition/raw/master/screenshot.png


Features
========

- It's an installable Plone Theme package.
- After installation from Add-ons controlpanel, this theme is enabled automatically.
- It's have support for clean uninstallation.
- Also it's a simple Diazo package (Zip file).


Installation
============


Zip file
--------

If you are an end user, you might enjoy installation via zip file import.

1. Download a `zip file <https://github.com/collective/plonetheme.transition/raw/master/transition.zip>`_.
2. Import the theme from the Diazo theme control panel.

Enabling the theme
^^^^^^^^^^^^^^^^^^

Select and enable the theme from the Diazo control panel. That's it!


Buildout
--------

If you are a developer, you might enjoy installing it via buildout.

For install ``plonetheme.transition`` package add it to your ``buildout`` section's 
*eggs* parameter e.g.: ::

   [buildout]
    ...
    eggs =
        ...
        plonetheme.transition


and then running ``bin/buildout``.

Or, you can add it as a dependency on your own product ``setup.py`` file: ::

    install_requires=[
        ...
        'plonetheme.transition',
    ],


Contribute
==========

- Issue Tracker: https://github.com/collective/plonetheme.transition/issues
- Source Code: https://github.com/collective/plonetheme.transition


License
=======

The project is licensed under the GPLv2.

Credits
-------

- Guido Stevens (guido.stevens at cosent dot net).

Contributors
------------

- Leonardo J. Caballero G. (leonardocaballero at gmail dot com).


.. _`Transition Theme`: https://templated.co/transition
.. _`Guido Stevens`: https://twitter.com/GuidoStevens
.. _`plone.app.theming`: https://pypi.org/project/plone.app.theming/
