from wand.image import CHANNELS, FILTER_TYPES
from wand.api import library, libmagick
from wand.drawing import Drawing
from wand.color import Color
from wand.compat import string_type
import numbers
import ctypes
import collections

libmagick.AcquireKernelInfo.restype = ctypes.c_void_p
libmagick.AcquireKernelInfo.argtypes = [
    ctypes.c_char_p
]
libmagick.DestroyKernelInfo.restype = ctypes.c_void_p
libmagick.DestroyKernelInfo.argtypes = [
    ctypes.c_void_p
]
library.MagickAdaptiveBlurImage.restype = ctypes.c_bool
library.MagickAdaptiveBlurImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double,
    ctypes.c_double
]
library.MagickAddNoiseImage.restype = ctypes.c_bool
library.MagickAddNoiseImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int
]
library.MagickAutoGammaImage.restype = ctypes.c_bool
library.MagickAutoGammaImage.argtypes = [
    ctypes.c_void_p
]
library.MagickAutoLevelImage.restype = ctypes.c_bool
library.MagickAutoLevelImage.argtypes = [
    ctypes.c_void_p
]
library.MagickBlackThresholdImage.restype = ctypes.c_bool
library.MagickBlackThresholdImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p
]
library.MagickBlurImage.restype = ctypes.c_bool
library.MagickBlurImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double,
    ctypes.c_double
]
library.MagickBrightnessContrastImage.restype = ctypes.c_bool
library.MagickBrightnessContrastImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double,
    ctypes.c_double
]
library.MagickCharcoalImage.restype = ctypes.c_bool
library.MagickCharcoalImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double,
    ctypes.c_double
]
library.MagickChopImage.restype = ctypes.c_bool
library.MagickChopImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.c_size_t,
    ctypes.c_ssize_t,
    ctypes.c_ssize_t
]
library.MagickClutImage.restype = ctypes.c_bool
library.MagickClutImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p
]
library.MagickColorizeImage.restype = ctypes.c_bool
library.MagickColorizeImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_void_p
]
library.MagickCommentImage.restype = ctypes.c_bool
library.MagickCommentImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p
]
library.MagickContrastImage.restype = ctypes.c_bool
library.MagickContrastImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_bool
]
library.MagickConvolveImage.restype = ctypes.c_bool
library.MagickConvolveImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.POINTER(ctypes.c_double)
]
library.MagickCycleColormapImage.restype = ctypes.c_bool
library.MagickCycleColormapImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_ssize_t
]
library.MagickDespeckleImage.restype = ctypes.c_bool
library.MagickDespeckleImage.argtypes = [
    ctypes.c_void_p
]
library.MagickEdgeImage.restype = ctypes.c_bool
library.MagickEdgeImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double
]
library.MagickEmbossImage.restype = ctypes.c_bool
library.MagickEmbossImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double,
    ctypes.c_double
]
library.MagickEnhanceImage.restype = ctypes.c_bool
library.MagickEnhanceImage.argtypes = [
    ctypes.c_void_p
]
library.MagickExtentImage.restype = ctypes.c_bool
library.MagickExtentImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.c_size_t,
    ctypes.c_ssize_t,
    ctypes.c_ssize_t
]
library.MagickHaldClutImage.restype = ctypes.c_bool
library.MagickHaldClutImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p
]
library.MagickImplodeImage.restype = ctypes.c_bool
library.MagickImplodeImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double
]
library.MagickLabelImage.restype = ctypes.c_bool
library.MagickLabelImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p
]
library.MagickMagnifyImage.restype = ctypes.c_bool
library.MagickMagnifyImage.argtypes = [
    ctypes.c_void_p
]
library.MagickMinifyImage.restype = ctypes.c_bool
library.MagickMinifyImage.argtypes = [
    ctypes.c_void_p
]
library.MagickMorphologyImage.restype = ctypes.c_bool
library.MagickMorphologyImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_ssize_t,
    ctypes.c_void_p
]
library.MagickMotionBlurImage.restype = ctypes.c_bool
library.MagickMotionBlurImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double
]
library.MagickOilPaintImage.restype = ctypes.c_bool
library.MagickOilPaintImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double
]
library.MagickOpaquePaintImage.restype = ctypes.c_bool
library.MagickOpaquePaintImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_double,
    ctypes.c_bool
]
library.MagickOrderedPosterizeImage.restype = ctypes.c_bool
library.MagickOrderedPosterizeImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p
]
library.MagickPolaroidImage.restype = ctypes.c_bool
library.MagickPolaroidImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_double
]
library.MagickPosterizeImage.restype = ctypes.c_bool
library.MagickPosterizeImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.c_bool
]
library.MagickRaiseImage.restype = ctypes.c_bool
library.MagickRaiseImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.c_size_t,
    ctypes.c_ssize_t,
    ctypes.c_ssize_t,
    ctypes.c_bool
]
library.MagickRandomThresholdImage.restype = ctypes.c_bool
library.MagickRandomThresholdImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.c_size_t
]
library.MagickRemapImage.restype = ctypes.c_bool
library.MagickRemapImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_int
]
library.MagickResampleImage.restype = ctypes.c_bool
library.MagickResampleImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_int,
    ctypes.c_double
]
library.MagickRollImage.restype = ctypes.c_bool
library.MagickRollImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_ssize_t,
    ctypes.c_ssize_t
]
library.MagickShadeImage.restype = ctypes.c_bool
library.MagickShadeImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_bool,
    ctypes.c_double,
    ctypes.c_double
]
library.MagickShadowImage.restype = ctypes.c_bool
library.MagickShadowImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_ssize_t,
    ctypes.c_ssize_t
]
library.MagickShaveImage.restype = ctypes.c_bool
library.MagickShaveImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.c_size_t
]
library.MagickShearImage.restype = ctypes.c_bool
library.MagickShearImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_double,
    ctypes.c_double
]
library.MagickSparseColorImage.restype = ctypes.c_bool
library.MagickSparseColorImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_size_t,
    ctypes.POINTER(ctypes.c_double)
]
library.MagickSpreadImage.restype = ctypes.c_bool
library.MagickSpreadImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_double
]
library.MagickWaveImage.restype = ctypes.c_bool
library.MagickWaveImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double,
    ctypes.c_double
]
library.MagickWhiteThresholdImage.restype = ctypes.c_bool
library.MagickWhiteThresholdImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p
]

