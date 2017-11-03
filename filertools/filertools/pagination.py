# coding=utf-8
from __future__ import unicode_literals, absolute_import

from rest_framework.pagination import PageNumberPagination


class DefaultPagination(PageNumberPagination):
    page_size = 10
