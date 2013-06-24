Tinned Django v.0.1
-------------------

.. image:: https://travis-ci.org/futurecolors/tinned-django.png?branch=master
    :target: https://travis-ci.org/futurecolors/tinned-django

Tinned Django is a custom project template used at `Future Colors`_.
Meant to be used with python 2.6-2.7.

.. note::
    This is **NOT** a general purpose template.
    It's focused on our workflow and shared for curious people out there.

Goals
~~~~~

Enforce best practices for new projects based on Django.

* New style folder structure (1.4+)
* `Class-based settings`_ for different environments with sane defaults
* Separate LocalSettings for every developer
* Useful batteries are included (see `requirements.txt`_)
* Comprehensive .gitignore

Usage
~~~~~

Install Django 1.4+ so that ``django-admin.py`` is available.

Open tinned can with Django::

    $ django-admin.py startproject <yourprojectname> --template https://github.com/futurecolors/tinned-django/zipball/master --extension py,gitignore
    $ mv tinned_django/<yourprojectname> <yourprojectname>
    $ rm -r tinned_django

Environments
^^^^^^^^^^^^

:BaseSettings:  Defaults for all other environments, safe and sound
:Development:   Local development
:Testing:       Running tests
:Staging:       Pre-production, for per-release deploys
:Production:    No comments

Contributing
~~~~~~~~~~~~
::

    $ pip install -r requirements.txt
    $ nosetests

Changelog
~~~~~~~~~

0.2 (24-06-2012)
^^^^^^^^^^^^^^^^
* Added waffle, floppyforms, extensions.

0.1 (22-06-2012)
^^^^^^^^^^^^^^^^
* First proper release

Previous (undocumented) version of tinned-django is available in `ancient`_ branch.

See also
~~~~~~~~

* `Andrew McCloud's template`_
* `Django HTML5Boilerplate and Twitter Bootstrap template`_


.. _Future Colors: http://futurecolors.ru
.. _Class-based settings: http://django-configurations.readthedocs.org/
.. _requirements.txt: https://github.com/futurecolors/tinned-django/blob/master/tinned_django/requirements.txt
.. _ancient: https://github.com/futurecolors/tinned-django/tree/ancient
.. _Django HTML5Boilerplate and Twitter Bootstrap template: https://github.com/xenith/django-base-template
.. _Andrew McCloud's template: https://github.com/amccloud/django-project-skel