DITHER_METHODS = ('undefined', 'nodither', 'riemersma', 'floydsteinberg')

MORPHOLOGY_METHODS = ('undefined', 'convolve', 'correlate', 'erode', 'dilate',
                      'erodeintensity', 'dilateintensity', 'distance',
                      'open', 'close', 'openintensity', 'closeintensity',
                      'smooth', 'edgein', 'edgeout', 'edge', 'tophat',
                      'bottomhat', 'hitandmiss', 'thinning', 'thicken',
                      'voronoi', 'iterativedistance')

NOISE_TYPES = ('undefined', 'uniform', 'gaussian', 'multiplicative',
               'impulse', 'laplacian', 'poisson', 'random')

INTERPOLATEPIXEL_METHODS = ('undefined', 'average', 'bicubic', 'bilinear',
                            'filter', 'integer', 'mesh', 'nearestneighbor',
                            'spline', 'average9', 'average16', 'blend',
                            'background', 'catrom')

SPARSE_METHODS = dict(undefined=0,  # DISTORTION_METHODS['undefined'],
                      barycentric=1,  # DISTORTION_METHODS['affine'],
                      bilinear=7,  # DISTORTION_METHODS['bilinear_reverse'],
                      polynomial=8,  # DISTORTION_METHODS['polynomial'],
                      shepards=16,  # DISTORTION_METHODS['shepards'],
                      voronoi=18,  # DISTORTION_METHODS['sentinel'],
                      inverse=19,
                      manhattan=20)


def adaptiveblur(image, radius, sigma):
    if not isinstance(radius, numbers.Real):
        raise TypeError('radius has to be a numbers.Real, not ' +
                        repr(radius))
    elif not isinstance(sigma, numbers.Real):
        raise TypeError('sigma has to be a numbers.Real, not ' +
                        repr(sigma))
    r = library.MagickAdaptiveBlurImage(image.wand, radius, sigma)
    if not r:
        image.raise_exception()


def addnoise(image, type):
    if type not in NOISE_TYPES:
        raise ValueError('expected string from NOISE_TYPES, not ' +
                         repr(type))
    index = NOISE_TYPES.index(type)
    r = library.MagickAddNoiseImage(image.wand, index)
    if not r:
        image.raise_exception()


def autogamma(image):
    r = library.MagickAutoGammaImage(image.wand)
    if not r:
        image.raise_exception()


