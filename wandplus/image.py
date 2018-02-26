#!/usr/bin/env python

from wand.image import Image, BaseImage
from wand.image import CHANNELS, FILTER_TYPES, COLORSPACE_TYPES
from wand.api import library, libmagick
from wand.drawing import Drawing
from wand.color import Color
from wand.compat import string_type
import numbers
import ctypes
import collections

# %Start Definition%  -- do not remove this comment!
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
library.MagickAdaptiveBlurImageChannel.restype = ctypes.c_bool
library.MagickAdaptiveBlurImageChannel.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_double,
    ctypes.c_double
]
library.MagickAdaptiveResizeImage.restype = ctypes.c_bool
library.MagickAdaptiveResizeImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.c_size_t
]
library.MagickAdaptiveSharpenImage.restype = ctypes.c_bool
library.MagickAdaptiveSharpenImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double,
    ctypes.c_double
]
library.MagickAdaptiveSharpenImageChannel.restype = ctypes.c_bool
library.MagickAdaptiveSharpenImageChannel.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_double,
    ctypes.c_double
]
library.MagickAdaptiveThresholdImage.restype = ctypes.c_bool
library.MagickAdaptiveThresholdImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.c_size_t,
    ctypes.c_ssize_t
]
library.MagickAddImage.restype = ctypes.c_bool
library.MagickAddImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p
]
library.MagickAddNoiseImage.restype = ctypes.c_bool
library.MagickAddNoiseImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int
]
library.MagickAddNoiseImageChannel.restype = ctypes.c_bool
library.MagickAddNoiseImageChannel.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_int
]
library.MagickAffineTransformImage.restype = ctypes.c_bool
library.MagickAffineTransformImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p
]
library.MagickAutoGammaImage.restype = ctypes.c_bool
library.MagickAutoGammaImage.argtypes = [
    ctypes.c_void_p
]
library.MagickAutoGammaImageChannel.restype = ctypes.c_bool
library.MagickAutoGammaImageChannel.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int
]
library.MagickAutoLevelImage.restype = ctypes.c_bool
library.MagickAutoLevelImage.argtypes = [
    ctypes.c_void_p
]
library.MagickAutoLevelImageChannel.restype = ctypes.c_bool
library.MagickAutoLevelImageChannel.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int
]
library.MagickBlackThresholdImage.restype = ctypes.c_bool
library.MagickBlackThresholdImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p
]
library.MagickBlueShiftImage.restype = ctypes.c_bool
library.MagickBlueShiftImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double
]
library.MagickBlurImage.restype = ctypes.c_bool
library.MagickBlurImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double,
    ctypes.c_double
]
library.MagickBlurImageChannel.restype = ctypes.c_bool
library.MagickBlurImageChannel.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_double,
    ctypes.c_double
]
library.MagickBrightnessContrastImage.restype = ctypes.c_bool
library.MagickBrightnessContrastImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double,
    ctypes.c_double
]
library.MagickBrightnessContrastImageChannel.restype = ctypes.c_bool
library.MagickBrightnessContrastImageChannel.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
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
library.MagickClampImage.restype = ctypes.c_bool
library.MagickClampImage.argtypes = [
    ctypes.c_void_p
]
library.MagickClampImageChannel.restype = ctypes.c_bool
library.MagickClampImageChannel.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int
]
library.MagickClipImage.restype = ctypes.c_bool
library.MagickClipImage.argtypes = [
    ctypes.c_void_p
]
library.MagickClutImage.restype = ctypes.c_bool
library.MagickClutImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p
]
library.MagickClutImageChannel.restype = ctypes.c_bool
library.MagickClutImageChannel.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_void_p
]
library.MagickColorDecisionListImage.restype = ctypes.c_bool
library.MagickColorDecisionListImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p
]
library.MagickColorizeImage.restype = ctypes.c_bool
library.MagickColorizeImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_void_p
]
library.MagickColorMatrixImage.restype = ctypes.c_bool
library.MagickColorMatrixImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p
]
library.MagickCommentImage.restype = ctypes.c_bool
library.MagickCommentImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p
]
library.MagickConstituteImage.restype = ctypes.c_bool
library.MagickConstituteImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.c_size_t,
    ctypes.c_char_p,
    ctypes.c_int,
    ctypes.c_void_p
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
library.MagickConvolveImageChannel.restype = ctypes.c_bool
library.MagickConvolveImageChannel.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_size_t,
    ctypes.POINTER(ctypes.c_double)
]
library.MagickCycleColormapImage.restype = ctypes.c_bool
library.MagickCycleColormapImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_ssize_t
]
library.MagickDecipherImage.restype = ctypes.c_bool
library.MagickDecipherImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p
]
library.MagickDeskewImage.restype = ctypes.c_bool
library.MagickDeskewImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double
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
library.MagickEncipherImage.restype = ctypes.c_bool
library.MagickEncipherImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p
]
library.MagickEnhanceImage.restype = ctypes.c_bool
library.MagickEnhanceImage.argtypes = [
    ctypes.c_void_p
]
library.MagickEqualizeImage.restype = ctypes.c_bool
library.MagickEqualizeImage.argtypes = [
    ctypes.c_void_p
]
library.MagickEqualizeImageChannel.restype = ctypes.c_bool
library.MagickEqualizeImageChannel.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int
]
library.MagickExtentImage.restype = ctypes.c_bool
library.MagickExtentImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.c_size_t,
    ctypes.c_ssize_t,
    ctypes.c_ssize_t
]
library.MagickFilterImage.restype = ctypes.c_bool
library.MagickFilterImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p
]
library.MagickFilterImageChannel.restype = ctypes.c_bool
library.MagickFilterImageChannel.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_void_p
]
library.MagickFloodfillPaintImage.restype = ctypes.c_bool
library.MagickFloodfillPaintImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_void_p,
    ctypes.c_double,
    ctypes.c_void_p,
    ctypes.c_ssize_t,
    ctypes.c_ssize_t,
    ctypes.c_bool
]
library.MagickForwardFourierTransformImage.restype = ctypes.c_bool
library.MagickForwardFourierTransformImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_bool
]
library.MagickHaldClutImage.restype = ctypes.c_bool
library.MagickHaldClutImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p
]
library.MagickHaldClutImageChannel.restype = ctypes.c_bool
library.MagickHaldClutImageChannel.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_void_p
]
library.MagickImplodeImage.restype = ctypes.c_bool
library.MagickImplodeImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double
]
library.MagickInverseFourierTransformImage.restype = ctypes.c_bool
library.MagickInverseFourierTransformImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_bool
]
library.MagickLabelImage.restype = ctypes.c_bool
library.MagickLabelImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p
]
library.MagickLocalContrastImage.restype = ctypes.c_bool
library.MagickLocalContrastImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double,
    ctypes.c_double
]
library.MagickMagnifyImage.restype = ctypes.c_bool
library.MagickMagnifyImage.argtypes = [
    ctypes.c_void_p
]
library.MagickMinifyImage.restype = ctypes.c_bool
library.MagickMinifyImage.argtypes = [
    ctypes.c_void_p
]
library.MagickMontageImage.restype = ctypes.c_void_p
library.MagickMontageImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_char_p,
    ctypes.c_char_p,
    ctypes.c_int,
    ctypes.c_char_p
]
library.MagickMorphologyImage.restype = ctypes.c_bool
library.MagickMorphologyImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_ssize_t,
    ctypes.c_void_p
]
library.MagickMorphologyImageChannel.restype = ctypes.c_bool
library.MagickMorphologyImageChannel.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
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
library.MagickMotionBlurImageChannel.restype = ctypes.c_bool
library.MagickMotionBlurImageChannel.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
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
library.MagickOpaquePaintImageChannel.restype = ctypes.c_bool
library.MagickOpaquePaintImageChannel.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
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
library.MagickOrderedPosterizeImageChannel.restype = ctypes.c_bool
library.MagickOrderedPosterizeImageChannel.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
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
library.MagickRandomThresholdImageChannel.restype = ctypes.c_bool
library.MagickRandomThresholdImageChannel.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
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
library.MagickRotationalBlurImage.restype = ctypes.c_bool
library.MagickRotationalBlurImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double
]
library.MagickRotationalBlurImageChannel.restype = ctypes.c_bool
library.MagickRotationalBlurImageChannel.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_double
]
library.MagickScaleImage.restype = ctypes.c_bool
library.MagickScaleImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.c_size_t
]
library.MagickSegmentImage.restype = ctypes.c_bool
library.MagickSegmentImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_bool,
    ctypes.c_double,
    ctypes.c_double
]
library.MagickSelectiveBlurImage.restype = ctypes.c_bool
library.MagickSelectiveBlurImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double
]
library.MagickSelectiveBlurImageChannel.restype = ctypes.c_bool
library.MagickSelectiveBlurImageChannel.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double
]
library.MagickSeparateImageChannel.restype = ctypes.c_bool
library.MagickSeparateImageChannel.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int
]
library.MagickSepiaToneImage.restype = ctypes.c_bool
library.MagickSepiaToneImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double
]
library.MagickSetSizeOffset.restype = ctypes.c_bool
library.MagickSetSizeOffset.argtypes = [
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.c_size_t,
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
library.MagickSharpenImage.restype = ctypes.c_bool
library.MagickSharpenImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double,
    ctypes.c_double
]
library.MagickSharpenImageChannel.restype = ctypes.c_bool
library.MagickSharpenImageChannel.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_double,
    ctypes.c_double
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
library.MagickSigmoidalContrastImage.restype = ctypes.c_bool
library.MagickSigmoidalContrastImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_bool,
    ctypes.c_double,
    ctypes.c_double
]
library.MagickSigmoidalContrastImageChannel.restype = ctypes.c_bool
library.MagickSigmoidalContrastImageChannel.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_bool,
    ctypes.c_double,
    ctypes.c_double
]
library.MagickSketchImage.restype = ctypes.c_bool
library.MagickSketchImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double
]
library.MagickSolarizeImage.restype = ctypes.c_bool
library.MagickSolarizeImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double
]
library.MagickSolarizeImageChannel.restype = ctypes.c_bool
library.MagickSolarizeImageChannel.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
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
library.MagickSpliceImage.restype = ctypes.c_bool
library.MagickSpliceImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.c_size_t,
    ctypes.c_ssize_t,
    ctypes.c_ssize_t
]
library.MagickSpreadImage.restype = ctypes.c_bool
library.MagickSpreadImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_double
]
library.MagickStatisticImage.restype = ctypes.c_bool
library.MagickStatisticImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_size_t,
    ctypes.c_size_t
]
library.MagickStatisticImageChannel.restype = ctypes.c_bool
library.MagickStatisticImageChannel.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.c_size_t,
    ctypes.c_size_t
]
library.MagickSteganoImage.restype = ctypes.c_void_p
library.MagickSteganoImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_ssize_t
]
library.MagickStereoImage.restype = ctypes.c_void_p
library.MagickStereoImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p
]
library.MagickSwirlImage.restype = ctypes.c_bool
library.MagickSwirlImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double
]
library.MagickTextureImage.restype = ctypes.c_void_p
library.MagickTextureImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p
]
library.MagickThumbnailImage.restype = ctypes.c_bool
library.MagickThumbnailImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.c_size_t
]
library.MagickTintImage.restype = ctypes.c_bool
library.MagickTintImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_void_p
]
library.MagickVignetteImage.restype = ctypes.c_bool
library.MagickVignetteImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_ssize_t,
    ctypes.c_ssize_t
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
# %End Definition%  -- do not remove this comment!

