from Products.PortalTransforms.interfaces import ITransform
from zope.interface import implements


class OdtTransform:
    """
    Odt templating transform.

    Input: odt model
    Output: rendered odt
    """

    implements(ITransform)

    __name__ = "odt_transform"
    inputs = ('application/vnd.oasis.opendocument.text', )
    output = "application/vnd.oasis.opendocument.text.transformed"

    def __init__(self, name=None, **kwargs):
        self.conf = kwargs

        if name:
            self.__name__ = name

    def name(self):
        return self.__name__

    def convert(self, orig, data, **kwargs):
        from ooopy.Transformer import Transformer
        from ooopy import Transforms
        from StringIO import StringIO
        from ooopy.OOoPy import OOoPy
        sio = StringIO()
        ooo = OOoPy(infile=StringIO(orig), outfile=sio)
        ooo_mimetype = ooo.mimetype
        ppp = Transforms.get_meta(ooo_mimetype)
#        ttt = Transformer(ooo_mimetype, ppp)
        import pdb; pdb.set_trace()
        ttt = Transformer(ooo_mimetype,
                          Transforms.Autoupdate(),
                          Transforms.Editinfo(),
        #                  Transforms.Field_Replace(prio=99,
         #                                          replace=cb),
                          Transforms.Field_Replace(replace={'plone_version' : '4.3.2-sunny-day-beta',
                                                            }
                                                  ),
                          Transforms.Addpagebreak_Style(),
                          Transforms.Addpagebreak()
                         )
        ttt.transform(ooo)
        ooo.close()
        ov = sio.getvalue()
        data.setData(ov)
        return data


def register():
    return OdtTransform()
