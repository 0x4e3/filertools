# coding=utf-8
from __future__ import unicode_literals, absolute_import

from django.core.management.base import BaseCommand, CommandError

from filer.models import Folder
from filertools.filertools.models import OrderedFile


class Command(BaseCommand):
    help = 'Fixes ordering for specified folder or for whole tree'

    def __init__(self, stdout=None, stderr=None, no_color=False):
        self.rebuilt_folders_count = 0
        super(Command, self).__init__(stdout, stderr, no_color)

    def add_arguments(self, parser):
        parser.add_argument('folder_id', nargs='?', type=int, default=None)

        parser.add_argument('with_children', nargs='?',
                            type=bool, default=True)

    def process_folder(self, folder):
        ordered_files = OrderedFile.objects.filter(folder_id=folder.id)
        orders = [order for order in range(len(ordered_files))][::-1]
        for ordered_file in ordered_files:
            ordered_file.order = orders.pop()
            ordered_file.save()
        self.rebuilt_folders_count += 1

    def traverse_folders_tree(self, folder, with_children):
        self.process_folder(folder)

        if not with_children:
            return

        children = folder.children.all()
        for child in children:
            self.traverse_folders_tree(child, with_children)
        return

    def handle(self, *args, **options):
        if options['folder_id']:
            try:
                folder = Folder.objects.get(id=options['folder_id'])
            except Folder.DoesNotExist:
                raise CommandError('Incorrect folder id')
            folders = [folder]
        else:
            folders = Folder.objects.filter(parent=None)

        for folder in folders:
            self.traverse_folders_tree(folder, options['with_children'])

        if self.rebuilt_folders_count:
            self.stdout.write(
                self.style.SUCCESS(
                    'Successfully rebuilt {} '
                    'folders'.format(self.rebuilt_folders_count)))