DITHER_METHODS = ('undefined', 'nodither', 'riemersma', 'floydsteinberg')

MONTAGE_MODES = ('undefined', 'frame', 'unframe', 'concatenate')

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

STATISTIC_TYPES = ('undefined', 'gradient', 'maximum', 'mean', 'median',
                   'minimum', 'mode', 'nonpeak', 'standarddeviation',
                   'rootmeansquare')

STORAGE_TYPES = ('undefined', 'char', 'double', 'float', 'integer',
                 'long', 'quantum', 'short')


class KernelInfo(ctypes.Structure):
    _fields_ = [
        ('type', ctypes.c_int),
        ('width', ctypes.c_size_t),
        ('height', ctypes.c_size_t),
        ('x', ctypes.c_ssize_t),
        ('y', ctypes.c_ssize_t),
        ('value', ctypes.POINTER(ctypes.c_double)),
        ('minimum', ctypes.c_double),
        ('negative_range', ctypes.c_double),
        ('positive_range', ctypes.c_double),
        ('angle', ctypes.c_double),
        ('next', ctypes.c_void_p),
        ('signature', ctypes.c_size_t)
    ]

    def __init__(self, width, height, kernel):
        if not isinstance(kernel, collections.Sequence):
            raise TypeError('expecting sequence of arguments, not ' +
                            repr(kernel))
        length = len(kernel)
        assert(width * height == length)
        self.width = width
        self.height = height
        self.value = (ctypes.c_double * length)(*kernel)


def adaptiveblur(image, radius, sigma, channel=None):
    """adaptively blurs the image by blurring less intensely
    near image edges and more intensely far from edges.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param radius: the radius of the Gaussian, in pixels,
                   not counting the center pixel.
                   if 0, suitable radius is selected.
    :type radius: :class:`numbers.Real`
    :param sigma: the standard deviation of the Gaussian, in pixels.
    :type sigma: :class:`numbers.Real`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
                    If ``None``, select all channels.
    :type channel: :class:`str`
    """
    if not isinstance(radius, numbers.Real):
        raise TypeError('radius has to be a numbers.Real, not ' +
                        repr(radius))
    elif not isinstance(sigma, numbers.Real):
        raise TypeError('sigma has to be a numbers.Real, not ' +
                        repr(sigma))
    if channel:
        if channel not in CHANNELS:
            raise ValueError('expected value from CHANNELS, not ' +
                             repr(channel))
        r = library.MagickAdaptiveBlurImageChannel(image.wand,
                                                   CHANNELS[channel],
                                                   radius, sigma)
    else:
        r = library.MagickAdaptiveBlurImage(image.wand, radius, sigma)
    if not r:
        image.raise_exception()


def adaptiveresize(image, columns, rows):
    """adaptively resize image with data dependent triangulation.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param columns: the number of columns in the scaled image.
    :type columns: :class:`numbers.Integral`
    :param rows: the number of rows in the scaled image.
    :type rows: :class:`numbers.Integral`
    """
    if not isinstance(columns, numbers.Integral):
        raise TypeError('columns has to be a numbers.Integral, not ' +
                        repr(columns))
    elif not isinstance(rows, numbers.Integral):
        raise TypeError('rows has to be a numbers.Integral, not ' +
                        repr(rows))
    r = library.MagickAdaptiveResizeImage(image.wand, columns, rows)
    if not r:
        image.raise_exception()


def adaptivesharpen(image, radius, sigma, channel=None):
    """adaptively sharpens the image by sharpening
    more intensely near image edges and less intensely far from edges. We
    sharpen the image with a Gaussian operator of the given radius and standard
    deviation (sigma).  For reasonable results, radius should be larger than
    sigma.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param radius: the radius of the Gaussian, in pixels,
                   not counting the center pixel.
                   if 0, suitable radius is selected.
    :type radius: :class:`numbers.Real`
    :param sigma: the standard deviation of the Gaussian, in pixels.
    :type sigma: :class:`numbers.Real`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
                    If ``None``, select all channels.
    :type channel: :class:`str`
    """
    if not isinstance(radius, numbers.Real):
        raise TypeError('radius has to be a numbers.Real, not ' +
                        repr(radius))
    elif not isinstance(sigma, numbers.Real):
        raise TypeError('sigma has to be a numbers.Real, not ' +
                        repr(sigma))
    if channel:
        if channel not in CHANNELS:
            raise ValueError('expected value from CHANNELS, not ' +
                             repr(channel))
        r = library.MagickAdaptiveSharpenImage(image.wand, CHANNELS[channel],
                                               radius, sigma)
    else:
        r = library.MagickAdaptiveSharpenImage(image.wand, radius, sigma)
    if not r:
        image.raise_exception()


def adaptivethreshold(image, width, height, offset):
    """selects an individual threshold for each pixel
    based on the range of intensity values in its local neighborhood.  This
    allows for thresholding of an image whose global intensity histogram
    doesn't contain distinctive peaks.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param width: the width of the local neighborhood.
    :type width: :class:`numbers.Integral`
    :param height: the height of the local neighborhood.
    :type height: :class:`numbers.Integral`
    :param offset: the mean offset.
    :type offset: :class:`numbers.Integral`
    """
    if not isinstance(width, numbers.Integral):
        raise TypeError('width has to be a numbers.Integral, not ' +
                        repr(width))
    elif not isinstance(height, numbers.Integral):
        raise TypeError('height has to be a numbers.Integral, not ' +
                        repr(height))
    elif not isinstance(offset, numbers.Integral):
        raise TypeError('offset has to be a numbers.Integral, not ' +
                        repr(offset))
    r = library.MagickAdaptiveThresholdImage(image.wand, width, height, offset)
    if not r:
        image.raise_exception()


def add(dstimage, srcimage):
    """append source image(s) to sequence of destination.

    This function conflicts with wand.image.Image.sequence.
    Do NOT use together

    :param dstimage: target image.
    :type dstimage: :class:`wand.image.Image`
    :param srcimage: image(s) to be added.
    :type srcimage: :class:`wand.image.Image`
    """
    r = library.MagickAddImage(dstimage.wand, srcimage.wand)
    if not r:
        dstimage.raise_exception()


def addnoise(image, type, channel=None):
    """adds random noise to the image.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param type: The type of noise included in :const:`NOISE_TYPES`.
                 e.g. 'uniform', 'gaussian', 'random'
    :type type: :class:`str`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
                    If ``None``, select all channels.
    :type channel: :class:`str`
    """
    if type not in NOISE_TYPES:
        raise ValueError('expected string from NOISE_TYPES, not ' +
                         repr(type))
    index = NOISE_TYPES.index(type)
    if channel:
        if channel not in CHANNELS:
            raise ValueError('expected value from CHANNELS, not ' +
                             repr(channel))
        r = library.MagickAddNoiseImageChannel(image.wand, CHANNELS[channel],
                                               index)
    else:
        r = library.MagickAddNoiseImage(image.wand, index)
    if not r:
        image.raise_exception()


