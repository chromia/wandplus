#!/usr/bin/env python

from wand.image import Image, BaseImage
from wand.image import CHANNELS, FILTER_TYPES, COLORSPACE_TYPES
from wand.image import COMPARE_METRICS, IMAGE_LAYER_METHOD
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
libmagick.GetMagickFeatures.restype = ctypes.c_char_p
libmagick.GetMagickFeatures.argtypes = [
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
library.MagickClipImagePath.restype = ctypes.c_bool
library.MagickClipImagePath.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p,
    ctypes.c_bool
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
library.MagickCoalesceImages.restype = ctypes.c_void_p
library.MagickCoalesceImages.argtypes = [
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
library.MagickCombineImages.restype = ctypes.c_void_p
library.MagickCombineImages.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int
]
library.MagickCommentImage.restype = ctypes.c_bool
library.MagickCommentImage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p
]
library.MagickCompareImageChannels.restype = ctypes.c_void_p
library.MagickCompareImageChannels.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_double)
]
library.MagickCompareImageLayers.restype = ctypes.c_void_p
library.MagickCompareImageLayers.argtypes = [
    ctypes.c_void_p,
    ctypes.c_int
]
library.MagickCompareImages.restype = ctypes.c_void_p
library.MagickCompareImages.argtypes = [
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_double)
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
library.MagickExportImagePixels.restype = ctypes.c_bool
library.MagickExportImagePixels.argtypes = [
    ctypes.c_void_p,
    ctypes.c_ssize_t,
    ctypes.c_ssize_t,
    ctypes.c_size_t,
    ctypes.c_size_t,
    ctypes.c_char_p,
    ctypes.c_int,
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
library.MagickResetImagePage.restype = ctypes.c_bool
library.MagickResetImagePage.argtypes = [
    ctypes.c_void_p,
    ctypes.c_char_p
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
library.MagickSetFirstIterator.restype = ctypes.c_bool
library.MagickSetFirstIterator.argtypes = [
    ctypes.c_void_p
]
library.MagickSetIteratorIndex.restype = ctypes.c_bool
library.MagickSetIteratorIndex.argtypes = [
    ctypes.c_void_p,
    ctypes.c_ssize_t
]
library.MagickSetLastIterator.restype = ctypes.c_bool
library.MagickSetLastIterator.argtypes = [
    ctypes.c_void_p
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
library.MagickGetVersion.restype = ctypes.c_char_p
library.MagickGetVersion.argtypes = [
    ctypes.POINTER(ctypes.c_size_t)
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

    :param image: the target image.
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

    :param image: the target image.
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

    :param image: the target image.
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

    :param image: the target image.
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

    :param dstimage: the target image.
    :type dstimage: :class:`wand.image.Image`
    :param srcimage: image(s) to be added.
    :type srcimage: :class:`wand.image.Image`
    """
    r = library.MagickAddImage(dstimage.wand, srcimage.wand)
    if not r:
        dstimage.raise_exception()


def addnoise(image, type, channel=None):
    """adds random noise to the image.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param type: The type of noise in :const:`NOISE_TYPES`.
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

    :param image: the target image.
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

    :param image: the target image.
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

    :param image: the target image.
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

    :param image: the target image.
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

    :param image: the target image.
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

    :param image: the target image.
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

    :param image: the target image.
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

    :param image: the target image.
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

    :param image: the target image.
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

    :param image: the target image.
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

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    """
    r = library.MagickClipImage(image.wand)
    if not r:
        image.raise_exception()


def clippath(image, pathname, inside):
    """clips along the named paths from the 8BIM profile, if present.
    Later operations take effect inside the path.  Id may be a number
    if preceded with #, to work on a numbered path,
    e.g., "#1" to use the first path.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param pathname: name of clipping path resource. If name is preceded by #,
                     use clipping path numbered by name.
    :type pathname: :class:`str`
    :param inside: if non-zero, later operations take effect
                   inside clipping path. Otherwise later operations take effect
                   outside clipping path.
    """
    if not isinstance(pathname, string_type):
        raise TypeError('expected a string, not ' + repr(pathname))
    elif not isinstance(inside, bool):
        raise TypeError('sharpen must be a bool, not ' +
                        repr(sharpen))
    buffer = ctypes.create_string_buffer(pathname.encode())
    r = library.MagickClipImagePath(image.wand, buffer, inside)
    if not r:
        image.raise_exception()


def clut(image, clutimage, channel=None):
    """replaces colors in the image from a color lookup table.

    :param image: the target image.
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


def coalesce(image):
    """composites a set of images while respecting any page
    offsets and disposal methods.  GIF, MIFF, and MNG animation sequences
    typically start with an image background and each subsequent image
    varies in size and offset.  MagickCoalesceImages() returns a new sequence
    where each image in the sequence is the same size as the first and
    composited with the next image in the sequence.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :rtype: :class:`wand.image.Image`
    """
    new_wand = library.MagickCoalesceImages(image.wand)
    if new_wand:
        return Image(image=BaseImage(new_wand))
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

    :param image: the target image.
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

    :param image: the target image.
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

    :param image: the target image.
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


def combine(image, channel):
    """combines one or more images into a single image.  The
    grayscale value of the pixels of each image in the sequence is assigned in
    order to the specified  hannels of the combined image.   The typical
    ordering would be image 1 => Red, 2 => Green, 3 => Blue, etc.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
                    and integer value will be accepted.
    :type channel: :class:`str` or :class:`numbers.Integral`
    """
    if channel not in CHANNELS:
        if isinstance(channel, numbers.Integral):
            index = channel
        else:
            raise ValueError('expected value from CHANNELS, not ' +
                             repr(channel))
    else:
        index = CHANNELS[channel]
    new_wand = library.MagickCombineImages(image.wand, index)
    if new_wand:
        return Image(image=BaseImage(new_wand))
    image.raise_exception()


def comment(image, text):
    """adds a comment to your image.

    :param image: the target image.
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


def compare(image, reference, metric='undefined', channel=None):
    """compares an image to a reconstructed image and returns
    the specified difference image.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param reference: the reference image.
    :type reference: :class:`wand.image.Image`
    :param metric: The metric type to use for comparing.
    :type metric: :class:`str`
    :returns: The difference image(:class:`wand.image.Image`),
              the computed distortion between the images
              (:class:`numbers.Integral`)
    :rtype: :class:`tuple`
    """
    if metric not in COMPARE_METRICS:
        raise ValueError('expected string from COMPARE_METRICS, not ' +
                         repr(type))
    metric = COMPARE_METRICS.index(metric)
    distortion = ctypes.c_double()
    if channel:
        if channel not in CHANNELS:
            raise ValueError('expected value from CHANNELS, not ' +
                             repr(channel))
        diff = library.MagickCompareImageChannels(image.wand, reference.wand,
                                                  CHANNELS[channel],
                                                  metric,
                                                  ctypes.byref(distortion))
    else:
        diff = library.MagickCompareImages(image.wand, reference.wand,
                                           metric, ctypes.byref(distortion))
    return Image(BaseImage(diff)), distortion.value


def comparelayer(image, method):
    """compares each image with the next in a sequence
    and returns the maximum bounding region of any pixel differences it
    discovers.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param method: the compare method in IMAGE_LAYER_METHOD.
    :type method: :class:`str`
    """
    if method not in IMAGE_LAYER_METHOD:
        raise ValueError('expected string from IMAGE_LAYER_METHOD, not ' +
                         repr(type))
    index = IMAGE_LAYER_METHOD.index(method)
    diff = library.MagickCompareImageLayers(image.wand, index)
    if diff:
        return Image(BaseImage(diff))
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

    :param image: the target image.
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

    :param image: the target image.
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

    :param image: the target image.
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

    :param image: the target image.
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

    :param image: the target image.
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

    :param image: the target image.
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

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    """
    r = library.MagickDespeckleImage(image.wand)
    if not r:
        image.raise_exception()


def edge(image, radius):
    """enhance edges within the image with a convolution filter
    of the given radius.

    :param image: the target image.
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

    :param image: the target image.
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

    :param image: the target image.
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

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    """
    r = library.MagickEnhanceImage(image.wand)
    if not r:
        image.raise_exception()


def equalize(image, channel=None):
    """equalizes the image histogram.

    :param image: the target image.
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


def export(image, x, y, columns, rows, map, storage):
    if not isinstance(x, numbers.Integral):
        raise TypeError('x has to be a numbers.Integral, not ' +
                        repr(x))
    elif not isinstance(y, numbers.Integral):
        raise TypeError('y has to be a numbers.Integral, not ' +
                        repr(y))
    elif not isinstance(columns, numbers.Integral):
        raise TypeError('columns has to be a numbers.Integral, not ' +
                        repr(columns))
    elif not isinstance(rows, numbers.Integral):
        raise TypeError('rows has to be a numbers.Integral, not ' +
                        repr(rows))
    elif not isinstance(map, string_type):
        raise TypeError('expected a string, not ' + repr(map))
    elif storage not in STORAGE_TYPES:
        raise ValueError('expected value from CHANNELS, not ' +
                         repr(storage))

    map_buffer = ctypes.create_string_buffer(map.encode())
    storage_index = STORAGE_TYPES.index(storage)

    storage_dic = {
        'char': ctypes.c_char,
        'double': ctypes.c_double,
        'float': ctypes.c_float,
        'integer': ctypes.c_int,
        'long': ctypes.c_long,
        'short': ctypes.c_short
    }
    storage_dic['quantum'] = storage_dic[getquantumtype()]
    stype = storage_dic[storage]
    length = columns * rows * len(map)
    pixels = (stype * length)()
    r = library.MagickExportImagePixels(image.wand, x, y, columns, rows,
                                        map_buffer, storage_index, pixels)
    if r:
        return pixels
    else:
        image.raise_exception()
        return None


def extent(image, x, y, width, height):
    """extends the image as defined by the geometry, gravity,
    and background color.  Set the (x,y) offset of the geometry to move
    the original image relative to the extended image.

    :param image: the target image.
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

    :param image: the target image.
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

    :param image: the target image.
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

    :param image: the target image.
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


def getquantumtype():
    """returns the Quantum type name.
    the type is defined by configuration on build.

    :returns: a string in STORAGE_TYPES.
    :rtype: :class:`str`
    """
    import re
    unknowntype = 'char'

    # get depth
    v = getversion()
    versionstring = v[3]
    m = re.findall(r'Q\d+', versionstring)
    if len(m) == 0:
        return unknowntype
    depth = int(m[0][1:])

    # check HDRI support
    features = libmagick.GetMagickFeatures().decode()
    HDRI = re.search(r'HDRI', features)

    # get quantum type(reference: magick/magick-type.h)
    if depth == 8:
        if HDRI:
            return 'float'
        else:
            return 'char'
    elif depth == 16:
        if HDRI:
            return 'float'
        else:
            return 'short'
    elif depth == 32:
        if HDRI:
            return 'double'
        else:
            return 'integer'
    elif depth == 64:
        return 'double'
    else:
        return unknowntype


def getversion():
    """returns the ImageMagick API version as a string constant
    and as a number.

    :returns: [major, minor, build, versionstring]
              e.g. [6, 9, 9, 'ImageMagick 6.9.9-36 Q8 x64 ...']
    :rtype: :class:`tuple`
    """
    version = ctypes.c_size_t()
    versionstring = library.MagickGetVersion(ctypes.byref(version))
    v = version.value
    major = v // 256
    minor = (v % 256) // 16
    build = v % 16
    return major, minor, build, versionstring.decode()


def haldclut(image, clutimage, channel=None):
    """replaces colors in the image from a Hald color lookup table.
    A Hald color lookup table is a 3-dimensional color cube mapped to 2
    dimensions.  Create it with the HALD coder.  You can apply any color
    transformation to the Hald image and then use this method to apply the
    transform to the image.

    :param image: the target image.
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

    :param image: the target image.
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
    """adds a label to your image.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param text: the image label text.
    :type text: :class:`str`
    """
    if not isinstance(text, string_type):
        raise TypeError('expected a string, not ' + repr(text))
    buffer = ctypes.create_string_buffer(text.encode())
    r = library.MagickLabelImage(image.wand, buffer)
    if not r:
        image.raise_exception()


def localcontrast(image, radius, strength):
    """attempts to increase the appearance of
    large-scale light-dark transitions. Local contrast enhancement works
    similarly to sharpening with an unsharp mask, however the mask is instead
    created using an image with a greater blur distance.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param radius: the radius of the Gaussian, in pixels,
                   not counting the center pixel.
    :type radius: :class:`numbers.Real`
    :param strength: the strength of the blur mask in percentage.
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
    """is a convenience method that scales an image
    proportionally to twice its original size.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    """
    r = library.MagickMagnifyImage(image.wand)
    if not r:
        image.raise_exception()


def minify(image):
    """is a convenience method that scales an image
    proportionally to one-half its original size

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    """
    r = library.MagickMinifyImage(image.wand)
    if not r:
        image.raise_exception()


def montage(image, drawing, tile_geometry, thumbnail_geometry, mode, frame):
    """creates a composite image by combining several
    separate images. The images are tiled on the composite image with the name
    of the image optionally appearing just below the individual tile.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param drawing: the drawing context.
    :type drawing: :class:`wand.drawing.Drawing`
    :param tile_geometry: the number of tiles per row and page
                          (e.g. 6x4+0+0).
    :type tile_geometry: :class:`str`
    :param thumbnail_geometry: Preferred image size and border size of each
                               thumbnail (e.g. 120x120+4+3>).
    :type thumbnail_geometry: :class:`str`
    :param mode: Thumbnail framing mode in :const:`MONTAGE_MODES`.
    :type mode: :class:`str`
    :param frame: Surround the image with an ornamental border
                  (e.g. 15x15+3+3).
                  The frame color is that of the thumbnail's matte color.
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
    """applies a user supplied kernel to the image
    according to the given mophology method.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param method: the morphology method in :const:`MORPHOLOGY_METHODS`.
    :type method: :class:`str`
    :param iterations: apply the operation this many times (or no change).
                       A value of -1 means loop until no change found.
                       How this is applied may depend on the morphology method.
                       Typically this is a value of 1.
    :type iterations: :class:`numbers.Integral`
    :param kernelinfo: a string representing the kernel
                       in format "\{kernel\}[:[k_args}]"
                       e.g. Diamond:4
                       see also http://www.imagemagick.org/Usage/morphology/
    :type kernelinfo: :class:`str`
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
    """simulates motion blur.  We convolve the image with a
    Gaussian operator of the given radius and standard deviation (sigma).
    For reasonable results, radius should be larger than sigma.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param radius: the radius of the Gaussian, in pixels,
                   not counting the center pixel.
                   if 0, suitable radius is selected.
    :type radius: :class:`numbers.Real`
    :param sigma: the standard deviation of the Gaussian, in pixels.
    :type sigma: :class:`numbers.Real`
    :param angle: Apply the effect along this angle.
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
    """applies a special effect filter that simulates an oil
    painting.  Each pixel is replaced by the most frequent color occurring
    in a circular region defined by radius.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param radius: the radius of the circular neighborhood.
    :type radius: :class:`numbers.Real`
    """
    if not isinstance(radius, numbers.Real):
        raise TypeError('radius has to be a numbers.Real, not ' +
                        repr(radius))
    r = library.MagickOilPaintImage(image.wand, radius)
    if not r:
        image.raise_exception()


def opaquepaint(image, target, fill, fuzz, invert=False, channel=None):
    """changes any pixel that matches color with the color defined by fill.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param target: Change this target color to the fill color within the image.
    :type target: :class:`wand.color.Color`
    :param fill: the fill color.
    :type fill: :class:`wand.color.Color`
    :param fuzz: By default target must match a particular pixel color exactly.
                 However, in many cases two colors may differ
                 by a small amount. The fuzz member of image defines how much
                 tolerance is acceptable to consider two colors as the same.
                 For example, set fuzz to 10 and the color red at intensities
                 of 100 and 102 respectively are now interpreted
                 as the same color for the purposes of the floodfill.
    :type fuzz: :class:`numbers.Real`
    :param invert: paint any pixel that does not match the target color.
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
    """performs an ordered dither based on a number
    of pre-defined dithering threshold maps, but over multiple intensity levels,
    which can be different for different channels, according to the input
    arguments.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param threshold_map: A string containing the name of the threshold dither
                          map to use, followed by zero or more numbers
                          representing the number of color levels
                          tho dither between.
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
    """simulates a Polaroid picture.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param drawing: the draw context.
    :type drawing: :class:`wand.drawing.Drawing`
    :param angle: Apply the effect along this angle.
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
    """reduces the image to a limited number of color level.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param levels: Number of color levels allowed in each channel.
                   Very low values (2, 3, or 4) have the most visible effect.
    :type levels: :class:`numbers.Integral`
    :param dither: if True, dither the mapped image.
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
    """creates a simulated three-dimensional button-like effect
    by lightening and darkening the edges of the image.  Members width and
    height of raise_info define the width of the vertical and horizontal
    edge of the effect.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param x: x coord of the area
    :type x: :class:`numbers.Integral`
    :param y: y coord of the area
    :type y: :class:`numbers.Integral`
    :param width: width of the area, in pixels.
    :type width: :class:`numbers.Integral`
    :param height: height of the area, in pixels.
    :type height: :class:`numbers.Integral`
    :param raiseeffect: if True, creates a 3-D raise effect.
                        otherwise, a lowered effect.
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
    """changes the value of individual pixels based on
    the intensity of each pixel compared to threshold.  The result is a
    high-contrast, two color image.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param low: low threshold in range 0..QuantumRange.
    :type low: :class:`numbers.Integral`
    :param high: high threshold in range 0..QuantumRange.
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
    """replaces the colors of an image with the closest color
    from a reference image.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param mapimage: the reference image.
    :type mapimage: :class:`wand.image.Image`
    :param method: dither method in :const:`DITHER_METHODS`.
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
    """resample image to desired resolution.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param x_resolution: the new image x resolution
    :type x_resolution: :class:`numbers.Real`
    :param y_resolution: the new image y resolution.
    :type y_resolution: :class:`numbers.Real`
    :param filter: Image filter in :const:`FILTER_TYPES`.
    :type filter: :class:`numbers.Integral`
    :param blur: the blur factor where > 1 is blurry, < 1 is sharp.
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


def resetpage(image, x, y, width=0, height=0):
    """resets the Wand page canvas and position.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param x: the x-offset of the new page.
    :type x: :class:`numbers.Integral`
    :param y: the y-offset of the new page.
    :type y: :class:`numbers.Integral`
    :param width: the width of the new page.
    :type width: :class:`numbers.Integral`
    :param height: the height of the new page.
    :type height: :class:`numbers.Integral`
    """
    if not isinstance(x, numbers.Integral):
        raise ValueError('x has to be a numbers.Integral, not ' +
                         repr(x))
    elif not isinstance(y, numbers.Integral):
        raise ValueError('y has to be a numbers.Integral, not ' +
                         repr(y))
    elif not isinstance(width, numbers.Integral):
        raise ValueError('width has to be a numbers.Integral, not ' +
                         repr(width))
    elif not isinstance(height, numbers.Integral):
        raise ValueError('height has to be a numbers.Integral, not ' +
                         repr(height))
    page = '{0}x{1}+{2}+{3}'.format(width, height, x, y)
    buffer = ctypes.create_string_buffer(page.encode())
    r = library.MagickResetImagePage(image.wand, buffer)
    if not r:
        image.raise_exception()


def roll(image, x, y):
    """offsets an image as defined by x and y.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param x: the x offset.
    :type x: :class:`numbers.Integral`
    :param y: the y offset.
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
    """rotational blurs an image.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param angle: the angle of the blur in degrees.
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
    """scales the size of an image to the given dimensions.

    :param image: the target image.
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
    r = library.MagickScaleImage(image.wand, columns, rows)
    if not r:
        image.raise_exception()


def segment(image, colorspace, verbose, cluster_threshold, smooth_threshold):
    """segments an image by analyzing the histograms of the
    color components and identifying units that are homogeneous with the fuzzy
    C-means technique.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param colorspace: the image colorspace in :const:`COLORSPACE_TYPES`.
    :type colorspace: :class:`str`
    :param verbose: Set to True to print detailed information
                    about the identified classes.
    :type verbose: :class:`bool`
    :param cluster_threshold: This represents the minimum number of pixels
                              contained in a hexahedra before it can be
                              considered valid (expressed as a percentage).
    :type cluster_threshold: :class:`numbers.Real`
    :param smooth_threshold: the smoothing threshold eliminates noise
                             in the second derivative of the histogram.
                             As the value is increased, you can expect a
                             smoother second derivative.
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
    """selectively blur an image within a contrast
    threshold. It is similar to the unsharpen mask that sharpens everything
    with contrast above a certain threshold.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param radius: the radius of the gaussian, in pixels,
                   not counting the center pixel.
    :type radius: :class:`numbers.Real`
    :param sigma: the standard deviation of the gaussian, in pixels.
    :type sigma: :class:`numbers.Real`
    :param threshold: only pixels within this contrast threshold are included
                      in the blur operation.
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
    """separates a channel from the image and returns a
    grayscale image.  A channel is a particular color component of each pixel
    in the image.

    :param image: the target image.
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
    """applies a special effect to the image, similar to the
    effect achieved in a photo darkroom by sepia toning.  Threshold ranges from
    0 to QuantumRange and is a measure of the extent of the sepia toning.  A
    threshold of 80% is a good starting point for a reasonable tone.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param threshold: Define the extent of the sepia toning.
    :type threshold: :class:`numbers.Real`
    """
    if not isinstance(threshold, numbers.Real):
        raise TypeError('threshold has to be a numbers.Real, not ' +
                        repr(threshold))
    r = library.MagickSepiaToneImage(image.wand, threshold)
    if not r:
        image.raise_exception()


def setfirstiterator(image):
    """sets the wand iterator to the first image.

    This function conflicts with wand.image.Image.sequence.
    Do NOT use together

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    """
    r = library.MagickSetFirstIterator(image.wand)
    if not r:
        image.raise_exception()


def setiteratorindex(image, index):
    """set the iterator to the given position in the
    image list specified with the index parameter.  A zero index will set
    the first image as current, and so on.  Negative indexes can be used
    to specify an image relative to the end of the images in the wand, with
    -1 being the last image in the wand.

    If the index is invalid (range too large for number of images in wand)
    the function will return False, but no 'exception' will be raised,
    as it is not actually an error.  In that case the current image will not
    change.

    After using any images added to the wand using wandplus.image.add() or
    wand.image.Image.read() will be added after the image indexed, regardless
    of if a zero (first image in list) or negative index (from end) is used.

    This function conflicts with wand.image.Image.sequence.
    Do NOT use together

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param index: the position in the image list.
    """
    if not isinstance(index, numbers.Integral):
        raise TypeError('index has be a numbers.Integral, not ' +
                        repr(index))
    r = library.MagickSetIteratorIndex(image.wand, index)
    if not r:
        image.raise_exception()


def setlastiterator(image):
    """sets the wand iterator to the last image.

    This function conflicts with wand.image.Image.sequence.
    Do NOT use together

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    """
    r = library.MagickSetLastIterator(image.wand)
    if not r:
        image.raise_exception()


def setsizeoffset(image, columns, rows, offset):
    """sets the size and offset of the magick wand.  Set it
    before you read a raw image format such as RGB, GRAY, or CMYK.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param columns: the image width in pixels.
    :type columns: :class:`numbers.Integral`
    :param rows: the image rows in pixels.
    :type rows: :class:`numbers.Integral`
    :param offset: the image offset.
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
    """shines a distant light on an image to create a
    three-dimensional effect. You control the positioning of the light with
    azimuth and elevation.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param gray: A value other than zero shades the intensity of each pixel.
    :type gray: :class:`bool`
    :param azimuth: azimuth is measured in degrees off the x axis
    :type azimuth: :class:`numbers.Real`
    :param elevation: elevation is measured in pixels above the Z axis.
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
    """simulates an image shadow.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param opacity: percentage transparency.
    :type opacity: :class:`numbers.Real`
    :param sigma: the standard deviation of the Gaussian, in pixels.
    :type sigma: :class:`numbers.Real`
    :param x: the shadow x-offset.
    :type x: :class:`numbers.Integral`
    :param y: the shadow y-offset.
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
    """sharpens an image.  We convolve the image with a
    Gaussian operator of the given radius and standard deviation (sigma).
    For reasonable results, the radius should be larger than sigma.

    :param image: the target image.
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
        r = library.MagickSharpenImageChannel(image.wand, CHANNELS[channel],
                                              radius, sigma)
    else:
        r = library.MagickSharpenImage(image.wand, radius, sigma)
    if not r:
        image.raise_exception()


def shave(image, columns, rows):
    """shaves pixels from the image edges.  It allocates the
    memory necessary for the new Image structure and returns a pointer to the
    new image.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param columns: the number of columns in the scaled image.
    :type columns: :class:`numbers.Integral`
    :param rows: the number of rows in the scaled image.
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
    """slides one edge of an image along the X or Y axis,
    creating a parallelogram.  An X direction shear slides an edge along the X
    axis, while a Y direction shear slides an edge along the Y axis.
    The amount of the shear is controlled by a shear angle.
    For X direction shears, x_shear is measured relative to the Y axis,
    and similarly, for Y direction shears y_shear is measured relative
    to the X axis.  Empty triangles left over from
    shearing the image are filled with the background color.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param background: the background color
    :type background: :class:`wand.color.Color`
    :param x: the number of degrees to shear the image.
    :type x: :class:`numbers.Real`
    :param y: the number of degrees to shear the image.
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
    """adjusts the contrast of an image with a
    non-linear sigmoidal contrast algorithm.  Increase the contrast of the
    image using a sigmoidal transfer function without saturating highlights or
    shadows.  Contrast indicates how much to increase the contrast (0 is none;
    3 is typical; 20 is pushing it); mid-point indicates where midtones fall in
    the resultant image (0 is white; 50% is middle-gray; 100% is black).

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param sharpen: Increase or decrease image contrast.
                    Set to True to increase the image contrast.
    :type sharpen: :class:`bool`
    :param alpha: strength of the contrast, the larger the number the more
                  'threshold-like' it becomes.
    :type alpha: :class:`numbers.Real`
    :param beta: midpoint of the function as a color value 0 to QuantumRange.
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
    """simulates a pencil sketch.  We convolve the image with
    a Gaussian operator of the given radius and standard deviation (sigma).
    For reasonable results, radius should be larger than sigma.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param radius: the radius of the Gaussian, in pixels,
                   not counting the center pixel.
                   if 0, suitable radius is selected.
    :type radius: :class:`numbers.Real`
    :param sigma: the standard deviation of the Gaussian, in pixels.
    :type sigma: :class:`numbers.Real`
    :param angle: Apply the effect along this angle.
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
    """applies a special effect to the image, similar to the
    effect achieved in a photo darkroom by selectively exposing areas of photo
    sensitive paper to light.  Threshold ranges from 0 to QuantumRange and is a
    measure of the extent of the solarization.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param threshold: Define the extent of the solarization.
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
    """given a set of coordinates, interpolates the colors found
    at those coordinates, across the whole image, using various methods.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param channel: the channel type. available values can be found
                    in the :const:`CHANNELS` mapping.
    :type channel: :class:`str`
    :param method: the method of image sparseion.
                   available values can be found in :const:`SPARSE_METHODS`.

                   TODO: more detailed information

    :type method: :class:`str`
    :param arguments: the arguments for this sparseion method.
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
    """splices a solid color into the image.

    :param image: the target image.
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
    r = library.MagickSpliceImage(image.wand, width, height, x, y)
    if not r:
        image.raise_exception()


def spread(image, amount):
    """is a special effects method that randomly displaces each
    pixel in a block defined by the radius parameter.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param amount: Choose a random pixel in a neighborhood of this extent.
    :type amount: :class:`numbers.Real`
    """
    if not isinstance(amount, numbers.Real):
        raise TypeError('amount has to be a numbers.Real, not ' +
                        repr(amount))
    r = library.MagickSpreadImage(image.wand, amount)
    if not r:
        image.raise_exception()


def statistic(image, statistic_type, width, height, channel=None):
    """replace each pixel with corresponding statistic from
    the neighborhood of the specified width and height.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param statistic_type: the statistic type in :const:`STATISTIC_TYPES`.
    :type statistic_type: :class:`str`
    :param width: the width of the pixel neighborhood.
    :type width: :class:`numbers.Integral`
    :param height: the height of the pixel neighborhood.
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
    """hides a digital watermark within the image.
    Recover the hidden watermark later to prove that the authenticity of
    an image.  Offset defines the start position within the image to hide
    the watermark.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param watermark: the watermark image.
    :type watermark: :class:`wand.image.Image`
    :param offset: Start hiding at this offset into the image.
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
    """composites two images and produces a single image that
    is the composite of a left and right image of a stereo pair.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param offsetimage: Another image.
    :type offsetimage: :class:`wand.image.Image`
    """
    new_wand = library.MagickStereoImage(image.wand, offsetimage.wand)
    if new_wand:
        return Image(image=BaseImage(new_wand))
    image.raise_exception()


def swirl(image, degrees):
    """swirls the pixels about the center of the image, where
    degrees indicates the sweep of the arc through which each pixel is moved.
    You get a more dramatic effect as the degrees move from 1 to 360.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param degrees: Define the tightness of the swirling effect.
    :type degrees: :class:`numbers.Real`
    """
    if not isinstance(degrees, numbers.Real):
        raise TypeError('degrees has to be a numbers.Real, not ' +
                        repr(degrees))
    r = library.MagickSwirlImage(image.wand, degrees)
    if not r:
        image.raise_exception()


def texture(image, textureimage):
    """repeatedly tiles the texture image across and down the image canvas.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param textureimage: the texture image.
    :type textureimage: :class:`wand.image.Image`
    """
    new_wand = library.MagickTextureImage(image.wand, textureimage.wand)
    if new_wand:
        return Image(image=BaseImage(new_wand))
    image.raise_exception()


def thumbnail(image, columns, rows):
    """changes the size of an image to the given dimensions
    and removes any associated profiles.  The goal is to produce small low cost
    thumbnail images suited for display on the Web.

    :param image: the target image.
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
    r = library.MagickThumbnailImage(image.wand, columns, rows)
    if not r:
        image.raise_exception()


def tint(image, tint, opacity):
    """applies a color vector to each pixel in the image.  The
    length of the vector is 0 for black and white and at its maximum for the
    midtones.  The vector weighting function is
    f(x)=(1-(4.0*((x-0.5)*(x-0.5)))).

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param tint: the tint pixel wand.
    :type tint: :class:`wand.color.Color`
    :param opacity: the color representing the opacity.
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
    """softens the edges of the image in vignette style.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param black: the black point.
    :type black: :class:`numbers.Real`
    :param white: the white point.
    :type white: :class:`numbers.Real`
    :param x: the x coord of the ellipse offset.
    :type x: :class:`numbers.Integral`
    :param y: the y coord of the ellipse offset.
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
    """creates a "ripple" effect in the image by shifting
    the pixels vertically along a sine wave whose amplitude and wavelength
    is specified by the given parameters.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param amplitude: the amplitude of the sine wave.
    :type amplitude: :class:`numbers.Real`
    :param wave_length: the wave length of the sine wave.
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
    """is like ThresholdImage() but  force all pixels
    above the threshold into white while leaving all pixels below the threshold
    unchanged.

    :param image: the target image.
    :type image: :class:`wand.image.Image`
    :param threshold: the color representing the threshold.
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
