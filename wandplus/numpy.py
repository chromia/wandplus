#!/usr/bin/env python

from wand.image import Image
from wand.color import Color
from wand.compat import string_type
from wandplus.image import STORAGE_TYPES, exportpixels, importpixels
import numbers
import numpy


_channellist = {
    1: 'I',
    3: 'RGB',
    4: 'RGBA'
}
_channellist_rev = {
    1: 'I',
    3: 'BGR',
    4: 'BGRA'
}


def numpy2wand(npimage, storage='char', bgr=False):
    """converts numpy-styled image to Wand image.

    :param npimage: numpy image.
    :type npimage: :class:`numpy.ndarray`
    :param storage: the storage type represents size of the pixel.
                    this value must be defined in wand.image.STORAGE_TYPES.
                      'char': unsigned char [0..255]  ('uint8' in numpy)
                      'short': unsigned short [0..65535] ('uint16' in numpy)
                      'integer': unsigned int [0..2^32] ('uint32' in numpy)
                      'float': 32bit-float ('float32' in numpy)
                      'double': 64bit-float ('float64' in numpy)
    :type storage: :class:`str`
    :param bgr: if True, replace the order of the channels
                         from B,G,R-order to R,G,B-order(option for opencv).
    :type bgr: :class:`bool`
    :return: converted Wand image
    :rtype: :class:`wand.image.Image`
    """
    if len(npimage.shape) == 1:
        (height, width, channels) = (1, *npimage.shape, 1)
    if len(npimage.shape) == 2:
        (height, width, channels) = (*npimage.shape, 1)
    elif len(npimage.shape) == 3:
        (height, width, channels) = npimage.shape
    else:
        raise ValueError('the image has over 4-dimentions is not supported.')
    if storage not in STORAGE_TYPES:
        raise ValueError('expected string from STORAGE_TYPES, not ' +
                         repr(storage))
    elif not isinstance(bgr, bool):
        raise TypeError('bgr must be a bool, not ' +
                        repr(bgr))

    wandimage = Image(width=width, height=height, background=Color('white'))
    if channels in _channellist:
        if bgr:
            channelmap = _channellist_rev[channels]
        else:
            channelmap = _channellist[channels]
    else:
        raise ValueError('the image which has ' + channels +
                         'channels is not supported,' +
                         '1 or 3 or 4 channel-image is expected.')
    importpixels(wandimage, 0, 0, width, height, channelmap, storage,
                 npimage.flatten().tolist())
    return wandimage


def wand2numpy(wandimage, channels=3, storage='char', bgr=False):
    """converts Wand image to numpy-styled image.

    :param wandimage: Wand image.
    :type wandimage: :class:`wand.image.Image`
    :param channels: the numbers of the channels picked up
                     from the source image.
                       1: grayscale image
                       3: color image with R,G,B channels
                       4: color image with R,G,B,A channels
    :type channels: :class:`numbers.Integral`
    :param storage: the storage type represents size of the pixel.
                    this value must be defined in wand.image.STORAGE_TYPES.
                      'char': unsigned char [0..255]  ('uint8' in numpy)
                      'short': unsigned short [0..65535] ('uint16' in numpy)
                      'integer': unsigned int [0..2^32] ('uint32' in numpy)
                      'float': 32bit-float ('float32' in numpy)
                      'double': 64bit-float ('float64' in numpy)
    :type storage: :class:`str`
    :param bgr: if True, replace the order of the color channels
                         from B,G,R-order to R,G,B-order(option for opencv).
    :return: converted numpy image
    :rtype: :class:`numpy.ndarray`
    """
    if isinstance(channels, string_type):
        channelmap = channels
    else:
        if not isinstance(channels, numbers.Integral):
            raise TypeError('channels has to be a numbers.Integral, not ' +
                            repr(channels))
        elif channels in _channellist:
            if bgr:
                channelmap = _channellist_rev[channels]
            else:
                channelmap = _channellist[channels]
        else:
            raise ValueError('expected value is 1 or 2 or 4, ' +
                             '{0} is not supported.'.format(channels))
    if storage not in STORAGE_TYPES:
        raise ValueError('expected string from STORAGE_TYPES, not ' +
                         repr(storage))
    elif not isinstance(bgr, bool):
        raise TypeError('bgr must be a bool, not ' +
                        repr(bgr))

    pixels = exportpixels(wandimage, 0, 0, wandimage.width, wandimage.height,
                          channelmap, storage)
    shape = (wandimage.height, wandimage.width, channels)
    npimage = numpy.reshape(pixels, shape)
    return npimage


if __name__ == '__main__':
    pass