def affinetransform(image, drawing):
    """transforms an image as dictated by the affine
    matrix of the drawing context.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param drawing: the drawing context called Drawing.affine function.
    :type drawing: :class:`wand.drawing.Drawing`
    """
    if not isinstance(drawing, Drawing):
        raise TypeError('drawing must be a wand.drawing.Drawing instance, '
                        'not ' + repr(drawing))
    r = library.MagickAffineTransformImage(image.wand, drawing.resource)
    if not r:
        image.raise_exception()


def autogamma(image, channel=None):
    """extracts the 'mean' from the image and adjust the
    image to try make set its gamma appropriatally.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
                    If ``None``, select all channels.
    :type channel: :class:`str`
    """
    if channel:
        if channel not in CHANNELS:
            raise ValueError('expected value from CHANNELS, not ' +
                             repr(channel))
        r = library.MagickAutoGammaImageChannel(image.wand, CHANNELS[channel])
    else:
        r = library.MagickAutoGammaImage(image.wand)
    if not r:
        image.raise_exception()


def autolevel(image, channel=None):
    """adjusts the levels of a particular image channel by
    scaling the minimum and maximum values to the full quantum range.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
                    If ``None``, select all channels.
    :type channel: :class:`str`
    """
    if channel:
        if channel not in CHANNELS:
            raise ValueError('expected value from CHANNELS, not ' +
                             repr(channel))
        r = library.MagickAutoLevelImageChannel(image.wand, CHANNELS[channel])
    else:
        r = library.MagickAutoLevelImage(image.wand)
    if not r:
        image.raise_exception()


def blackthreshold(image, threshold):
    """is like MagickThresholdImage() but  forces all
    pixels below the threshold into black while leaving all pixels above the
    threshold unchanged.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param threshold: threshold color.
    :type threshold: :class:`wand.color.Color`
    """
    if not isinstance(threshold, Color):
        raise TypeError('threshold must be a wand.color.Color, not ' +
                        repr(threshold))
    with threshold:
        r = library.MagickBlackThresholdImage(image.wand, threshold.resource)
        if not r:
            image.raise_exception()


def blueshift(image, factor=1.5):
    """mutes the colors of the image to simulate a scene at
    nighttime in the moonlight.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param factor: the blue shift factor (default 1.5)
    :type factor: :class:`numbers.Real`
    """
    if not isinstance(factor, numbers.Real):
        raise TypeError('factor has to be a numbers.Real, not ' +
                        repr(factor))
    r = library.MagickBlueShiftImage(image.wand, factor)
    if not r:
        image.raise_exception()


def blur(image, radius, sigma, channel=None):
    """blurs an image.  We convolve the image with a gaussian
    operator of the given radius and standard deviation (sigma).  For reasonable
    results, the radius should be larger than sigma.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param radius: the radius of the , in pixels, not counting the center pixel.
                   if 0, suitable radius is selected.
    :type radius: :class:`numbers.Real`
    :param sigma: the standard deviation of the , in pixels.
    :type sigma: :class:`numbers.Real`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
                    If ``None``, select all channels.
    :type channel: :class:`str`
    """
    if not isinstance(radius, numbers.Real):
        raise TypeError('radius has to be a numbers.Real, not ' +
                        repr(radius))
    elif not isinstance(sigma, numbers.Real):
        raise TypeError('sigma has to be a numbers.Real, not ' +
                        repr(sigma))
    if channel:
        if channel not in CHANNELS:
            raise ValueError('expected value from CHANNELS, not ' +
                             repr(channel))
        r = library.MagickBlurImageChannel(image.wand, CHANNELS[channel],
                                           radius, sigma)
    else:
        r = library.MagickBlurImage(image.wand, radius, sigma)
    if not r:
        image.raise_exception()


def brightnesscontrast(image, brightness, contrast, channel=None):
    """to change the brightness and/or contrast
    of an image.  It converts the brightness and contrast parameters into slope
    and intercept and calls a polynomical function to apply to the image.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param brightness: the brightness percent (-100 .. 100).
    :type brightness: :class:`numbers.Real`
    :param contrast: the contrast percent (-100 .. 100).
    :type contrast: :class:`numbers.Real`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
                    If ``None``, select all channels.
    :type channel: :class:`str`
    """
    if not isinstance(brightness, numbers.Real):
        raise TypeError('brightness has to be a numbers.Real, not ' +
                        repr(brightness))
    elif not isinstance(contrast, numbers.Real):
        raise TypeError('contrast has to be a numbers.Real, not ' +
                        repr(contrast))
    if channel:
        if channel not in CHANNELS:
            raise ValueError('expected value from CHANNELS, not ' +
                             repr(channel))
        r = library.MagickBrightnessContrastImageChannel(image.wand,
                                                         CHANNELS[channel],
                                                         brightness,
                                                         contrast)
    else:
        r = library.MagickBrightnessContrastImage(image.wand, brightness,
                                                  contrast)
    if not r:
        image.raise_exception()


def charcoal(image, radius, sigma):
    """simulates a charcoal drawing.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param radius: the radius of the Gaussian, in pixels,
                   not counting the center pixel.
    :type radius: :class:`numbers.Real`
    :param sigma: the standard deviation of the Gaussian, in pixels.
    :type sigma: :class:`numbers.Real`
    """
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
    """removes a region of an image and collapses the image to
    occupy the removed portion.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param x: the region x offset.
    :type x: :class:`numbers.Integral`
    :param y: the region y offset.
    :type y: :class:`numbers.Integral`
    :param width: the region width
    :type width: :class:`numbers.Integral`
    :param height: the region height
    :type height: :class:`numbers.Integral`
    """
    if not isinstance(x, numbers.Integral):
        raise TypeError('x has to be a numbers.Integral, not ' +
                        repr(x))
    elif not isinstance(y, numbers.Integral):
        raise TypeError('y has to be a numbers.Integral, not ' +
                        repr(y))
    elif not isinstance(width, numbers.Integral):
        raise TypeError('width has to be a numbers.Integral, not ' +
                        repr(width))
    elif not isinstance(height, numbers.Integral):
        raise TypeError('height has to be a numbers.Integral, not ' +
                        repr(height))
    r = library.MagickChopImage(image.wand, width, height, x, y)
    if not r:
        image.raise_exception()


def clamp(image, channel=None):
    """restricts the color range from 0 to the quantum depth.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
                    If ``None``, select all channels.
    :type channel: :class:`str`
    """
    if channel:
        if channel not in CHANNELS:
            raise ValueError('expected value from CHANNELS, not ' +
                             repr(channel))
        r = library.MagickClampImageChannel(image.wand, CHANNELS[channel])
    else:
        r = library.MagickClampImage(image.wand)
    if not r:
        image.raise_exception()


def clip(image):
    """clips along the first path from the 8BIM profile, if present.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    """
    r = library.MagickClipImage(image.wand)
    if not r:
        image.raise_exception()


def clut(image, clutimage, channel=None):
    """replaces colors in the image from a color lookup table.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param clutimage: the clut image.
    :type clutimage: :class:`wand.image.Image`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
                    If ``None``, select all channels.
    :type channel: :class:`str`
    """
    if channel:
        if channel not in CHANNELS:
            raise ValueError('expected value from CHANNELS, not ' +
                             repr(channel))
        r = library.MagickClutImageChannel(image.wand, CHANNELS[channel],
                                           clutimage.wand)
    else:
        r = library.MagickClutImage(image.wand, clutimage.wand)
    if not r:
        image.raise_exception()


def colordecisionlist(image, ccc_text):
    """accepts a lightweight Color Correction
    Collection (CCC) file which solely contains one or more color corrections
    and applies the color correction to the image.  Here is a sample CCC file:

    <ColorCorrectionCollection xmlns="urn:ASC:CDL:v1.2">
        <ColorCorrection id="cc03345">
            <SOPNode>
                <Slope> 0.9 1.2 0.5 </Slope>
                <Offset> 0.4 -0.5 0.6 </Offset>
                <Power> 1.0 0.8 1.5 </Power>
            </SOPNode>
            <SATNode>
                <Saturation> 0.85 </Saturation>
            </SATNode>
        </ColorCorrection>
    </ColorCorrectionCollection>

    which includes the offset, slope, and power for each of the RGB channels
    as well as the saturation.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param ccc_text: the color correction collection in XML.
    :type ccc_text: :class:`str`
    """
    if not isinstance(ccc_text, string_type):
        raise TypeError('expected a string, not ' + repr(ccc_text))
    buffer = ctypes.create_string_buffer(ccc_text.encode())
    r = library.MagickColorDecisionListImage(image.wand, buffer)
    if not r:
        image.raise_exception()


