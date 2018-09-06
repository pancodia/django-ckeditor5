/*
* @Author: panc25
* @Date:   2018-09-05 14:27:55
* @Last Modified by:   panc25
* @Last Modified time: 2018-09-06 14:05:01
*/

/* global CKEDITOR */
;(
    function() {
        var el = document.getElementById('ckeditor-init-script');
        if (el && !window.CKEDITOR_BASEPATH) {
            window.CKEDITOR_BASEPATH = el.getAttribute('data-ckeditor-basepath');
        }

        // Polyfill from https://developer.mozilla.org/en/docs/Web/API/Element/matches
        if (!Element.prototype.matches) {
            Element.prototype.matches =
                Element.prototype.matchesSelector ||
                Element.prototype.mozMatchesSelector ||
                Element.prototype.msMatchesSelector ||
                Element.prototype.oMatchesSelector ||
                Element.prototype.webkitMatchesSelector ||
                function(s) {
                    var matches = (this.document || this.ownerDocument).querySelectorAll(s),
                        i = matches.length;
                    while (--i >= 0 && matches.item(i) !== this) {}
                    return i > -1;
                };
        }

        function runInitialisers() {
            initialiseCKEditor();
            initialiseCKEditorInInlinedForms();
        }

        if (document.readyState != 'loading') {
            runInitialisers();
        } else {
            document.addEventListener('DOMContentLoaded', runInitialisers);
        }

        // Initialize CKEditors for all the textareas on the page
        function initialiseCKEditor() {
            // Any textarea tag with data-type=ckeditortype is replaced by CKEditor
            var textareas = Array.prototype.slice.call(
                document.querySelectorAll('textarea[data-type=ckeditortype]')
            );
            for (var i=0; i<textareas.length; ++i) {
                var t = textareas[i];
                if (t.getAttribute('data-processed') == '0' && t.id.indexOf('__prefix__') == -1) {
                    t.setAttribute('data-processed', '1');
                    // CKEDITOR.replace(t.id, JSON.parse(t.getAttribute('data-config')));  // CKEditor 4
                    ClassicEditor
                        .create(document.querySelector('#'+t.id),
                                JSON.parse(t.getAttribute('data-config')))
                        .catch( error => {
                            console.log( error );
                        });
                }
            }
        }

        function initialiseCKEditorInInlinedForms() {
            document.body.addEventListener(
                'click',
                function(e) {
                    if (e.target && (
                        e.target.matches('.add-row a') ||
                        e.target.matches('.grp-add-handler')
                    )) {
                        initialiseCKEditor();
                    }
                });
        }

    }()
);
