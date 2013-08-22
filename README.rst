Tinned Django v.0.3
-------------------

.. image:: https://travis-ci.org/futurecolors/tinned-django.png?branch=master
    :target: https://travis-ci.org/futurecolors/tinned-django

Tinned Django is a custom project template used at `Future Colors`_.
Meant to be used with python 2.7.

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

These are defaults for all kinds of environments, specified by ``DJANGO_CONFIGURATION``
They're defined in ``{{ project_name}}.settings`` module.

:BaseSettings:  Defaults for all other environments, safe and sound
:BaseLive:      Local development
:Live:          Real-time updates, includes local settings per developer
:Testing:       Running tests in CI/locally
:Dev:           Nightly/daily/hourly builds for QA and other folks
:Rc:            Pre-production, for per-release deploys
:Production:    No comments


Local settings
^^^^^^^^^^^^^^

Local settings, for each developer that are in effect in ``Live`` environment
are defined in ``{{ project_name}}.live_settings`` module.
Each mixin should be regular CBS mixin, named after developer USER env variable
with first letter captialized. Example: ``USER=prophet -> class Prophet(object): pass``
These settings are checked into repository for easy developement.


Contributing
~~~~~~~~~~~~
::

    $ pip install -r requirements.txt
    $ nosetests


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