def colormatrix(image, width, height, color_matrix):
    """apply color transformation to an image. The method
    permits saturation changes, hue rotation, luminance to alpha, and various
    other effects.  Although variable-sized transformation matrices can be used,
    typically one uses a 5x5 matrix for an RGBA image and a 6x6 for CMYKA
    (or RGBA with offsets).  The matrix is similar to those used by Adobe Flash
    except offsets are in column 6 rather than 5 (in support of CMYKA images)
    and offsets are normalized (divide Flash offset by 255).

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param width: the number of columns of ``color_matrix``.
    :type width: :class:`numbers.Integral`
    :param height: the number of rows of ``color_matrix``.
    :type height: :class:`numbers.Integral`
    :param color_matrix: the color matrix.
    :type color_matrix: :class:`collections.Sequence`,
                        :class:`numbers.Real`
    """
    if not isinstance(width, numbers.Integral):
        raise ValueError('width has to be a numbers.Integral, not ' +
                         repr(width))
    elif not isinstance(height, numbers.Integral):
        raise ValueError('height has to be a numbers.Integral, not ' +
                         repr(height))
    kernelinfo = KernelInfo(width, height, color_matrix)
    if kernelinfo:
        r = library.MagickColorMatrixImage(image.wand,
                                           ctypes.byref(kernelinfo))
        if not r:
            image.raise_exception()


def colorize(image, color, opacity):
    """blends the fill color with each pixel in the image.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param color: the fill color.
    :type color: :class:`wand.color.Color`
    :param opacity: the color represents opacity.
    :type opacity: :class:`wand.color.Color`
    """
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
    """adds a comment to your image.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param text: the image comment.
    :type text: :class:`str`
    """
    if not isinstance(text, string_type):
        raise TypeError('expected a string, not ' + repr(text))
    buffer = ctypes.create_string_buffer(text.encode())
    r = library.MagickCommentImage(image.wand, buffer)
    if not r:
        image.raise_exception()


def constitute(image, columns, rows, map, storage, pixels):
    """adds an image to the wand comprised of the pixel
    data you supply.  The pixel data must be in scanline order top-to-bottom.
    The data can be char, short int, int, float, or double(in C language).
    Float and double require the pixels to be normalized [0..1],
    otherwise [0..Max],  where Max is the maximum value
    the type can accomodate (e.g. 255 for char).

    For example, to create a 640x480 image from
    unsigned red-green-blue character data, use

        constitute(image,640,480,"RGB",'char',pixels);

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param columns: width in pixels of the image.
    :type columns: :class:`numbers.Integral`
    :param rows: height in pixels of the image.
    :type rows: :class:`numbers.Integral`
    :param map: This string reflects the expected ordering of the pixel array.
                It can be any combination or order of R = red, G = green,
                B = blue, A = alpha (0 is transparent),
                O = opacity (0 is opaque), C = cyan, Y = yellow, M = magenta,
                K = black, I = intensity (for grayscale), P = pad.
    :type map: :class:`str`
    :param storage: Define the data type of the pixels.
                    Float and double types are expected to be normalized [0..1]
                    otherwise [0..QuantumRange].
                    Choose from :const:`STORAGE_TYPES`.
    :type storage: :class:`str`
    :param pixels: This array of values contain the pixel components
                   as defined by map and type. You must preallocate this array
                   where the expected length varies depending on the values
                   of width, height, map, and type.
    :type pixels: :class:`collections.Sequence`,
                  :class:type of `storage`
    """
    if not isinstance(columns, numbers.Integral):
        raise ValueError('columns has to be a numbers.Integral, not ' +
                         repr(columns))
    elif not isinstance(rows, numbers.Integral):
        raise ValueError('rows has to be a numbers.Integral, not ' +
                         repr(rows))
    elif not isinstance(map, string_type):
        raise TypeError('expected a string, not ' + repr(map))
    elif storage not in STORAGE_TYPES:
        raise ValueError('expected string from STORAGE_TYPES, not ' +
                         repr(storage))
    elif not isinstance(pixels, collections.Sequence):
        raise TypeError('expecting sequence of arguments, not ' +
                        repr(pixels))

    map_buffer = ctypes.create_string_buffer(map.encode())
    storage_index = STORAGE_TYPES.index(storage)
    pixels_buffer = None
    length = len(pixels)

    if image.quantum_range > 256:
        qtype = ctypes.c_short
    else:
        qtype = ctypes.c_char

    storage_dic = {
        'char': ctypes.c_char,
        'double': ctypes.c_double,
        'float': ctypes.c_float,
        'integer': ctypes.c_int,
        'long': ctypes.c_long,
        'quantum': qtype,
        'short': ctypes.c_short
    }
    stype = storage_dic[storage]
    pixels_buffer = (stype * length)(*pixels)

    r = library.MagickConstituteImage(image.wand, columns, rows, map_buffer,
                                      storage_index, pixels_buffer)
    if not r:
        image.raise_exception()


def contrast(image, sharpen):
    """enhances the intensity differences between the lighter
    and darker elements of the image.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param sharpen: Increase or decrease image contrast.
    :type sharpen: :class:`bool`
    """
    if not isinstance(sharpen, bool):
        raise TypeError('sharpen must be a bool, not ' +
                        repr(sharpen))
    r = library.MagickContrastImage(image.wand, sharpen)
    if not r:
        image.raise_exception()


def convolve(image, order, kernel, channel=None):
    """applies a custom convolution kernel to the image.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param order: the number of columns and rows in the filter kernel.
    :type order: :class:`numbers.Integral`
    :param kernel: An array of doubles representing the convolution kernel.
    :type kernel: :class:`collections.Sequence`,
                  :class:`numbers.Real`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
                    If ``None``, select all channels.
    :type channel: :class:`str`
    """
    if not isinstance(order, numbers.Integral):
        raise ValueError('order has to be a numbers.Integral, not ' +
                         repr(order))
    elif not isinstance(kernel, collections.Sequence):
        raise TypeError('expecting sequence of arguments, not ' +
                        repr(kernel))
    assert(len(kernel) == order * order)
    p_kernel = (ctypes.c_double * len(kernel))(*kernel)
    if channel:
        if channel not in CHANNELS:
            raise ValueError('expected value from CHANNELS, not ' +
                             repr(channel))
        r = library.MagickConvolveImageChannel(image.wand, CHANNELS[channel],
                                               order, p_kernel)
    else:
        r = library.MagickConvolveImage(image.wand, order, p_kernel)
    if not r:
        image.raise_exception()


def cyclecolormap(image, displace):
    """displaces an image's colormap by a given number
    of positions.  If you cycle the colormap a number of times you can produce
    a psychodelic effect.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param displace: displace the colormap this amount.
    :type displace: :class:`numbers.Integral`
    """
    if not isinstance(displace, numbers.Integral):
        raise ValueError('displace has to be a numbers.Integral, not ' +
                         repr(displace))
    r = library.MagickCycleColormapImage(image.wand, displace)
    if not r:
        image.raise_exception()


def decipher(image, passphrase):
    """converts cipher pixels to plain pixels.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param passphrase: the passphrase.
    :type passphrase: :class:`str`
    """
    if not isinstance(passphrase, string_type):
        raise TypeError('expected a string, not ' + repr(passphrase))
    buffer = ctypes.create_string_buffer(passphrase.encode())
    r = library.MagickDecipherImage(image.wand, buffer)
    if not r:
        image.raise_exception()


def deskew(image, threshold):
    """removes skew from the image.  Skew is an artifact that
    occurs in scanned images because of the camera being misaligned,
    imperfections in the scanning or surface, or simply because the paper was
    not placed completely flat when scanned.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param threshold: separate background from foreground.
    :type threshold: :class:`numbers.Real`
    """
    if not isinstance(threshold, numbers.Real):
        raise TypeError('radius has to be a numbers.Real, not ' +
                        repr(threshold))
    r = library.MagickDeskewImage(image.wand, threshold)
    if not r:
        image.raise_exception()


def despeckle(image):
    """reduces the speckle noise in an image while
    perserving the edges of the original image.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    """
    r = library.MagickDespeckleImage(image.wand)
    if not r:
        image.raise_exception()


def edge(image, radius):
    """enhance edges within the image with a convolution filter
    of the given radius.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param radius: the radius of the pixel neighborhood.
                   if 0, suitable radius is selected.
    :type radius: :class:`numbers.Real`
    """
    if not isinstance(radius, numbers.Real):
        raise TypeError('radius has to be a numbers.Real, not ' +
                        repr(radius))
    r = library.MagickEdgeImage(image.wand, radius)
    if not r:
        image.raise_exception()


def emboss(image, radius, sigma):
    """returns a grayscale image with a three-dimensional
    effect.  We convolve the image with a Gaussian operator of the given radius
    and standard deviation (sigma).  For reasonable results, radius should be
    larger than sigma.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param radius: the radius of the Gaussian, in pixels,
                   not counting the center pixel.
                   if 0, suitable radius is selected.
    :type radius: :class:`numbers.Real`
    :param sigma: the standard deviation of the Gaussian, in pixels.
    :type sigma: :class:`numbers.Real`
    """
    if not isinstance(radius, numbers.Real):
        raise TypeError('radius has to be a numbers.Real, not ' +
                        repr(radius))
    elif not isinstance(sigma, numbers.Real):
        raise TypeError('sigma has to be a numbers.Real, not ' +
                        repr(sigma))
    r = library.MagickEmbossImage(image.wand, radius, sigma)
    if not r:
        image.raise_exception()


