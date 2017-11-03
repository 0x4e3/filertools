# coding=utf-8
from __future__ import unicode_literals, absolute_import

from filer.models import Folder
from rest_framework import viewsets

from filertools.filertools import settings
from filertools.filertools.pagination import DefaultPagination
from filertools.filertools.serializers import FilerFolderModelSerializer


class FilerFolderViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Folder.objects.none()
    pagination_class = DefaultPagination
    serializer_class = FilerFolderModelSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q')
        if not query:
            return self.queryset
        selected_folders = self.request.query_params.getlist('folders[]')

        excluded_folders_ids = settings.FILERTOOLS_FOLDERS_DENY_COPY_TO

        if selected_folders:
            excluded_folders_ids += selected_folders

        folders = Folder.objects.\
            filter(name__istartswith=query).\
            exclude(id__in=excluded_folders_ids).\
            exclude(parent_id__in=excluded_folders_ids).\
            exclude(parent__parent_id__in=excluded_folders_ids).\
            exclude(parent__parent__parent_id__in=excluded_folders_ids).\
            exclude(parent__parent__parent__parent_id__in=excluded_folders_ids)

        available_folders = []
        for folder in folders:
            if folder.has_read_permission(self.request):
                available_folders.append(folder)
        return available_folders