def autolevel(image):
    r = library.MagickAutoLevelImage(image.wand)
    if not r:
        image.raise_exception()


def blackthreshold(image, threshold):
    if not isinstance(threshold, Color):
        raise TypeError('threshold must be a wand.color.Color, not ' +
                        repr(threshold))
    with threshold:
        r = library.MagickBlackThresholdImage(image.wand, threshold.resource)
        if not r:
            image.raise_exception()


def brightnesscontrast(image, brightness, contrast):
    if not isinstance(brightness, numbers.Real):
        raise TypeError('brightness has to be a numbers.Real, not ' +
                        repr(brightness))
    elif not isinstance(contrast, numbers.Real):
        raise TypeError('contrast has to be a numbers.Real, not ' +
                        repr(contrast))
    r = library.MagickBrightnessContrastImage(image.wand, brightness, contrast)
    if not r:
        image.raise_exception()


def blur(image, radius, sigma):
    if not isinstance(radius, numbers.Real):
        raise TypeError('radius has to be a numbers.Real, not ' +
                        repr(radius))
    elif not isinstance(sigma, numbers.Real):
        raise TypeError('sigma has to be a numbers.Real, not ' +
                        repr(sigma))
    r = library.MagickBlurImage(image.wand, radius, sigma)
    if not r:
        image.raise_exception()


def charcoal(image, radius, sigma):
    if not isinstance(radius, numbers.Real):
        raise TypeError('radius has to be a numbers.Real, not ' +
                        repr(radius))
    elif not isinstance(sigma, numbers.Real):
        raise TypeError('sigma has to be a numbers.Real, not ' +
                        repr(sigma))
    r = library.MagickCharcoalImage(image.wand, radius, sigma)
    if not r:
        image.raise_exception()


def chop(image, x, y, width, height):
    if not isinstance(x, numbers.Integral):
        raise TypeError('x has to be a numbers.Real, not ' +
                        repr(x))
    elif not isinstance(y, numbers.Integral):
        raise TypeError('y has to be a numbers.Real, not ' +
                        repr(y))
    elif not isinstance(width, numbers.Integral):
        raise TypeError('width has to be a numbers.Real, not ' +
                        repr(width))
    elif not isinstance(height, numbers.Integral):
        raise TypeError('height has to be a numbers.Real, not ' +
                        repr(height))
    r = library.MagickChopImage(image.wand, width, height, x, y)
    if not r:
        image.raise_exception()


def clut(image, clutimage):
    r = library.MagickClutImage(image.wand, clutimage.wand)
    if not r:
        image.raise_exception()


def colorize(image, color, opacity):
    if not isinstance(color, Color):
        raise TypeError('color must be a wand.color.Color, not ' +
                        repr(color))
    elif not isinstance(opacity, Color):
        raise TypeError('opacity must be a wand.color.Color, not ' +
                        repr(opacity))
    with color:
        with opacity:
            r = library.MagickColorizeImage(image.wand, color.resource,
                                            opacity.resource)
            if not r:
                image.raise_exception()


def comment(image, text):
    if not isinstance(text, string_type):
        raise TypeError('expected a string, not ' + repr(text))
    buffer = ctypes.create_string_buffer(text.encode())
    r = library.MagickCommentImage(image.wand, buffer)
    if not r:
        image.raise_exception()


def contrast(image, sharpen):
    if not isinstance(sharpen, bool):
        raise TypeError('sharpen must be a bool, not ' +
                        repr(sharpen))
    r = library.MagickContrastImage(image.wand, sharpen)
    if not r:
        image.raise_exception()


def convolve(image, order, kernel):
    if not isinstance(order, numbers.Integral):
        raise ValueError('order has to be a numbers.Integral, not ' +
                         repr(order))
    elif not isinstance(kernel, collections.Sequence):
        raise TypeError('expecting sequence of arguments, not ' +
                        repr(kernel))
    assert(len(kernel) == order * order)
    p_kernel = (ctypes.c_double * len(kernel))(*kernel)
    r = library.MagickConvolveImage(image.wand, order, p_kernel)
    if not r:
        image.raise_exception()


def cycle(image, displace):
    if not isinstance(displace, numbers.Integral):
        raise ValueError('displace has to be a numbers.Integral, not ' +
                         repr(displace))
    r = library.MagickCycleColormapImage(image.wand, displace)
    if not r:
        image.raise_exception()


def despeckle(image):
    r = library.MagickDespeckleImage(image.wand)
    if not r:
        image.raise_exception()


