=====
Usage
=====

To use filertools in a project, add it to your `INSTALLED_APPS`:

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