def encipher(image, passphrase):
    """converts plaint pixels to cipher pixels.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param passphrase: the passphrase.
    :type passphrase: :class:`str`
    """
    if not isinstance(passphrase, string_type):
        raise TypeError('expected a string, not ' + repr(passphrase))
    buffer = ctypes.create_string_buffer(passphrase.encode())
    r = library.MagickEncipherImage(image.wand, buffer)
    if not r:
        image.raise_exception()


def enhance(image):
    """applies a digital filter that improves the quality of a noisy image.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    """
    r = library.MagickEnhanceImage(image.wand)
    if not r:
        image.raise_exception()


def equalize(image, channel=None):
    """equalizes the image histogram.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
                    If ``None``, select all channels.
    :type channel: :class:`str`
    """
    if channel:
        if channel not in CHANNELS:
            raise ValueError('expected value from CHANNELS, not ' +
                             repr(channel))
        r = library.MagickEqualizeImageChannel(image.wand, CHANNELS[channel])
    else:
        r = library.MagickEqualizeImage(image.wand)
    if not r:
        image.raise_exception()


def extent(image, x, y, width, height):
    """extends the image as defined by the geometry, gravity,
    and background color.  Set the (x,y) offset of the geometry to move
    the original image relative to the extended image.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param x: the region x offset.
    :type x: :class:`numbers.Integral`
    :param y: the region y offset.
    :type y: :class:`numbers.Integral`
    :param width: the region width.
    :type width: :class:`numbers.Integral`
    :param height: the region height.
    :type height: :class:`numbers.Integral`
    """
    if not isinstance(x, numbers.Integral):
        raise TypeError('x has to be a numbers.Integral, not ' +
                        repr(x))
    elif not isinstance(y, numbers.Integral):
        raise TypeError('y has to be a numbers.Integral, not ' +
                        repr(y))
    elif not isinstance(width, numbers.Integral):
        raise TypeError('width has to be a numbers.Integral, not ' +
                        repr(width))
    elif not isinstance(height, numbers.Integral):
        raise TypeError('height has to be a numbers.Integral, not ' +
                        repr(height))
    r = library.MagickExtentImage(image.wand, width, height, x, y)
    if not r:
        image.raise_exception()


def filterimage(image, columns, rows, kernel, channel=None):
    """applies a custom convolution kernel to the image.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param columns: the columns of kernel.
    :type columns: :class:`numbers.Integral`
    :param rows: the rows of kernel.
    :type rows: :class:`numbers.Integral`
    :param kernel: An array of doubles representing the convolution kernel.
    :type kernel: :class:`collections.Sequence`,
                  :class:`numbers.Real`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
                    If ``None``, select all channels.
    :type channel: :class:`str`
    """
    if not isinstance(columns, numbers.Integral):
        raise TypeError('columns has to be a numbers.Integral, not ' +
                        repr(columns))
    elif not isinstance(rows, numbers.Integral):
        raise TypeError('rows has to be a numbers.Integral, not ' +
                        repr(rows))
    elif not isinstance(kernel, collections.Sequence):
        raise TypeError('expecting sequence of arguments, not ' +
                        repr(kernel))
    assert(columns * rows == len(kernel))
    kernelinfo = KernelInfo(columns, rows, kernel)
    if channel:
        if channel not in CHANNELS:
            raise ValueError('expected value from CHANNELS, not ' +
                             repr(channel))
        r = library.MagickFilterImageChannel(image.wand, CHANNELS[channel],
                                             ctypes.byref(kernelinfo))
    else:
        r = library.MagickFilterImage(image.wand, ctypes.byref(kernelinfo))
    if not r:
        image.raise_exception()


def floodfillpaint(image, fillcolor, fuzz, bordercolor, x, y,
                   invert=False, channel=None):
    """changes the color value of any pixel that matches
    target and is an immediate neighbor.  If the method FillToBorderMethod is
    specified, the color value is changed for any neighbor pixel that does not
    match the bordercolor member of image.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param fillcolor: the floodfill color.
    :type fillcolor: :class:`wand.color.Color`
    :param fuzz: By default target must match a particular pixel color exactly.
                 However, in many cases two colors may differ
                 by a small amount. The fuzz member of image defines how much
                 tolerance is acceptable to consider two colors as the same.
                 For example, set fuzz to 10 and the color red at intensities
                 of 100 and 102 respectively are now interpreted
                 as the same color for the purposes of the floodfill.
    :type fuzz: :class:`numbers.Real`
    :param bordercolor: the border color.
    :type bordercolor: :class:`wand.color.Color`
    :param x: x coord of the starting location.
    :type x: :class:`numbers.Integral`
    :param y: y coord of the starting location.
    :type y: :class:`numbers.Integral`
    :param invert: paint any pixel that does not match the target color.
    :type invert: :class:`bool`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
                    If ``None``, select all channels.
    :type channel: :class:`str`
    """
    if not isinstance(fillcolor, Color):
        raise TypeError('fillcolor must be a wand.color.Color, not ' +
                        repr(fillcolor))
    elif not isinstance(fuzz, numbers.Real):
        raise TypeError('fuzz has to be a numbers.Real, not ' +
                        repr(fuzz))
    elif not isinstance(bordercolor, Color):
        raise TypeError('bordercolor must be a wand.color.Color, not ' +
                        repr(bordercolor))
    elif not isinstance(x, numbers.Integral):
        raise TypeError('x has to be a numbers.Integral, not ' +
                        repr(x))
    elif not isinstance(y, numbers.Integral):
        raise TypeError('y has to be a numbers.Integral, not ' +
                        repr(y))
    elif not isinstance(invert, bool):
        raise TypeError('invert must be a bool, not ' +
                        repr(invert))
    if not channel:
        channel = 'default_channels'
    if channel not in CHANNELS:
            raise ValueError('expected value from CHANNELS, not ' +
                             repr(channel))
    with fillcolor:
        with bordercolor:
            r = library.MagickFloodfillPaintImage(image.wand,
                                                  CHANNELS[channel],
                                                  fillcolor.resource, fuzz,
                                                  bordercolor.resource, x, y,
                                                  invert)
            if not r:
                image.raise_exception()


def forwardfouriertransform(image, magnitude):
    """implements the discrete Fourier
    transform (DFT) of the image either as a magnitude / phase or real /
    imaginary image pair.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param magnitude: if true, return as magnitude / phase pair
                      otherwise a real / imaginary image pair.
    :type magnitude: :class:`bool`
    """
    if not isinstance(magnitude, bool):
        raise TypeError('magnitude must be a bool, not ' +
                        repr(magnitude))
    r = library.MagickForwardFourierTransformImage(image.wand, magnitude)
    if not r:
        image.raise_exception()


def haldclut(image, clutimage, channel=None):
    """replaces colors in the image from a Hald color lookup table.
    A Hald color lookup table is a 3-dimensional color cube mapped to 2
    dimensions.  Create it with the HALD coder.  You can apply any color
    transformation to the Hald image and then use this method to apply the
    transform to the image.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param clutimage: the hald CLUT image.
    :type clutimage: :class:`wand.image.Image`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
                    If ``None``, select all channels.
    :type channel: :class:`str`
    """
    if channel:
        if channel not in CHANNELS:
            raise ValueError('expected value from CHANNELS, not ' +
                             repr(channel))
        r = library.MagickHaldClutImageChannel(image.wand, CHANNELS[channel],
                                               clutimage.wand)
    else:
        r = library.MagickHaldClutImage(image.wand, clutimage.wand)
    if not r:
        image.raise_exception()


def implode(image, amount):
    """creates a new image that is a copy of an existing
    one with the image pixels "implode" by the specified percentage.  It
    allocates the memory necessary for the new Image structure and returns a
    pointer to the new image.

    :param image: target image.
    :type image: :class:`wand.image.Image`
    :param amount: Define the extent of the implosion.
    :type amount: :class:`numbers.Real`
    """
    if not isinstance(amount, numbers.Real):
        raise TypeError('amount has to be a numbers.Real, not ' +
                        repr(amount))
    r = library.MagickImplodeImage(image.wand, amount)
    if not r:
        image.raise_exception()


def inversefouriertransform(image1, image2, magnitude):
    """implements the inverse discrete
    Fourier transform (DFT) of the image either as a magnitude / phase
    or real / imaginary image pair.

    :param image1: magnitude-image or real-image.
                   furthermore, converted image is stored to image1
    :type image1: :class:`wand.image.Image`
    :param image2: phase-image or imaginary-image
    :type image2: :class:`wand.image.Image`
    :param magnitude: if True, images are used as a magnitude / phase pair
                      otherwise a real / imaginary image pair.
    :type magnitude: :class:`bool`
    """
    if not isinstance(magnitude, bool):
        raise TypeError('magnitude must be a bool, not ' +
                        repr(magnitude))
    r = library.MagickInverseFourierTransformImage(image1.wand,
                                                   image2.wand,
                                                   magnitude)
    if not r:
        image1.raise_exception()


