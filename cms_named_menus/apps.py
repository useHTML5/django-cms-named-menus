# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.apps import AppConfig


class CMSNamedMenusConfig(AppConfig):
    name = 'cms_named_menus'
    verbose_name = 'Редактирование меню'

    def ready(self):
        import cms_named_menus.signals

