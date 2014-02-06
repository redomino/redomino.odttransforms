redomino.odttransforms
======================

It register a new portal transforms that let you generate odt files for a given .odt template.

This products is very simple: it just interpolates odt variables with the given ones you pass calling the transformer.
Therefore it performs just variable substitutions, not a real odt templating processor.
No external bynaries are needed, it depends on http://ooopy.sourceforge.net/.

This plugin is meant for developers, it could be used for generating odt files, write a custom PloneFormGen adapter, etc.

Usage
-----

Code:

    from zope.component import getUtility
    from Products.PortalTransforms.interfaces import IPortalTransformsTool
    file_contents = open('your odt file with variables').read()     # see redomino/odttransforms/tests/input.odt
    portal_transforms = getUtility(IPortalTransformsTool)
    converter = portal_transforms.convertTo(target_mimetype='application/vnd.oasis.opendocument.text.transformed',
                                            orig=file_contents,
                                            mimetype='application/vnd.oasis.opendocument.text',
                                            mapper=dict(plone_version='4.3.2-sunny-day-beta'),
                                           )
    transformed_odt_contents = converter.getData()



Authors
-------

* Davide Moro <davide.moro@redomino.com>

