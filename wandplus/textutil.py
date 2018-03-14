#!/usr/bin/env python

"""
Emulation functions of ImageMagick's automatic sizing feature

.. include:: summary/textutil.txt
"""

from wand.image import Image


def _calcSuitableFontsize_sub(size, f, f_low, f_high):
    f_mid = f_low + (f_high - f_low) // 2
    szL = f(f_low)
    szH = f(f_high)
    if abs(f_high - f_low) <= 1:
        if(f_high == size):
            return f_high
        else:
            return f_low

    if(szL > size):
        return _calcSuitableFontsize_sub(size, f, f_low//2, f_low)
    elif(szH < size):
        return _calcSuitableFontsize_sub(size, f, f_high, f_high*2)
    else:
        szM = f(f_mid)
        if szM < size:
            return _calcSuitableFontsize_sub(size, f, f_mid, f_high)
        else:
            return _calcSuitableFontsize_sub(size, f, f_low, f_mid)


def calcSuitableFontsize(draw, text, multiline=False, width=None, height=None):
    """calculate the font size from the specified image dimensions and text.

    :param draw: the drawing context
    :type draw: :class:`wand.drawing.Drawing`
    :param text: the source text.
    :type text: :class:`str`
    :param multiline: if True, `text` parameter is handled as multi line text.
                      otherwise, `text` is single line text.
    :type multiline: :class:`bool`
    :param width: the image width. if None, the value is automatically
                  calculated from `height`.
    :type width: :class:`numbers.Integral`
    :param height: the image height. if None, the value is automatically
                   calculated from `width`.
    :type height: :class:`numbers.Integral`
    :returns: if both `width` and `height` are None, returns None
              otherwise, returns the suitable font size.
    :rtype: :class:`numbers.Integral`
    """
    default_lower = 20
    default_upper = 40

    if width is None and height is None:
        return None
    else:
        w = width if width else 1
        h = height if height else 1
        with Image(width=w, height=h) as dummyimage:
            def f_x(fontsize):
                draw.font_size = fontsize
                mt = draw.get_font_metrics(dummyimage, text, multiline)
                return int(mt.text_width)

            def f_y(fontsize):
                draw.font_size = fontsize
                mt = draw.get_font_metrics(dummyimage, text, multiline)
                return int(mt.text_height)

            size = 0
            size_backup = draw.font_size
            if width and height:
                sizex = _calcSuitableFontsize_sub(w, f_x,
                                                  default_lower,
                                                  default_upper)
                sizey = _calcSuitableFontsize_sub(h, f_y,
                                                  default_lower,
                                                  default_upper)
                size = min(sizex, sizey)
            else:
                p = (w, f_x) if width else (h, f_y)
                size_backup = draw.font_size
                size = _calcSuitableFontsize_sub(p[0], p[1],
                                                 default_lower, default_upper)

            draw.font_size = size_backup
            return size


def calcSuitableImagesize(draw, text, multiline=False):
    """calculate the image dimensions from the specified text and font size.

    :param draw: the drawing context which has been set the font size.
    :type draw: :class:`wand.drawing.Drawing`
    :param text: the source text.
    :type text: :class:`str`
    :param multiline: if True, `text` parameter is handled as multi line text.
                      otherwise, `text` is single line text.
    :type multiline: :class:`bool`
    :returns: the pair of (`width`, `height`).
    :rtype: :class:`tuple`
    """
    with Image(width=1, height=1) as dummyimage:
        mt = draw.get_font_metrics(dummyimage, text, multiline)
        return (int(mt.text_width), int(mt.text_height+mt.y1))


if __name__ == '__main__':
    pass
