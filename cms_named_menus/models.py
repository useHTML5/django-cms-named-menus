# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from autoslug.fields import AutoSlugField
from jsonfield import JSONField
import collections


class CMSNamedMenu(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    slug = AutoSlugField(always_update=True, populate_from='name')
    pages = JSONField(blank=True, null=True, verbose_name="Редактирование меню",
                      load_kwargs={
                          'object_hook': collections.OrderedDict
                      },
                      default=[])

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"
