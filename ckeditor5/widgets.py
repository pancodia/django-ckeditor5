# -*- coding: utf-8 -*-
# @Author: panc25
# @Date:   2018-09-05 13:56:55
# @Last Modified by:   panc25
# @Last Modified time: 2018-09-05 21:17:20

from __future__ import absolute_import

from django import forms
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.core.serializers.json import DjangoJSONEncoder
try: from django.utils.encoding import force_str
except: from django.utils.encoding import force_text as force_str
from django.utils.functional import Promise
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.utils.translation import get_language
try:
    from django.forms.widgets import get_default_renderer
except ImportError:
    from django.forms.renderers import get_default_renderer

from js_asset import JS, static

try:
    # Django >= 1.7
    from django.forms.utils import flatatt
except ImportError:
    # Django < 1.7
    from django.forms.util import flatatt


class LazyEncoder(DjangoJSONEncoder):

    def default(self, obj):
        if isinstance(obj, Promise):
            return force_str(obj)
        return super(LazyEncoder, self).default(obj)


json_encode = LazyEncoder().encode

DEFAULT_CONFIG = {
    'toolbar': ['Source', '-', 'Bold', 'Italic'],
}


class CKEditorWidget(forms.Textarea):
    """Widget providing CKEditor for Rich Text Editing.

    This widget supports direct image uploads and embed.
    """
    class Media:
        js = (
            JS('ckeditor5/ckeditor-init.js',
                {
                    'id': 'ckeditor-init-script',
                    'data-ckeditor-basepath': getattr(
                        settings,
                        'CKEDITOR_BASEPATH',
                        static('ckeditor5/ckeditor_build_classic/'),
                    ),
                }),
            'ckeditor5/ckeditor_build_classic/ckeditor.js',
        )

    def __init__(self, config_name='default', *args, **kwargs):
        super(CKEditorWidget, self).__init__(*args, **kwargs)
        # Setup config from defaults
        self.config = DEFAULT_CONFIG.copy()

        # Try to get valid config from settings
        configs = getattr(settings, 'CKEDITOR_CONFIGS', None)  # CKEditor 5 configuration in settings
        if configs:
            if isinstance(configs, dict):
                # Make sure the config_name exists
                if config_name in configs:
                    config = configs[config_name]
                    # Make sure the configurations is a dictionary
                    if not isinstance(config, dict):
                        raise ImproperlyConfigured('CKEDITOR_CONFIGS["%s"] \
                                setting must be a dictionary type.' %
                                                        config_name)
                    # Override defaults with settings config
                    self.config.update(config)
                else:
                    raise ImproperlyConfigured("No configuration named '%s' \
                            found in your CKEDITOR_CONFIGS setting." %
                                                    config_name)
            else:
                raise ImproperlyConfigured('CKEDITOR_CONFIGS setting must be a\
                        dictionary type.')

    def render(self, name, value, attrs=None, renderer=None):
        if renderer is None:
            renderer = get_default_renderer()

        if value is None:
            value = ''

        final_attrs = self.build_attrs(self.attrs, attrs, name=name)
        self._set_config()

        context = {
            'final_attrs': flatatt(final_attrs),
            'value': conditional_escape(force_str(value)),
            'id': final_attrs['id'],
            'config': json_encode(self.config),
        }

        return mark_safe(renderer.render('ckeditor5/widget.html', context))

    def build_attrs(self, base_attrs, extra_attrs=None, **kwargs):
        """Helper function to build an attribute dictionary.

        This is a combination of the same method from Django<=1.10 and Django1.11+

        :param base_attrs: [description]
        :type base_attrs: [type]
        :param **kwargs: [description]
        :type **kwargs: [type]
        :param extra_attrs: [description], defaults to None
        :type extra_attrs: [type], optional
        """
        attrs = dict(base_attrs, **kwargs)
        if extra_attrs:
            attrs.update(extra_attrs)
        return attrs

    def _set_config(self):
        lang = get_language()
        if lang == 'zh-hans':
            lang = 'zh-cn'
        elif lang == 'zh-hant':
            lang = 'zh'
        self.config['language'] = lang
