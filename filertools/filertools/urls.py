# coding=utf-8
from django.conf.urls import url

from filertools.filertools import api

filer_folders = (
    api.FilerFolderViewSet.as_view({
        'get': 'list'
    })
)

urlpatterns = [
    url(r'^filer/folder/', filer_folders, name='filer_folders_list'),
]
