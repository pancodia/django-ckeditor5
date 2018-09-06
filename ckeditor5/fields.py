# -*- coding: utf-8 -*-
# @Author: panc25
# @Date:   2018-09-05 16:07:04
# @Last Modified by:   panc25
# @Last Modified time: 2018-09-05 21:20:10

from __future__ import absolute_import

from django import forms
from django.db import models

from .widgets import CKEditorWidget


class RichTextField(models.TextField):

    def __init__(self, *args, **kwargs):
        self.config_name = kwargs.pop('config_name', 'default')
        super(RichTextField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': self._get_form_class(),
            'config_name': self.config_name,
        }
        defaults.update(kwargs)
        return super(RichTextField, self).formfield(**defaults)

    @staticmethod
    def _get_form_class():
        return RichTextField


class RichTextFormField(forms.fields.CharField):

    def __init__(self, config_name='default', *args, **kwargs):
        kwargs.update({
            'widget': CKEditorWidget(config_name=config_name)
        })
        super(RichTextFormField, self).__init__(*args, **kwargs)