def label(image, text):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param text:
    :type text: :class:`str`
    """
    if not isinstance(text, string_type):
        raise TypeError('expected a string, not ' + repr(text))
    buffer = ctypes.create_string_buffer(text.encode())
    r = library.MagickLabelImage(image.wand, buffer)
    if not r:
        image.raise_exception()


def localcontrast(image, radius, strength):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param radius:
    :type radius: :class:`numbers.Real`
    :param strength:
    :type strength: :class:`numbers.Real`
    """
    if not isinstance(radius, numbers.Real):
        raise TypeError('radius has to be a numbers.Real, not ' +
                        repr(radius))
    elif not isinstance(strength, numbers.Real):
        raise TypeError('strength has to be a numbers.Real, not ' +
                        repr(strength))
    r = library.MagickLocalContrastImage(image.wand, radius, strength)
    if not r:
        image.raise_exception()


def magnify(image):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    """
    r = library.MagickMagnifyImage(image.wand)
    if not r:
        image.raise_exception()


def minify(image):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    """
    r = library.MagickMinifyImage(image.wand)
    if not r:
        image.raise_exception()


def montage(image, drawing, tile_geometry, thumbnail_geometry, mode, frame):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param drawing:
    :type drawing: :class:`wand.drawing.Drawing`
    :param tile_geometry:
    :type tile_geometry: :class:`str`
    :param thumbnail_geometry:
    :type thumbnail_geometry: :class:`str`
    :param mode:
    :type mode: :class:`str`
    :param frame:
    :type frame: :class:`str`
    """
    if not isinstance(drawing, Drawing):
        raise TypeError('drawing must be a wand.drawing.Drawing instance, '
                        'not ' + repr(drawing))
    elif not isinstance(tile_geometry, string_type):
        raise TypeError('expected a string, not ' + repr(tile_geometry))
    elif not isinstance(thumbnail_geometry, string_type):
        raise TypeError('expected a string, not ' + repr(thumbnail_geometry))
    elif mode not in MONTAGE_MODES:
        raise ValueError('expected string from MONTAGE_MODES, not ' +
                         repr(mode))
    elif not isinstance(frame, string_type):
        raise TypeError('expected a string, not ' + repr(frame))
    tile_buffer = ctypes.create_string_buffer(tile_geometry.encode())
    thumb_buffer = ctypes.create_string_buffer(thumbnail_geometry.encode())
    frame_buffer = ctypes.create_string_buffer(frame.encode())
    mode_index = MONTAGE_MODES.index(mode)
    new_wand = library.MagickMontageImage(image.wand, drawing.resource,
                                          tile_buffer, thumb_buffer,
                                          mode_index, frame_buffer)
    image.raise_exception()
    if new_wand:
        return Image(image=BaseImage(new_wand))
    image.raise_exception()


def morphology(image, method, iterations, kernelinfo, channel=None):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param method:
    :type method: :class:`str`
    :param iterations:
    :type iterations: :class:`numbers.Integral`
    :param kernelinfo:
    :type kernelinfo: :class:`collections.Sequence`,
                      :class:`numbers.Real`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
                    If ``None``, select all channels.
    :type channel: :class:`str`
    """
    if method not in MORPHOLOGY_METHODS:
        raise ValueError('expected string from MORPHOLOGY_METHODS, not ' +
                         repr(method))
    elif not isinstance(iterations, numbers.Integral):
        raise ValueError('iterations has to be a numbers.Integral, not ' +
                         repr(iterations))
    methodindex = MORPHOLOGY_METHODS.index(method)
    kinfo = ctypes.create_string_buffer(kernelinfo.encode())
    kernel = libmagick.AcquireKernelInfo(kinfo)
    if channel:
        if channel not in CHANNELS:
            raise ValueError('expected value from CHANNELS, not ' +
                             repr(channel))
        r = library.MagickMorphologyImageChannel(image.wand, CHANNELS[channel],
                                                 methodindex, iterations,
                                                 kernel)
    else:
        r = library.MagickMorphologyImage(image.wand, methodindex,
                                          iterations, kernel)
    kernel = libmagick.DestroyKernelInfo(kernel)
    if not r:
        image.raise_exception()


def motionblur(image, radius, sigma, angle, channel=None):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param radius:
    :type radius: :class:`numbers.Real`
    :param sigma:
    :type sigma: :class:`numbers.Real`
    :param angle:
    :type angle: :class:`numbers.Real`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
                    If ``None``, select all channels.
    :type channel: :class:`str`
    """
    if not isinstance(radius, numbers.Real):
        raise TypeError('radius has to be a numbers.Real, not ' +
                        repr(radius))
    elif not isinstance(sigma, numbers.Real):
        raise TypeError('sigma has to be a numbers.Real, not ' +
                        repr(sigma))
    elif not isinstance(angle, numbers.Real):
        raise TypeError('angle has to be a numbers.Real, not ' +
                        repr(angle))
    if channel:
        if channel not in CHANNELS:
            raise ValueError('expected value from CHANNELS, not ' +
                             repr(channel))
        r = library.MagickMotionBlurImageChannel(image.wand, CHANNELS[channel],
                                                 radius, sigma, angle)
    else:
        r = library.MagickMotionBlurImage(image.wand, radius, sigma, angle)
    if not r:
        image.raise_exception()


def oilpaint(image, radius):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param radius:
    :type radius: :class:`numbers.Real`
    """
    if not isinstance(radius, numbers.Real):
        raise TypeError('radius has to be a numbers.Real, not ' +
                        repr(radius))
    r = library.MagickOilPaintImage(image.wand, radius)
    if not r:
        image.raise_exception()


def opaquepaint(image, target, fill, fuzz, invert=False, channel=None):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param target:
    :type target: :class:`wand.color.Color`
    :param fill:
    :type fill: :class:`wand.color.Color`
    :param fuzz:
    :type fuzz: :class:`numbers.Real`
    :param invert:
    :type invert: :class:`bool`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
                    If ``None``, select all channels.
    :type channel: :class:`str`
    """
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
            if channel:
                if channel not in CHANNELS:
                    raise ValueError('expected value from CHANNELS, not ' +
                                     repr(channel))
                r = library.MagickOpaquePaintImageChannel(image.wand,
                                                          CHANNELS[channel],
                                                          target.resource,
                                                          fill.resource,
                                                          fuzz, invert)
            else:
                r = library.MagickOpaquePaintImage(image.wand, target.resource,
                                                   fill.resource, fuzz, invert)
            if not r:
                image.raise_exception()


def orderedposterize(image, threshold_map, channel=None):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param threshold_map:
    :type threshold_map: :class:`str`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
                    If ``None``, select all channels.
    :type channel: :class:`str`
    """
    if not isinstance(threshold_map, string_type):
        raise TypeError('expected a string, not ' + repr(threshold_map))
    buffer = ctypes.create_string_buffer(threshold_map.encode())
    if channel:
        if channel not in CHANNELS:
            raise ValueError('expected value from CHANNELS, not ' +
                             repr(channel))
        r = library.MagickOrderedPosterizeImageChannel(image.wand,
                                                       CHANNELS[channel],
                                                       buffer)
    else:
        r = library.MagickOrderedPosterizeImage(image.wand, buffer)
    if not r:
        image.raise_exception()


def polaroid(image, drawing, angle):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param drawing:
    :type drawing: :class:`wand.drawing.Drawing`
    :param angle:
    :type angle: :class:`numbers.Real`
    """
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
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param levels:
    :type levels: :class:`numbers.Integral`
    :param dither:
    :type dither: :class:`bool`
    """
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
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param x:
    :type x: :class:`numbers.Integral`
    :param y:
    :type y: :class:`numbers.Integral`
    :param width:
    :type width: :class:`numbers.Integral`
    :param height:
    :type height: :class:`numbers.Integral`
    :param raiseeffect:
    :type raiseeffect: :class:`bool`
    """
    if not isinstance(x, numbers.Integral):
        raise TypeError('x has to be a numbers.Integral, not ' +
                        repr(x))
    elif not isinstance(y, numbers.Integral):
        raise TypeError('y has to be a numbers.Integral, not ' +
                        repr(y))
    elif not isinstance(width, numbers.Integral):
        raise TypeError('width has to be a numbers.Integral, not ' +
                        repr(width))
    elif not isinstance(height, numbers.Integral):
        raise TypeError('height has to be a numbers.Integral, not ' +
                        repr(height))
    elif not isinstance(raiseeffect, bool):
        raise TypeError('raiseeffect must be a bool, not ' +
                        repr(raiseeffect))
    r = library.MagickRaiseImage(image.wand, x, y, width, height, raiseeffect)
    if not r:
        image.raise_exception()


def randomthreshold(image, low, high, channel=None):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param low:
    :type low: :class:`numbers.Integral`
    :param high:
    :type high: :class:`numbers.Integral`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
                    If ``None``, select all channels.
    :type channel: :class:`str`
    """
    if not isinstance(low, numbers.Integral):
        raise TypeError('low has to be a numbers.Integral, not ' +
                        repr(low))
    elif not isinstance(high, numbers.Integral):
        raise TypeError('high has to be a numbers.Integral, not ' +
                        repr(high))
    if channel:
        if channel not in CHANNELS:
            raise ValueError('expected value from CHANNELS, not ' +
                             repr(channel))
        r = library.MagickRandomThresholdImageChannel(image.wand,
                                                      CHANNELS[channel],
                                                      low, high)
    else:
        r = library.MagickRandomThresholdImage(image.wand, low, high)
    if not r:
        image.raise_exception()


