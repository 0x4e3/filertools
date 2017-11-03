=============================
filertools
=============================

.. image:: https://badge.fury.io/py/filertools.svg
    :target: https://badge.fury.io/py/filertools

.. image:: https://travis-ci.org/0x4e3/filertools.svg?branch=master
    :target: https://travis-ci.org/0x4e3/filertools

.. image:: https://codecov.io/gh/0x4e3/filertools/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/0x4e3/filertools

django-filer tools and extentions

Documentation
-------------

The full documentation is at https://filertools.readthedocs.io.

Quickstart
----------

Install filertools::

    pip install filertools

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'filertools.apps.FilertoolsConfig',
        ...
    )

Add filertools's URL patterns:

.. code-block:: python

    from filertools import urls as filertools_urls


    urlpatterns = [
        ...
        url(r'^', include(filertools_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