def edge(image, radius):
    if not isinstance(radius, numbers.Real):
        raise TypeError('radius has to be a numbers.Real, not ' +
                        repr(radius))
    r = library.MagickEdgeImage(image.wand, radius)
    if not r:
        image.raise_exception()


def emboss(image, radius, sigma):
    if not isinstance(radius, numbers.Real):
        raise TypeError('radius has to be a numbers.Real, not ' +
                        repr(radius))
    elif not isinstance(sigma, numbers.Real):
        raise TypeError('sigma has to be a numbers.Real, not ' +
                        repr(sigma))
    r = library.MagickEmbossImage(image.wand, radius, sigma)
    if not r:
        image.raise_exception()


def enhance(image):
    r = library.MagickEnhanceImage(image.wand)
    if not r:
        image.raise_exception()


def extent(image, x, y, width, height):
    if not isinstance(x, numbers.Integral):
        raise TypeError('x has to be a numbers.Real, not ' +
                        repr(x))
    elif not isinstance(y, numbers.Integral):
        raise TypeError('y has to be a numbers.Real, not ' +
                        repr(y))
    elif not isinstance(width, numbers.Integral):
        raise TypeError('width has to be a numbers.Real, not ' +
                        repr(width))
    elif not isinstance(height, numbers.Integral):
        raise TypeError('height has to be a numbers.Real, not ' +
                        repr(height))
    r = library.MagickExtentImage(image.wand, width, height, x, y)
    if not r:
        image.raise_exception()


def haldclut(image, clutimage):
    r = library.MagickHaldClutImage(image.wand, clutimage.wand)
    if not r:
        image.raise_exception()


def implode(image, amount):
    if not isinstance(amount, numbers.Real):
        raise TypeError('amount has to be a numbers.Real, not ' +
                        repr(amount))
    r = library.MagickImplodeImage(image.wand, amount)
    if not r:
        image.raise_exception()


def label(image, text):
    if not isinstance(text, string_type):
        raise TypeError('expected a string, not ' + repr(text))
    buffer = ctypes.create_string_buffer(text.encode())
    r = library.MagickLabelImage(image.wand, buffer)
    if not r:
        image.raise_exception()


def magnify(image):
    r = library.MagickMagnifyImage(image.wand)
    if not r:
        image.raise_exception()


def minify(image):
    r = library.MagickMinifyImage(image.wand)
    if not r:
        image.raise_exception()


def morphology(image, method, iterations, kernelinfo):
    if method not in MORPHOLOGY_METHODS:
        raise ValueError('expected string from MORPHOLOGY_METHODS, not ' +
                         repr(method))
    elif not isinstance(iterations, numbers.Integral):
        raise ValueError('iterations has to be a numbers.Integral, not ' +
                         repr(iterations))
    methodindex = MORPHOLOGY_METHODS.index(method)
    kinfo = ctypes.create_string_buffer(kernelinfo.encode())
    kernel = libmagick.AcquireKernelInfo(kinfo)
    r = library.MagickMorphologyImage(image.wand, methodindex,
                                      iterations, kernel)
    kernel = libmagick.DestroyKernelInfo(kernel)
    if not r:
        image.raise_exception()


def motionblur(image, radius, sigma, angle):
    if not isinstance(radius, numbers.Real):
        raise TypeError('radius has to be a numbers.Real, not ' +
                        repr(radius))
    elif not isinstance(sigma, numbers.Real):
        raise TypeError('sigma has to be a numbers.Real, not ' +
                        repr(sigma))
    elif not isinstance(angle, numbers.Real):
        raise TypeError('angle has to be a numbers.Real, not ' +
                        repr(angle))
    r = library.MagickMotionBlurImage(image.wand, radius, sigma, angle)
    if not r:
        image.raise_exception()


def oilpaint(image, radius):
    if not isinstance(radius, numbers.Real):
        raise TypeError('radius has to be a numbers.Real, not ' +
                        repr(radius))
    r = library.MagickOilPaintImage(image.wand, radius)
    if not r:
        image.raise_exception()


