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
        
        ttt = Transformer(ooo_mimetype,
                          Transforms.Field_Replace(replace=kwargs.get('mapper', {})),
                         )
        ttt.transform(ooo)
        ooo.close()
        ov = sio.getvalue()
        data.setData(ov)
        return data


def register():
    return OdtTransform()
