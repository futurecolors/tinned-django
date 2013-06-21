Tinned Django
-------------

Tinned Django is a custom project template used at `Future Colors`_.

.. warning::
    Work in progress!

.. note::
    This is **NOT** a general purpose template.
    It's focused on our workflow and shared for curious people out there.

Goals
~~~~~

Enforce best practices for new projects based on Django.

* New style folder structure (1.4+)
* `Class-based settings`_ for different environments
* Separate LocalSettings for every developer
* Must-have batteries are included (see requirements.txt)
* Comprehensive .gitignore

Usage
~~~~~

Since Django doesn't support arbitrary custom variables in project
tempates by default it's preferred way to install and create new project

* ``pip install tinned-django``
* ``open_can <yourprojectname> --var=XXX=yyy``

However, if you wish to use default startproject command without extra
variables substitution::

* ``django-admin.py startproject <yourprojectname> --template https://github.com/futurecolors/tinned-django/zipball/master --extension py,md,gitignore`

History
~~~~~~~

Previous (unreleased) version of tinned-django is available in ``ancient`` branch.

See also
~~~~~~~~

* `Andrew McCloud's template`_
* `Django HTML5Boilerplate and Twitter Bootstrap template`_


.. _Future Colors: http://futurecolors.ru
.. _Class-based settings: http://django-configurations.readthedocs.org/
.. _Django HTML5Boilerplate and Twitter Bootstrap template: https://github.com/xenith/django-base-template
.. _Andrew McCloud's template:: https://github.com/amccloud/django-project-skel