def opaquepaint(image, target, fill, fuzz, invert=False):
    if not isinstance(target, Color):
        raise TypeError('target must be a wand.color.Color instance, '
                        'not ' + repr(target))
    elif not isinstance(fill, Color):
        raise TypeError('fill must be a wand.color.Color instance, '
                        'not ' + repr(fill))
    elif not isinstance(fuzz, numbers.Real):
        raise TypeError('fuzz has to be a numbers.Real, not ' +
                        repr(fuzz))
    elif not isinstance(invert, bool):
        raise TypeError('invert must be a bool, not ' +
                        repr(invert))
    with target:
        with fill:
            r = library.MagickOpaquePaintImage(image.wand, target.resource,
                                               fill.resource, fuzz, invert)
            if not r:
                image.raise_exception()


def orderedposterize(image, threshold_map):
    if not isinstance(threshold_map, string_type):
        raise TypeError('expected a string, not ' + repr(threshold_map))
    buffer = ctypes.create_string_buffer(threshold_map.encode())
    r = library.MagickOrderedPosterizeImage(image.wand, buffer)
    if not r:
        image.raise_exception()


def polaroid(image, drawing, angle):
    if not isinstance(drawing, Drawing):
        raise TypeError('drawing must be a wand.drawing.Drawing instance, '
                        'not ' + repr(drawing))
    elif not isinstance(angle, numbers.Real):
        raise TypeError('angle has to be a numbers.Real, not ' +
                        repr(angle))
    r = library.MagickPolaroidImage(image.wand, drawing.resource, angle)
    if not r:
        image.raise_exception()


def posterize(image, levels, dither):
    if not isinstance(levels, numbers.Integral):
        raise TypeError('levels has to be a numbers.Integral, not ' +
                        repr(levels))
    elif not isinstance(dither, bool):
        raise TypeError('dither must be a bool, not ' +
                        repr(dither))
    r = library.MagickPosterizeImage(image.wand, levels, dither)
    if not r:
        image.raise_exception()


def raiseimage(image, x, y, width, height, raiseeffect):  # raise is keyword
    if not isinstance(x, numbers.Integral):
        raise TypeError('x has to be a numbers.Real, not ' +
                        repr(x))
    elif not isinstance(y, numbers.Integral):
        raise TypeError('y has to be a numbers.Real, not ' +
                        repr(y))
    elif not isinstance(width, numbers.Integral):
        raise TypeError('width has to be a numbers.Real, not ' +
                        repr(width))
    elif not isinstance(height, numbers.Integral):
        raise TypeError('height has to be a numbers.Real, not ' +
                        repr(height))
    elif not isinstance(raiseeffect, bool):
        raise TypeError('raiseeffect must be a bool, not ' +
                        repr(raiseeffect))
    r = library.MagickRaiseImage(image.wand, x, y, width, height, raiseeffect)
    if not r:
        image.raise_exception()


def randomthreshold(image, low, high):
    if not isinstance(low, numbers.Integral):
        raise TypeError('low has to be a numbers.Integral, not ' +
                        repr(low))
    elif not isinstance(high, numbers.Integral):
        raise TypeError('high has to be a numbers.Integral, not ' +
                        repr(high))
    r = library.MagickRandomThresholdImage(image.wand, low, high)
    if not r:
        image.raise_exception()


def remap(image, mapimage, method):
    if method not in DITHER_METHODS:
        raise ValueError('expected value from DITHER_METHODS, not ' +
                         repr(method))
    index = DITHER_METHODS.index(method)
    r = library.MagickRemapImage(image.wand, mapimage.wand, index)
    if not r:
        image.raise_exception()


def resample(image, x_resolution, y_resolution, filtertype, blur):
    if not isinstance(x_resolution, numbers.Integral):
        raise TypeError('x_resolution has to be a numbers.Real, not ' +
                        repr(x_resolution))
    elif not isinstance(y_resolution, numbers.Integral):
        raise TypeError('y_resolution has to be a numbers.Real, not ' +
                        repr(y_resolution))
    elif filtertype not in FILTER_TYPES:
        raise ValueError('expected value from FILTER_TYPES, not ' +
                         repr(filter))
    elif not isinstance(blur, numbers.Real):
        raise TypeError('blur has to be a numbers.Real, not ' +
                        repr(blur))
    filterindex = FILTER_TYPES.index(filtertype)
    r = library.MagickResampleImage(image.wand, x_resolution, y_resolution,
                                    filterindex, blur)
    if not r:
        image.raise_exception()


def roll(image, x, y):
    if not isinstance(x, numbers.Integral):
        raise TypeError('x has to be a numbers.Integral, not ' +
                        repr(x))
    elif not isinstance(y, numbers.Integral):
        raise TypeError('y has to be a numbers.Integral, not ' +
                        repr(y))
    r = library.MagickRollImage(image.wand, x, y)
    if not r:
        image.raise_exception()


