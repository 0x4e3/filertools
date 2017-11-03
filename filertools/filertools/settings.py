# coding=utf-8
from __future__ import unicode_literals, absolute_import

from django.conf import settings


FILERTOOLS_FOLDERS_DENY_COPY_TO = getattr(
    settings, 'FILERTOOLS_FOLDERS_DENY_COPY_TO', [])
