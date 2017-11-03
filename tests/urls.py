# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from filertools.filertools.urls import urlpatterns as filertools_urls

urlpatterns = [
    url(r'^', include(filertools_urls, namespace='filertools')),
]
