# coding=utf-8
from __future__ import unicode_literals, absolute_import

from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar


@toolbar_pool.register
class FilerToolbar(CMSToolbar):

    def populate(self):
        menu = self.toolbar.get_or_create_menu('filer', _('Filer'))
        url = reverse('admin:filer_folder_changelist')
        menu.add_sideframe_item(_('Directories'), url=url)
