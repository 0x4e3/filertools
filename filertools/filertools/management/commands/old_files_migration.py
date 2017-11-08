# coding=utf-8
from __future__ import unicode_literals, absolute_import

from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from filer.models import File
from filertools.filertools.models import OrderedFile


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        created_files_count = 0

        ordered_file_content_type = \
            ContentType.objects.get_for_model(OrderedFile)

        for filer_file in File.objects.all():
            try:
                filer_file.orderedfile
            except OrderedFile.DoesNotExist:
                ordered_file = OrderedFile(file_ptr_id=filer_file.id)
                ordered_file.__dict__.update(filer_file.__dict__)
                ordered_file.polymorphic_ctype = ordered_file_content_type
                ordered_file.order = 1
                ordered_file.save()
                created_files_count += 1
            else:
                # already has ordered file
                continue

        if created_files_count:
            # ToDo (vladimir@makhlay.com): add management command ordering rebuild call after implementation
            self.stdout.write(
                self.style.SUCCESS(
                    'Successfully created {} '
                    'OrderedFile`s'.format(created_files_count)))