def remap(image, mapimage, method):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param mapimage:
    :type mapimage: :class:`wand.image.Image`
    :param method:
    :type method: :class:`str`
    """
    if method not in DITHER_METHODS:
        raise ValueError('expected value from DITHER_METHODS, not ' +
                         repr(method))
    index = DITHER_METHODS.index(method)
    r = library.MagickRemapImage(image.wand, mapimage.wand, index)
    if not r:
        image.raise_exception()


def resample(image, x_resolution, y_resolution, filtertype, blur):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param x_resolution:
    :type x_resolution: :class:`numbers.Real`
    :param y_resolution:
    :type y_resolution: :class:`numbers.Real`
    :param filter:
    :type filter: :class:`numbers.Integral`
    :param blur:
    :type blur: :class:`numbers.Real`
    """
    if not isinstance(x_resolution, numbers.Real):
        raise TypeError('x_resolution has to be a numbers.Real, not ' +
                        repr(x_resolution))
    elif not isinstance(y_resolution, numbers.Real):
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
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param x:
    :type x: :class:`numbers.Integral`
    :param y:
    :type y: :class:`numbers.Integral`
    """
    if not isinstance(x, numbers.Integral):
        raise TypeError('x has to be a numbers.Integral, not ' +
                        repr(x))
    elif not isinstance(y, numbers.Integral):
        raise TypeError('y has to be a numbers.Integral, not ' +
                        repr(y))
    r = library.MagickRollImage(image.wand, x, y)
    if not r:
        image.raise_exception()


def rotationalblur(image, angle, channel=None):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param angle:
    :type angle: :class:`numbers.Real`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
                    If ``None``, select all channels.
    :type channel: :class:`str`
    """
    if not isinstance(angle, numbers.Real):
        raise TypeError('angle has to be a numbers.Real, not ' +
                        repr(angle))
    if channel:
        if channel not in CHANNELS:
            raise ValueError('expected value from CHANNELS, not ' +
                             repr(channel))
        r = library.MagickRotationalBlurImageChannel(image.wand,
                                                     CHANNELS[channel],
                                                     angle)
    else:
        r = library.MagickRotationalBlurImage(image.wand, angle)
    if not r:
        image.raise_exception()


def scale(image, columns, rows):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param columns:
    :type columns: :class:`numbers.Integral`
    :param rows:
    :type rows: :class:`numbers.Integral`
    """
    if not isinstance(columns, numbers.Integral):
        raise TypeError('columns has to be a numbers.Integral, not ' +
                        repr(columns))
    elif not isinstance(rows, numbers.Integral):
        raise TypeError('rows has to be a numbers.Integral, not ' +
                        repr(rows))
    r = library.MagickScaleImage(image.wand, columns, rows)
    if not r:
        image.raise_exception()


def segment(image, colorspace, verbose, cluster_threshold, smooth_threshold):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param colorspace:
    :type colorspace: :class:`str`
    :param verbose:
    :type verbose: :class:`bool`
    :param cluster_threshold:
    :type cluster_threshold: :class:`numbers.Real`
    :param smooth_threshold:
    :type smooth_threshold: :class:`numbers.Real`
    """
    if colorspace not in COLORSPACE_TYPES:
        raise ValueError('colorspace value from COLORSPACE_TYPES, not ' +
                         repr(colorspace))
    elif not isinstance(verbose, bool):
        raise TypeError('verbose must be a bool, not ' +
                        repr(verbose))
    elif not isinstance(cluster_threshold, numbers.Real):
        raise TypeError('cluster_threshold has to be a numbers.Real, not ' +
                        repr(cluster_threshold))
    elif not isinstance(smooth_threshold, numbers.Real):
        raise TypeError('smooth_threshold has to be a numbers.Real, not ' +
                        repr(smooth_threshold))
    csindex = COLORSPACE_TYPES.index(colorspace)
    r = library.MagickSegmentImage(image.wand, csindex, verbose,
                                   cluster_threshold, smooth_threshold)
    if not r:
        image.raise_exception()


def selectiveblur(image, radius, sigma, threshold, channel=None):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param radius:
    :type radius: :class:`numbers.Real`
    :param sigma:
    :type sigma: :class:`numbers.Real`
    :param threshold:
    :type threshold: :class:`numbers.Real`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
                    If ``None``, select all channels.
    :type channel: :class:`str`
    """
    if not isinstance(radius, numbers.Real):
        raise TypeError('radius has to be a numbers.Real, not ' +
                        repr(radius))
    elif not isinstance(sigma, numbers.Real):
        raise TypeError('sigma has to be a numbers.Real, not ' +
                        repr(sigma))
    elif not isinstance(threshold, numbers.Real):
        raise TypeError('threshold has to be a numbers.Real, not ' +
                        repr(threshold))
    if channel:
        if channel not in CHANNELS:
            raise ValueError('expected value from CHANNELS, not ' +
                             repr(channel))
        r = library.MagickSelectiveBlurImageChannel(image.wand,
                                                    CHANNELS[channel],
                                                    radius, sigma, threshold)
    else:
        r = library.MagickSelectiveBlurImage(image.wand,
                                             radius, sigma, threshold)
    if not r:
        image.raise_exception()


def separate_channel(image, channel):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
    :type channel: :class:`str`
    """
    if channel not in CHANNELS:
        raise ValueError('channel value from CHANNELS, not ' +
                         repr(channel))
    r = library.MagickSeparateImageChannel(image.wand, CHANNELS[channel])
    if not r:
        image.raise_exception()


def sepiatone(image, threshold):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param threshold:
    :type threshold: :class:`numbers.Real`
    """
    if not isinstance(threshold, numbers.Real):
        raise TypeError('threshold has to be a numbers.Real, not ' +
                        repr(threshold))
    r = library.MagickSepiaToneImage(image.wand, threshold)
    if not r:
        image.raise_exception()


def setsizeoffset(image, columns, rows, offset):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param columns:
    :type columns: :class:`numbers.Integral`
    :param rows:
    :type rows: :class:`numbers.Integral`
    :param offset:
    :type offset: :class:`numbers.Integral`
    """
    if not isinstance(columns, numbers.Integral):
        raise TypeError('columns has be a numbers.Integral, not ' +
                        repr(columns))
    elif not isinstance(rows, numbers.Integral):
        raise TypeError('rows has to be a numbers.Integral, not ' +
                        repr(rows))
    elif not isinstance(offset, numbers.Integral):
        raise TypeError('offset has to be a numbers.Integral, not ' +
                        repr(offset))
    r = library.MagickSetSizeOffset(image.wand, columns, rows, offset)
    if not r:
        image.raise_exception()


def shade(image, gray, azimuth, elevation):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param gray:
    :type gray: :class:`bool`
    :param azimuth:
    :type azimuth: :class:`numbers.Real`
    :param elevation:
    :type elevation: :class:`numbers.Real`
    """
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
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param opacity:
    :type opacity: :class:`numbers.Real`
    :param sigma:
    :type sigma: :class:`numbers.Real`
    :param x:
    :type x: :class:`numbers.Integral`
    :param y:
    :type y: :class:`numbers.Integral`
    """
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


def sharpen(image, radius, sigma, channel=None):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param radius:
    :type radius: :class:`numbers.Real`
    :param sigma:
    :type sigma: :class:`numbers.Real`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
                    If ``None``, select all channels.
    :type channel: :class:`str`
    """
    if not isinstance(radius, numbers.Real):
        raise TypeError('radius has to be a numbers.Real, not ' +
                        repr(radius))
    elif not isinstance(sigma, numbers.Real):
        raise TypeError('sigma has to be a numbers.Real, not ' +
                        repr(sigma))
    if channel:
        if channel not in CHANNELS:
            raise ValueError('expected value from CHANNELS, not ' +
                             repr(channel))
        r = library.MagickSharpenImageChannel(image.wand, CHANNELS[channel],
                                              radius, sigma)
    else:
        r = library.MagickSharpenImage(image.wand, radius, sigma)
    if not r:
        image.raise_exception()


def shave(image, columns, rows):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param columns:
    :type columns: :class:`numbers.Integral`
    :param rows:
    :type rows: :class:`numbers.Integral`
    """
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
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param background:
    :type background: :class:`wand.color.Color`
    :param x:
    :type x: :class:`numbers.Real`
    :param y:
    :type y: :class:`numbers.Real`
    """
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


def sigmoidalcontrast(image, sharpen, alpha, beta, channel=None):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param sharpen:
    :type sharpen: :class:`bool`
    :param alpha:
    :type alpha: :class:`numbers.Real`
    :param beta:
    :type beta: :class:`numbers.Real`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
                    If ``None``, select all channels.
    :type channel: :class:`str`
    """
    if not isinstance(sharpen, bool):
        raise TypeError('sharpen must be a bool, not ' +
                        repr(sharpen))
    elif not isinstance(alpha, numbers.Real):
        raise TypeError('alpha has to be a numbers.Real, not ' +
                        repr(alpha))
    elif not isinstance(beta, numbers.Real):
        raise TypeError('beta has to be a numbers.Real, not ' +
                        repr(beta))
    if channel:
        if channel not in CHANNELS:
            raise ValueError('expected value from CHANNELS, not ' +
                             repr(channel))
        r = library.MagickSigmoidalContrastImageChannel(image.wand,
                                                        CHANNELS[channel],
                                                        sharpen, alpha, beta)
    else:
        r = library.MagickSigmoidalContrastImage(image.wand,
                                                 sharpen, alpha, beta)
    if not r:
        image.raise_exception()