def shade(image, gray, azimuth, elevation):
    if not isinstance(gray, bool):
        raise TypeError('gray must be a bool, not ' +
                        repr(gray))
    elif not isinstance(azimuth, numbers.Real):
        raise TypeError('azimuth has to be a numbers.Real, not ' +
                        repr(azimuth))
    elif not isinstance(elevation, numbers.Real):
        raise TypeError('elevation has to be a numbers.Real, not ' +
                        repr(elevation))
    r = library.MagickShadeImage(image.wand, gray, azimuth, elevation)
    if not r:
        image.raise_exception()


def shadow(image, opacity, sigma, x, y):
    if not isinstance(opacity, numbers.Real):
        raise TypeError('opacity has to be a numbers.Real, not ' +
                        repr(opacity))
    elif not isinstance(sigma, numbers.Real):
        raise TypeError('sigma has to be a numbers.Real, not ' +
                        repr(sigma))
    elif not isinstance(x, numbers.Integral):
        raise TypeError('x has to be a numbers.Integral, not ' +
                        repr(x))
    elif not isinstance(y, numbers.Integral):
        raise TypeError('y has to be a numbers.Integral, not ' +
                        repr(y))
    r = library.MagickShadowImage(image.wand, opacity, sigma, x, y)
    if not r:
        image.raise_exception()


def shave(image, columns, rows):
    if not isinstance(columns, numbers.Integral):
        raise TypeError('columns has be a numbers.Integral, not ' +
                        repr(columns))
    elif not isinstance(rows, numbers.Integral):
        raise TypeError('rows has to be a numbers.Integral, not ' +
                        repr(rows))
    r = library.MagickShaveImage(image.wand, columns, rows)
    if not r:
        image.raise_exception()


def shear(image, background, x, y):
    if not isinstance(background, Color):
        raise TypeError('background must be a wand.color.Color instance, '
                        'not ' + repr(background))
    elif not isinstance(x, numbers.Real):
        raise TypeError('x has to be a numbers.Real, not ' +
                        repr(x))
    elif not isinstance(y, numbers.Real):
        raise TypeError('y has to be a numbers.Real, not ' +
                        repr(y))
    with background:
        r = library.MagickShearImage(image.wand, background.resource, x, y)
        if not r:
            image.raise_exception()


def sparsecolor(image, channel, method, arguments):
    if channel not in CHANNELS:
        raise ValueError('expected value from CHANNELS, not ' +
                         repr(channel))
    if method not in SPARSE_METHODS:
        raise ValueError('expected value from SPARSE_METHODS, not ' +
                         repr(method))
    elif not isinstance(arguments, collections.Sequence):
        raise TypeError('expecting sequence of arguments, not ' +
                        repr(arguments))
    argc = len(arguments)
    argv = (ctypes.c_double * argc)(*arguments)
    c = CHANNELS[channel]
    m = SPARSE_METHODS[method]
    r = library.MagickSparseColorImage(image.wand, c, m, argc, argv)
    if not r:
        image.raise_exception()


def spread(image, method, amount):
    if method not in INTERPOLATEPIXEL_METHODS:
        raise ValueError('expected string from INTERPOLATEPIXEL_METHODS, ' +
                         'not ' + repr(method))
    if not isinstance(amount, numbers.Real):
        raise TypeError('amount has to be a numbers.Real, not ' +
                        repr(amount))
    index = INTERPOLATEPIXEL_METHODS.index(method)
    r = library.MagickSpreadImage(image.wand, index, amount)
    if not r:
        image.raise_exception()


def wave(image, amplitude, wave_length):
    if not isinstance(amplitude, numbers.Real):
        raise TypeError('amplitude has to be a numbers.Real, not ' +
                        repr(amplitude))
    elif not isinstance(wave_length, numbers.Real):
        raise TypeError('wave_length has to be a numbers.Real, not ' +
                        repr(wave_length))
    r = library.MagickWaveImage(image.wand, amplitude, wave_length)
    if not r:
        image.raise_exception()


def whitethreshold(image, threshold):
    if not isinstance(threshold, Color):
        raise TypeError('threshold must be a wand.color.Color, not ' +
                        repr(threshold))
    with threshold:
        r = library.MagickWhiteThresholdImage(image.wand, threshold.resource)
        if not r:
            image.raise_exception()


if __name__ == '__main__':
    pass
