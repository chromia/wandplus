from wand.image import CHANNELS
from wand.api import library, libmagick
from wand.color import Color
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
library.MagickAutoGammaImage.restype = ctypes.c_bool
library.MagickAutoGammaImage.argtypes = [
    ctypes.c_void_p
]
library.MagickAutoLevelImage.restype = ctypes.c_bool
library.MagickAutoLevelImage.argtypes = [
    ctypes.c_void_p
]
library.MagickBlurImage.restype = ctypes.c_bool
library.MagickBlurImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double,
    ctypes.c_double
]
library.MagickClutImage.restype = ctypes.c_bool
library.MagickClutImage.argtypes = [
    ctypes.c_void_p,
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

MORPHOLOGY_METHODS = ('undefined', 'convolve', 'correlate', 'erode', 'dilate',
                      'erodeintensity', 'dilateintensity', 'distance',
                      'open', 'close', 'openintensity', 'closeintensity',
                      'smooth', 'edgein', 'edgeout', 'edge', 'tophat',
                      'bottomhat', 'hitandmiss', 'thinning', 'thicken',
                      'voronoi', 'iterativedistance')

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


def autogamma(image):
    r = library.MagickAutoGammaImage(image.wand)
    if not r:
        image.raise_exception()


def autolevel(image):
    r = library.MagickAutoLevelImage(image.wand)
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


def clut(image, clutimage):
    r = library.MagickClutImage(image.wand, clutimage.wand)
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
        raise TypeError('x_shear has to be a numbers.Real, not ' +
                        repr(x))
    elif not isinstance(y, numbers.Real):
        raise TypeError('y_shear has to be a numbers.Real, not ' +
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