def sketch(image, radius, sigma, angle):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param radius:
    :type radius: :class:`numbers.Real`
    :param sigma:
    :type sigma: :class:`numbers.Real`
    :param angle:
    :type angle: :class:`numbers.Real`
    """
    if not isinstance(radius, numbers.Real):
        raise TypeError('radius has to be a numbers.Real, not ' +
                        repr(radius))
    elif not isinstance(sigma, numbers.Real):
        raise TypeError('sigma has to be a numbers.Real, not ' +
                        repr(sigma))
    elif not isinstance(angle, numbers.Real):
        raise TypeError('angle has to be a numbers.Real, not ' +
                        repr(angle))
    r = library.MagickSketchImage(image.wand, radius, sigma, angle)
    if not r:
        image.raise_exception()


def solarize(image, threshold, channel=None):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param threshold:
    :type threshold: :class:`numbers.Real`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
                    If ``None``, select all channels.
    :type channel: :class:`str`
    """
    if not isinstance(threshold, numbers.Real):
        raise TypeError('threshold has to be a numbers.Real, not ' +
                        repr(threshold))
    if channel:
        if channel not in CHANNELS:
            raise ValueError('expected value from CHANNELS, not ' +
                             repr(channel))
        r = library.MagickSolarizeImageChannel(image.wand, CHANNELS[channel],
                                               threshold)
    else:
        r = library.MagickSolarizeImage(image.wand, threshold)
    if not r:
        image.raise_exception()


def sparsecolor(image, channel, method, arguments):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param channel:
    :type channel: :class:`str`
    :param method:
    :type method: :class:`str`
    :param arguments:
    :type arguments: :class:`collections.Sequence`,
                     :class:`numbers.Real`
    """
    if channel not in CHANNELS:
        raise ValueError('expected value from CHANNELS, not ' +
                         repr(channel))
    elif method not in SPARSE_METHODS:
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


def splice(image, x, y, width, height):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param x:
    :type x: :class:`numbers.Integral`
    :param y:
    :type y: :class:`numbers.Integral`
    :param width:
    :type width: :class:`numbers.Integral`
    :param height:
    :type height: :class:`numbers.Integral`
    """
    if not isinstance(x, numbers.Integral):
        raise TypeError('x has to be a numbers.Integral, not ' +
                        repr(x))
    elif not isinstance(y, numbers.Integral):
        raise TypeError('y has to be a numbers.Integral, not ' +
                        repr(y))
    elif not isinstance(width, numbers.Integral):
        raise TypeError('width has to be a numbers.Integral, not ' +
                        repr(width))
    elif not isinstance(height, numbers.Integral):
        raise TypeError('height has to be a numbers.Integral, not ' +
                        repr(height))
    r = library.MagickSpliceImage(image.wand, width, height, x, y)
    if not r:
        image.raise_exception()


def spread(image, method, amount):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param method:
    :type method: :class:`str`
    :param amount:
    :type amount: :class:`numbers.Real`
    """
    if method not in INTERPOLATEPIXEL_METHODS:
        raise ValueError('expected string from INTERPOLATEPIXEL_METHODS, ' +
                         'not ' + repr(method))
    elif not isinstance(amount, numbers.Real):
        raise TypeError('amount has to be a numbers.Real, not ' +
                        repr(amount))
    index = INTERPOLATEPIXEL_METHODS.index(method)
    r = library.MagickSpreadImage(image.wand, index, amount)
    if not r:
        image.raise_exception()


def statistic(image, statistic_type, width, height, channel=None):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param statistic_type:
    :type statistic_type: :class:`str`
    :param width:
    :type width: :class:`numbers.Integral`
    :param height:
    :type height: :class:`numbers.Integral`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
                    If ``None``, select all channels.
    :type channel: :class:`str`
    """
    if statistic_type not in STATISTIC_TYPES:
        raise ValueError('expected string from STATISTIC_TYPES, ' +
                         'not ' + repr(statistic_type))
    elif not isinstance(width, numbers.Integral):
        raise TypeError('width has to be a numbers.Integral, not ' +
                        repr(width))
    elif not isinstance(height, numbers.Integral):
        raise TypeError('height has to be a numbers.Integral, not ' +
                        repr(height))
    index = STATISTIC_TYPES.index(statistic_type)
    if channel:
        if channel not in CHANNELS:
            raise ValueError('expected value from CHANNELS, not ' +
                             repr(channel))
        r = library.MagickStatisticImageChannel(image.wand, CHANNELS[channel],
                                                index, width, height)
    else:
        r = library.MagickStatisticImage(image.wand, index, width, height)
    if not r:
        image.raise_exception()


def stegano(image, watermark, offset):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param watermark:
    :type watermark: :class:`wand.image.Image`
    :param offset:
    :type offset: :class:`numbers.Integral`
    """
    if not isinstance(offset, numbers.Integral):
        raise TypeError('offset has to be a numbers.Integral, not ' +
                        repr(offset))
    new_wand = library.MagickSteganoImage(image.wand, watermark.wand, offset)
    if new_wand:
        return Image(image=BaseImage(new_wand))
    image.raise_exception()


def stereo(image, offsetimage):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param offsetimage:
    :type offsetimage: :class:`wand.image.Image`
    """
    new_wand = library.MagickStereoImage(image.wand, offsetimage.wand)
    if new_wand:
        return Image(image=BaseImage(new_wand))
    image.raise_exception()


def swirl(image, degrees):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param degrees:
    :type degrees: :class:`numbers.Real`
    """
    if not isinstance(degrees, numbers.Real):
        raise TypeError('degrees has to be a numbers.Real, not ' +
                        repr(degrees))
    r = library.MagickSwirlImage(image.wand, degrees)
    if not r:
        image.raise_exception()


def texture(image, textureimage):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param textureimage:
    :type textureimage: :class:`wand.image.Image`
    """
    new_wand = library.MagickTextureImage(image.wand, textureimage.wand)
    if new_wand:
        return Image(image=BaseImage(new_wand))
    image.raise_exception()


def thumbnail(image, columns, rows):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param columns:
    :type columns: :class:`numbers.Integral`
    :param rows:
    :type rows: :class:`numbers.Integral`
    """
    if not isinstance(columns, numbers.Integral):
        raise TypeError('columns has to be a numbers.Integral, not ' +
                        repr(columns))
    elif not isinstance(rows, numbers.Integral):
        raise TypeError('rows has to be a numbers.Integral, not ' +
                        repr(rows))
    r = library.MagickThumbnailImage(image.wand, columns, rows)
    if not r:
        image.raise_exception()


def tint(image, tint, opacity):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param tint:
    :type tint: :class:`wand.color.Color`
    :param opacity:
    :type opacity: :class:`wand.color.Color`
    """
    if not isinstance(tint, Color):
        raise TypeError('tint must be a wand.color.Color instance, '
                        'not ' + repr(tint))
    elif not isinstance(opacity, Color):
        raise TypeError('opacity must be a wand.color.Color instance, '
                        'not ' + repr(opacity))
    with tint:
        with opacity:
            r = library.MagickTintImage(image.wand, tint.resource,
                                        opacity.resource)
            if not r:
                image.raise_exception()


def vignette(image, black, white, x, y):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param black:
    :type black: :class:`numbers.Real`
    :param white:
    :type white: :class:`numbers.Real`
    :param x:
    :type x: :class:`numbers.Integral`
    :param y:
    :type y: :class:`numbers.Integral`
    """
    if not isinstance(black, numbers.Real):
        raise TypeError('black has to be a numbers.Real, not ' +
                        repr(black))
    elif not isinstance(white, numbers.Real):
        raise TypeError('white has to be a numbers.Real, not ' +
                        repr(white))
    elif not isinstance(x, numbers.Integral):
        raise TypeError('x has to be a numbers.Integral, not ' +
                        repr(x))
    elif not isinstance(y, numbers.Integral):
        raise TypeError('y has to be a numbers.Integral, not ' +
                        repr(y))
    r = library.MagickVignetteImage(image.wand, black, white, x, y)
    if not r:
        image.raise_exception()


def wave(image, amplitude, wave_length):
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param amplitude:
    :type amplitude: :class:`numbers.Real`
    :param wave_length:
    :type wave_length: :class:`numbers.Real`
    """
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
    """

    :param image:
    :type image: :class:`wand.image.Image`
    :param threshold:
    :type threshold: :class:`wand.color.Color`
    """
    if not isinstance(threshold, Color):
        raise TypeError('threshold must be a wand.color.Color, not ' +
                        repr(threshold))
    with threshold:
        r = library.MagickWhiteThresholdImage(image.wand, threshold.resource)
        if not r:
            image.raise_exception()


if __name__ == '__main__':
    pass
