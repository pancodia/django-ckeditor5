import os, sys


sys.path.append(os.path.abspath('..'))

extensions = []

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'Django CKEditor 5'
copyright = u'2018 The Django-CKEditor Team and Pan Chao'

version = __import__('ckeditor5').__version__
release = version

pygments_style = 'sphinx'

html_theme = 'default'

html_static_path = ['_static']

htmlhelp_basename = 'DjangoCKEditor5doc'

latex_documents = [(
    'index',
    'DjangoCKEditor5.tex',
    u'Django CKEditor 5 Documentation',
    u'The Django-CKEditor Team and Pan Chao',
    'manual',
)]

man_pages = [(
    'index',
    'djangoCKEditor5',
    u'Django CKEditor 5 Documentation',
    [u'The Django-CKEditor Team and Pan Chao'],
    1,
)]

texinfo_documents = [(
    'index',
    'DjangoCKEditor5',
    u'Django CKEditor 5 Documentation',
    u'The Django-CKEditor Team and Pan Chao',
    'DjangoCKEditor5',
    'CKEditor 5 integration for Django',
    'Miscellaneous',
)]