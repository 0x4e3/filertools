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
        'filertools.filerface',
        ...
        'filer',
        ...
        'filertools.filertools',
        ...
    )

Specify custom filer File model:

.. code-block:: python

    FILER_FILE_MODELS = ['filertools.filertools.models.OrderedFile']

Add filertools's URL patterns:

.. code-block:: python

    from filertools import urls as filertools_urls


    urlpatterns = [
        ...
        url(r'^filer-api/', include('filertools.filertools.urls')),
        ...
    ]

Features
--------

* Filer menu on django-cms toolbar.
* Filer files custom ordering in the directory listing view.
* Async folder searching for files copy and move.
* Coping of folder tree structure.

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox
