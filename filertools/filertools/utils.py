# coding=utf-8
from __future__ import unicode_literals, absolute_import

from filer.models import Folder


def copy_filer_folder_structure(source_id=None, final_id=None):
    def create_sub_folders_for_folder(folder, destination):
        created_destination = \
            Folder.objects.create(name=folder, parent=destination)

        for f in folder.children.all():
            create_sub_folders_for_folder(f, created_destination)

    if not source_id or not final_id:
        return

    original_root = Folder.objects.get(id=source_id)
    destination_root = Folder.objects.get(id=final_id)
    for sub_folder in original_root.children.all():
        create_sub_folders_for_folder(sub_folder, destination_root)
