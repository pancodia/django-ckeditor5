Django CKEditor 5
===

<!-- MarkdownTOC levels="1,2" autolink='true' -->

- [Introduction](#introduction)
- [Installation](#installation)

<!-- /MarkdownTOC -->


# Introduction #

Django CKEditor 5 integrates [CKEditor 5](https://ckeditor.com/ckeditor-5/) with Django. The purpose of this package is the same as that of [the original django-ckeditor](https://github.com/django-ckeditor/django-ckeditor) except that we use CKEditor 5 while the original package uses [CKEditor 4](https://ckeditor.com/ckeditor-4/). 

According to [ckeditor.com](https://ckeditor.com/docs/ckeditor5/latest/builds/guides/migrate.html):

>When compared to its predecessor, CKEditor 5 should be considered a totally new editor.

The implementation follows the structure of [ckeditor in django-ckeditor](https://github.com/django-ckeditor/django-ckeditor/tree/master/ckeditor). So the usage should be very similar. The differences are:

- `static/ckeditor5` contains the build of the classic ckeditor 5 v11.0.1. It was downloaded as a zip file from [CKEditor 5's download page](https://ckeditor.com/ckeditor-5/download/).
- There is no `extraPlugins` in CKEditor 5. So the codes (in python, html, javascript) related to external plugins or external plugin resources are removed.
- `static/ckeditor5/ckeditor-init.js` is modified. In the `initialiseCKEditor` function:
    + The part that handles external plugins configuration  is removed. 
    + Instead of `CKEDITOR.replace`, CKEditor 5 uses `ClassicEditor.create` to initialize/create an editor.

# Installation #


