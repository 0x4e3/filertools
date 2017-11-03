# coding=utf-8
from __future__ import unicode_literals, absolute_import

from django.core import urlresolvers
from django.db import models
from django.utils.translation import ugettext_lazy as _

from filer.models import File


class OrderedFile(File):
    order = models.PositiveIntegerField(_('order'))

    class Meta(File.Meta):
        ordering = ['order']

    def save(self, *args, **kwargs):
        """
        Overrides `filer.File` `save` method to set `order` field value
        to newly uploaded files.
        """
        if not self.pk:
            max_order = OrderedFile.objects.\
                filter(folder_id=self.folder_id).\
                aggregate(models.Max('order'))
            try:
                next_order = max_order['order__max'] + 1
            except TypeError:
                next_order = 1
            self.order = next_order
        super(OrderedFile, self).save(*args, **kwargs)

    def get_admin_change_url(self):
        """
        Gets change view url for original model.

        We don't want to change default change view, so overriding method to
        pass original url to the template.

        :return: <str> -- change view url
        """
        model_name = File._meta.model_name
        filer_app_name = File._meta.app_label
        return urlresolvers.reverse(
            'admin:{0}_{1}_change'.format(filer_app_name, model_name),
            args=(self.pk,))

    def get_admin_delete_url(self):
        """
        Gets delete view url for original model.

        We don't want to change default delete view, so overriding method to
        pass original url to the template.

        :return: <str> -- delete view url
        """
        model_name = File._meta.model_name
        filer_app_name = File._meta.app_label
        return urlresolvers.reverse(
            'admin:{0}_{1}_delete'.format(filer_app_name, model_name),
            args=(self.pk,))
